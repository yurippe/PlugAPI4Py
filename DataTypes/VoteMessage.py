class VoteMessage():
    WOOT = 1
    MEH = -1
    #{u'a': u'vote', u'p': {u'i': 5113863, u'v': 1}, u's': u'thenightcoreclub'}
    def __init__(self, data):
        self.data = data

        ##parse it here
        try: self.uid = data["p"]["i"]
        except: self.uid = None

        try: self.vote = data["p"]["v"]
        except: self.vote = None
    
