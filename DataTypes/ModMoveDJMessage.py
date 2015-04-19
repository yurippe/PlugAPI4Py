class ModMoveDJMessage():
    #{u'a': u'modMoveDJ', u'p': {u'mi': 5107634, u'm': u'TNC.Lizzie', u'u': u'Idle Im Banned', u'o': 16, u'n': 10}, u's': u'thenightcoreclub'}
    def __init__(self, data):
        self.data = data

        ##parse it here
        try: self.id = data["p"]["mi"]
        except: self.id = None

        try: self.nameWhoMoved = data["p"]["m"]
        except: self.nameWhoMoved = None
        
        try: self.nameMoved = data["p"]["u"]
        except: self.nameMoved = None
        
        try: self.from = data["p"]["o"]
        except: self.from = None
        
        try: self.to = data["p"]["n"]
        except: self.to = None
