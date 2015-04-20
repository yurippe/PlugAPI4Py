class DjListUpdateMessage():
    #{u'a': u'djListUpdate', u'p': [6124312, ... 6163797], u's': u'thenightcoreclub'}
    def __init__(self, data):
        self.data = data

        ##parse it here
        try: self.users = data["p"] #keep for legacy support ?
        except: self.users = None

        try: self.djs = data["p"]
        except: self.djs = None
