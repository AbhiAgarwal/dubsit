GiphyGIFAPI = {'avg': 0, 'iter': 0}
RedditGIFAPI = {'avg': 0, 'iter': 0}
TumblrGIFAPI = {'avg': 0, 'iter': 0}

import time                                              
def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        #print '%r (%r, %r) %2.2f sec' % \
             # (method.__name__, args, kw, te-ts)
        if method.__name__ == 'GiphyGIFAPI':
        	GiphyGIFAPI['avg'] = (GiphyGIFAPI['avg']*GiphyGIFAPI['iter'] + (te - ts))/(GiphyGIFAPI['iter']+1)
        	GiphyGIFAPI['iter'] += 1
        return result
    return timed