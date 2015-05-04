class AdvanceMessage():
    #{u'a': u'advance', u'p': {u'c': 6327320, u'd': [5388249,..., 6059187], u'h': u'143e121c-88bc-47ee-8995-ab47dd98fccd', u'm': {u'author': u'Nightcore', u'title': u'Break The World', u'image': u'http://i.ytimg.com/vi/EqIYqoXt-Go/default.jpg', u'format': 1, u'cid': u'EqIYqoXt-Go', u'duration': 162, u'id': 278833958}, u'p': 7097502, u't': u'2015-04-18 00:25:14.899831'}, u's': u'thenightcoreclub'}
    def __init__(self, data):
        self.data = data

        ##parse it here
        try: self.uid = data["p"]["c"]
        except: self.uid = None

        try: self.djs = data["p"]["d"]
        except: self.djs = None
        
        try: self.media = data["p"]["m"]
        except: self.media = None

        try: self.historyId = data["p"]["h"]
        except: self.historyId = None
        
        try: self.timeBegun = data["p"]["u"]
        except: self.timeBegun = None
