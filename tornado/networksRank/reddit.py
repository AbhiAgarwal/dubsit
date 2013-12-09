from math import log
from boost import weights
from math import sqrt
# different models of rankings

# traditional ups, downs, comments and logs
def GIFscore(ups, downs, comments):
	# scoring for reddit's gifs
	s = (ups - downs) + comments
	order = log(max(abs(s), 1), 10)
	toReturn = (order * weights.weighing['GIFreddit'])
	# for future gifs
	weights.weight += order
	weights.iterations += 1
	weights.average = (weights.weight / weights.iterations)
	return toReturn

    # traditional ups, downs, comments and logs
def NEWSscore(ups, downs, comments):
    # scoring for reddit's gifs
    s = (ups - downs) + comments
    order = log(max(abs(s), 1), 10)
    toReturn = (order * weights.weighing['NEWSreddit'])
    # for future gifs
    weights.weight += order
    weights.iterations += 1
    weights.average = (weights.weight / weights.iterations)
    return toReturn

# wilson score interval
# http://amix.dk/uploads/wilsons_score_interval.png
# http://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval#Wilson_score_interval
# n is the total number of ratings
# zalpha/2 is the (1-alpha/2) quantile of the standard normal distribution
# phat is the observed fraction of positive ratings
def wilson(ups, downs, comments):
    n = ups + downs
    if n == 0:
        return 0
    z = 1.0
    phat = (float(ups) / n)
    ranking = sqrt(phat + z * z / (2 * n) - z * ((phat * (1 - phat) + z * z / (4 * n)) / n)) / (1 + z * z / n)
    return ranking
