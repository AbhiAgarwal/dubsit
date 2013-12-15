#!/usr/bin/python
import json
import urllib

class google(object):

    def __init__(self):
        self.allResults = []
        self.currentResult = []

    def search(self, searchfor):
        query = urllib.urlencode({'q': searchfor})
        url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
        search_response = urllib.urlopen(url)
        search_results = search_response.read()
        results = json.loads(search_results)
        data = results['responseData']
        print 'Total results: %s' % data['cursor']['estimatedResultCount']
        hits = data['results']
        print 'Top %d hits:' % len(hits)
        for h in hits: print ' ', h['url']
        print 'For more results, see %s' % data['cursor']['moreResultsUrl']
