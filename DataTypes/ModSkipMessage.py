class ModSkipMessage():
    #{u'a': u'modSkip', u'p': {u'mi': 5107634, u'm': u'TNC.Lizzie'}, u's': u'thenightcoreclub'}
    def __init__(self, data):
        self.data = data

        ##parse it here
        try: self.uid = data["p"]["mi"]
        except: self.uid = None

        try: self.userWhoSkiped = data["p"]["m"] #keep for legacy support
        except: self.userWhoSkiped = None

        try: self.mod = data["p"]["m"]
        except: self.mod = None
