import unicodedata

# Normalize Query function
def normalize(param1):
    query = unicodedata.normalize('NFKD', param1).encode('ascii','ignore')
    splitArray = query.split()
    query = " ".join(splitArray)
    return query