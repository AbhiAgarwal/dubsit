from mongo import analytics
import time

GIFRankHandler = analytics.getGIF()
NEWSRankHandler = analytics.getNews()

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        # GIFRankHandler
        if method.__name__ == 'GIFRankHandler':
            GIFRankHandler['avg'] = (GIFRankHandler['avg']*GIFRankHandler['iter'] + (te - ts))/(GIFRankHandler['iter']+1)
            GIFRankHandler['iter'] += 1
            analytics.averageTimeGIF(GIFRankHandler['avg'], GIFRankHandler['iter'])
        
        # NEWSRankHandler
        elif method.__name__ == 'NEWSRankHandler':
            NEWSRankHandler['avg'] = (NEWSRankHandler['avg']*NEWSRankHandler['iter'] + (te - ts))/(NEWSRankHandler['iter']+1)
            NEWSRankHandler['iter'] += 1
            analytics.averageTimeNews(NEWSRankHandler['avg'], NEWSRankHandler['iter'])

        return result
    return timed
