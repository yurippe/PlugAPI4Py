class ModMoveDJMessage():
    #{u'a': u'modMoveDJ', u'p': {u'mi': 5107634, u'm': u'TNC.Lizzie', u'u': u'Idle Im Banned', u'o': 16, u'n': 10}, u's': u'thenightcoreclub'}
    def __init__(self, data):
        self.data = data

        ##parse it here
        try: self.uid = data["p"]["mi"]
        except: self.uid = None

        try: self.nameWhoMoved = data["p"]["m"] #keep for legacy support ?
        except: self.nameWhoMoved = None

        try: self.mod = data["p"]["m"]
        except: self.mod = None
        
        try: self.nameMoved = data["p"]["u"] #keep for legacy support ?
        except: self.nameMoved = None

        try: self.movedUser = data["p"]["u"]
        except: self.movedUser = None
        
        try: self.from = data["p"]["o"] #keep for legacy support ?
        except: self.from = None

        try: self.fromPlace = data["p"]["o"]
        except: self.fromPlace = None
        
        try: self.to = data["p"]["n"] #keep for legacy support ?
        except: self.to = None

        try: self.toPlace = data["p"]["n"]
        except: self.toPlace = None
