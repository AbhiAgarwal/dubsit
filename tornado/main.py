#!/usr/bin/env python
import tornado.auth
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.autoreload
import tornado.websocket
import tornado.locale
import os.path
import uuid
from tornado.options import define, options

define("port", default = 8000, help = "run on the given port", type = int)
define("twitter_consumer_key", help = "The consumer key for Twitter", default = "ptihK8ip1Kk33qGwWZYhtQ")
define("twitter_consumer_secret", help = "The consumer secret", default = "rbeDljEnKh8ig8Vbpv0V6o33NMgxBM8WhAxmJt6Rtmc")
define("facebook_api_key", help = "your Facebook application API key", default = "")
define("facebook_secret", help = "your Facebook application secret", default = "")

i = 0
POLL_INTERVAL = 60

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/auth/twitter", AuthTwitterHandler),
            (r"/auth/facebook", AuthFacebookHandler),
            (r"/auth/logout", AuthLogoutHandler),
        ]
        settings = dict(
            cookie_secret = "8SGUe0QKS/ecvBl5WSYLw36RuNPtqEenqkIlAD0BoSY=",
            twitter_consumer_key = options.twitter_consumer_key,
            twitter_consumer_secret = options.twitter_consumer_secret,
            facebook_api_key = options.facebook_api_key,
            facebook_secret = options.facebook_secret,
            ui_modules = {'Post': PostModule, 'Tweet': TweetModule},
            cookie_secret = "43oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            login_url = "/",
            template_path = os.path.join(os.path.dirname(__file__), "templates"),
            static_path = os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies = True,
            debug = True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

class BaseHandler(tornado.web.RequestHandler):
    def get_current_twitter_user(self):
        user_json = self.get_secure_cookie("twitter_user")
        if not user_json: return None
        return tornado.escape.json_decode(user_json)

    def save_current_twitter_user(self, user):
        self.set_secure_cookie("twitter_user", tornado.escape.json_encode(user))

    def get_current_facebook_user(self):
        user_json = self.get_secure_cookie("facebook_user")
        if not user_json: return None
        return tornado.escape.json_decode(user_json)

    def save_current_facebook_user(self, user):
        self.set_secure_cookie("facebook_user", tornado.escape.json_encode(user))

class BaseHandler(tornado.web.RequestHandler):
    def get_current_twitter_user(self):
        user_json = self.get_secure_cookie("twitter_user")
        if not user_json: return None
        return tornado.escape.json_decode(user_json)

    def save_current_twitter_user(self, user):
        self.set_secure_cookie("twitter_user", tornado.escape.json_encode(user))

    def get_current_facebook_user(self):
        user_json = self.get_secure_cookie("facebook_user")
        if not user_json: return None
        return tornado.escape.json_decode(user_json)

    def save_current_facebook_user(self, user):
        self.set_secure_cookie("facebook_user", tornado.escape.json_encode(user))

class TweetMixin(object):
    waiters = {}
    polls = {}
    since_ids = {}

    def get_current_user(self):
        return self.get_current_twitter_user()

    def poll_twitter(self):
        user = self.get_current_twitter_user()
        import time
        cls = TweetMixin
        since_id = cls.since_ids.get(user['id'], 1)
        # print str(user['id']) + ' | since_id ' + str(since_id)
        timeout = cls.polls.get(user['id'], None)
        # Start polling if they havent already!
        if not timeout or timeout.deadline < time.time() and not self._finished:
            timeout = tornado.ioloop.IOLoop.instance().add_timeout(time.time() + POLL_INTERVAL, self.poll_twitter)
        self.polls[user['id']] = timeout
        # print self.polls
        args = dict(path = "/statuses/friends_timeline",
                             access_token=user["access_token"],
                             since_id = since_id,
                             count=30,
                             callback = self.async_callback(self.poll_twitter_cb))
        self.twitter_request(**args)

    def poll_twitter_cb(self, tweets):
        if tweets:
            user = self.get_current_twitter_user()
            # print str(user['id']) + " | retrieved " + str(len(tweets))
            cls = TweetMixin
            text = ""
            for tweet in tweets:
                # print tweet['id']
                text += self.render_string("modules/tweet.html", tweet=tweet, user=tweet['user'])
            cls.since_ids[user['id']] = int(tweets[0]['id'])
            self.finish(chunk=text) # needs to come before we kill the poller            
            timeout = self.polls[user['id']]
            if timeout and self._finished and timeout in tornado.ioloop.IOLoop.instance()._timeouts:
                tornado.ioloop.IOLoop.instance().remove_timeout(timeout)
                cls.polls[user['id']] = None

class FacebookMixin(object):
    waiters = {}
    polls = {}
    since_ids = {}

    def get_current_user(self):
        return self.get_current_facebook_user()
        
    def poll_facebook(self):
        user = self.get_current_facebook_user()
        import time
        cls = FacebookMixin
        # since_id = cls.since_ids.get(user['uid'], 1)
        # print str(user['id']) + ' | since_id ' + str(since_id)
        timeout = self.polls.get(user['uid'], None)
        # Start polling if they havent already!
        if not timeout or timeout.deadline < time.time() and not self._finished:
            timeout = tornado.ioloop.IOLoop.instance().add_timeout(time.time() + POLL_INTERVAL, self.poll_facebook)
        self.polls[user['uid']] = timeout
        args = dict(method="stream.get",
                    session_key= user["session_key"],
                    callback = self.async_callback(self.write_stream))

        if cls.since_ids.get(user['uid'], None):
            args['start_time'] = cls.since_ids[user['uid']]
            # print 'start_time: %d' % (args['start_time'])
        self.facebook_request(**args)
    
    def write_stream(self, stream):
        if stream is None:
            # Session may have expired
            self.redirect("/auth/login")
            #return

        if stream:
            cls = FacebookMixin
            user = self.get_current_facebook_user()
            posts = stream["posts"]
            if posts:
                text = self.get_text_from_stream(stream=stream)
                since_id = cls.since_ids.get(user['uid'], None)
                start_time = posts[0]['updated_time'] + 1
                if not since_id or start_time > since_id:
                    cls.since_ids[user['uid']]=start_time

                self.finish(chunk=text) # needs to come before we kill the poller
                
                timeout = self.polls[user['uid']]
                if timeout and self._finished and timeout in tornado.ioloop.IOLoop.instance()._timeouts:
                    tornado.ioloop.IOLoop.instance().remove_timeout(timeout)
                    self.polls[user['uid']] = None

    
    def get_text_from_stream(self, stream):
        text = ''
        stream["profiles"] = dict((p["id"], p) for p in stream["profiles"]) # mapping id => profile
        posts = stream["posts"]
        for post in posts:
            # print post
            # print "----------"
            try:
                text += self.render_string("modules/post.html", 
                                        post=post, 
                                        actor=stream["profiles"][post["actor_id"]])
            except:
                pass
        return text

class TwitterTimelineHandler(BaseHandler, TweetMixin, tornado.auth.TwitterMixin):
    # @tornado.web.authenticated
    @tornado.web.asynchronous
    def post(self):
        user = self.get_current_twitter_user()
        if user:
            self.async_callback(self.poll_twitter)()

class TwitterPreviousHandler(BaseHandler, TweetMixin, tornado.auth.TwitterMixin):
    # @tornado.web.authenticated
    @tornado.web.asynchronous 
    def post(self):
        user = self.get_current_twitter_user()
        if user:
            max_id = self.get_argument("max_id", None)
            if max_id:
                args = dict(path = "/statuses/friends_timeline",
                                     access_token=user["access_token"],
                                     max_id = int(max_id) - 1,
                                     callback = self.async_callback(self._on_post))
                self.twitter_request(**args)
    
    def _on_post(self, tweets):
        user = self.get_current_twitter_user()
        if user and tweets:
            text = ""
            for tweet in tweets:
                # print tweet['id']
                text += self.render_string("modules/tweet.html", tweet=tweet, user=tweet['user'])        
            self.finish(text)

class TwitterStatusHandler(BaseHandler, TweetMixin, tornado.auth.TwitterMixin):
    # @tornado.web.authenticated
    @tornado.web.asynchronous 
    def post(self):
        user = self.get_current_twitter_user()
        if user:
            status = self.get_argument("status", None)
            if status:
                args = dict(path = "/statuses/update",
                             access_token=user["access_token"],
                             post_args={'status': status},
                             callback = self.async_callback(self._on_post))
                self.twitter_request(**args)
    
    def _on_post(self, status):
        text = ""
        user = self.get_current_twitter_user()
        if user and status:
            text += self.render_string("modules/tweet.html", tweet=status, user=status['user'])
        self.finish(text)
        
class TwitterStatusLastHandler(BaseHandler, TweetMixin, tornado.auth.TwitterMixin):
    # @tornado.web.authenticated
    @tornado.web.asynchronous 
    def post(self):
        user = self.get_current_twitter_user()
        if user:
            args = dict(path = "/statuses/user_timeline",
                         access_token=user["access_token"],
                         count=1,
                         callback = self.async_callback(self._on_post))
            self.twitter_request(**args)
    
    def _on_post(self, statuses):
        text = ""
        user = self.get_current_twitter_user()
        if user and statuses:
            text += self.render_string("modules/tweet.html", tweet=statuses[0], user=statuses[0]['user'])
        self.finish(text)
            
class FacebookStreamHandler(BaseHandler, FacebookMixin, tornado.auth.FacebookMixin):
    #@tornado.web.authenticated
    @tornado.web.asynchronous
    def post(self):
        user = self.get_current_facebook_user()
        if user:
            self.async_callback(self.poll_facebook)()

class FacebookPreviousHandler(BaseHandler, FacebookMixin, tornado.auth.FacebookMixin):
    #@tornado.web.authenticated
    @tornado.web.asynchronous
    def post(self):
        user = self.get_current_facebook_user()
        if user:
            end_time = self.get_argument("end_time", None)
            if end_time:
                end_time = int(end_time) - 1
                start_time = (end_time - (60 *  60 * 24) )
                
                # print "%d / %d" % (start_time, end_time)
                args = dict(method="stream.get",
                            session_key= user["session_key"],
                            start_time = start_time,
                            end_time = end_time,
                            callback = self.async_callback(self._on_post))
                self.facebook_request(**args)
    
    def _on_post(self, stream):
        user = self.get_current_facebook_user()
        if user and stream:
            text = ""
            posts = stream["posts"]
            if posts:
                text = self.get_text_from_stream(stream=stream)            
            self.finish(text)


class FacebookStatusHandler(BaseHandler, FacebookMixin, tornado.auth.FacebookMixin):
    #@tornado.web.authenticated
    @tornado.web.asynchronous
    def post(self):
        user = self.get_current_facebook_user()
        if user:
            status = self.get_argument("status", None)
            if status:
                args = dict(method="stream.publish",
                            session_key= user["session_key"],
                            uid=user['uid'],
                            message=status,
                            callback = self.async_callback(self._on_post))
                self.facebook_request(**args)

    def _on_post(self, status):
        user = self.get_current_facebook_user()
        self.finish("updated")

class FacebookStatusLastHandler(BaseHandler, FacebookMixin, tornado.auth.FacebookMixin):
    #@tornado.web.authenticated
    @tornado.web.asynchronous
    def post(self):
        user = self.get_current_facebook_user()
        if user:
            args = dict(method="status.get",
                        session_key= user["session_key"],
                        uid=user['uid'],
                        limit=1,
                        callback = self.async_callback(self._on_post))
            self.facebook_request(**args)
            
    def _on_post(self, status):
        text = ""
        user = self.get_current_facebook_user()
        print status
        if user and status:
            if len(status) > 0:
                #[{u'source': 10732101402L, u'message': u'Our first post w @pingfm. 
                # Yep @MerchantCircle has just been added to ping.fm start updating MC w all of your other fav social networks',
                # u'status_id': 143652407725L, u'uid': 1562261327, u'time': 1254184501}]
                post = status[0]
                post['created_time'] = post.get('time')
                user['url'] = user.get('profile_url')
                text += self.render_string("modules/post.html", 
                                        post=post,
                                        actor=user)
                
        self.finish(text)

class AuthTwitterHandler(BaseHandler, tornado.auth.TwitterMixin):
    @tornado.web.asynchronous
    def get(self):
        if self.get_argument("oauth_token", None):
            self.get_authenticated_user(self.async_callback(self._on_auth))
            return
        self.authorize_redirect()

    def _on_auth(self, user):
        if not user:
            raise tornado.web.HTTPError(500, "Twitter auth failed")
        self.save_current_twitter_user(user)
        self.xsrf_token
        self.redirect("/")

class AuthFacebookHandler(BaseHandler, tornado.auth.FacebookMixin):
    @tornado.web.asynchronous
    def get(self):
        if self.get_argument("session", None):
            self.get_authenticated_user(self.async_callback(self._on_auth))
            return
        self.authorize_redirect("read_stream,publish_stream")
    
    def _on_auth(self, user):
        if not user:
            raise tornado.web.HTTPError(500, "Facebook auth failed")
        self.save_current_facebook_user(user)
        self.xsrf_token
        self.redirect(self.get_argument("next", "/"))

class AuthLogoutHandler(BaseHandler, tornado.auth.FacebookMixin):
    def get(self):
        logout = self.get_argument('logout', None)
        twitter_user = self.get_current_twitter_user()
        facebook_user = self.get_current_facebook_user()
        if logout == 'twitter':
            self.clear_cookie("twitter_user")
            twitter_user = None
        if logout == 'facebook':        
            self.clear_cookie("facebook_user")
            facebook_user = None
        if not twitter_user and not facebook_user:
            self.clear_cookie("_xsrf")
        self.redirect(self.get_argument("next", "/"))

class TweetModule(tornado.web.UIModule):
    def render(self, tweet, user=None):
        return self.render_string("modules/tweet.html", tweet=tweet, user=user)

class PostModule(tornado.web.UIModule):
    def render(self, post):
        return self.render_string("modules/post.html", post=post)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

def main():
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    tornado.autoreload.add_reload_hook(main)
    tornado.autoreload.start()
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()