operationCount = 0
GIFRankHandler = {'avg': 0, 'iter': 0}
NEWSRankHandler = {'avg': 0, 'iter': 0}

import time                                              
def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        #print '%r (%r, %r) %2.2f sec' % \
             # (method.__name__, args, kw, te-ts)
        if method.__name__ == 'GIFRankHandler':
        	GIFRankHandler['avg'] = (GIFRankHandler['avg']*GIFRankHandler['iter'] + (te - ts))/(GIFRankHandler['iter']+1)
        	GIFRankHandler['iter'] += 1
        elif method.__name__ == 'NEWSRankHandler':
            NEWSRankHandler['avg'] = (NEWSRankHandler['avg']*NEWSRankHandler['iter'] + (te - ts))/(NEWSRankHandler['iter']+1)
            NEWSRankHandler['iter'] += 1
        return result
    return timed