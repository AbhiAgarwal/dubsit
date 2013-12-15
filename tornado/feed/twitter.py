#!/usr/bin/env python
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket

class TwitterHandler(tornado.web.RequestHandler, tornado.auth.TwitterMixin):
        @tornado.web.asynchronous
        def get(self):
                oAuthToken = self.get_secure_cookie('access_key')
                oAuthSecret = self.get_secure_cookie('access_secret')
                userID = self.get_secure_cookie('user_id')

                if self.get_argument('oauth_token', None):
                        self.get_authenticated_user(self.async_callback(self._twitter_on_auth))
                        return

                elif oAuthToken and oAuthSecret:
                        accessToken = {
                                'key': oAuthToken,
                                'secret': oAuthSecret
                        }
                        self.twitter_request('/users/show',
                                access_token=accessToken,
                                user_id=userID,
                                callback=self.async_callback(self._twitter_on_user)
                        )
                        return

                self.authorize_redirect()

        def _twitter_on_auth(self, user):
                if not user:
                        self.clear_all_cookies()
                        raise tornado.web.HTTPError(500, 'Twitter authentication failed')

                self.set_secure_cookie('user_id', str(user['id']))
                self.set_secure_cookie('access_key', user['access_token']['key'])
                self.set_secure_cookie('access_secret', user['access_token']['secret'])

                self.redirect('/')

        def _twitter_on_user(self, user):
                if not user:
                        self.clear_all_cookies()
                        raise tornado.web.HTTPError(500, "Couldn't retrieve user information")
                self.write(tornado.escape.json_encode(user))

class TwitterLogoutHandler(tornado.web.RequestHandler):
        def get(self):
                self.clear_all_cookies()
                self.redirect('/')
