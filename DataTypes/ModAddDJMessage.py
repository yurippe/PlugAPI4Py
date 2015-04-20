class ModAddDJMessage():
    #{u'a': u'modAddDJ', u'p': {u'mi': 5107634, u'm': u'TNC.Lizzie', u't': u'Chocacho'}, u's': u'thenightcoreclub'}
    def __init__(self, data):
        self.data = data

        ##parse it here
        try: self.uid = data["p"]["mi"]
        except: self.uid = None

        try: self.userWhoAdded = data["p"]["m"] #keep for legacy support ?
        except: self.userWhoAdded = None

        try: self.mod = data["p"]["m"]
        except: self.mod = None
        
        try: self.userAdded = data["p"]["t"]
        except: self.userAdded = None
