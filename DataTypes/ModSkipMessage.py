class ModSkipMessage():
    #{u'a': u'modSkip', u'p': {u'mi': 5107634, u'm': u'TNC.Lizzie'}, u's': u'thenightcoreclub'}
    def __init__(self, data):
        self.data = data

        ##parse it here
        try: self.id = data["p"]["mi"]
        except: self.id = None

        try: self.userWhoSkiped = data["p"]["m"]
        except: self.userWhoSkiped = None
