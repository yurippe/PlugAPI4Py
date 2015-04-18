class UserLeaveMessage():
    #{u'a': u'vote', u'p': {u'i': 5113863, u'v': 1}, u's': u'thenightcoreclub'}
    def __init__(self, data):
        self.data = data

        ##parse it here
        try: self.id = data["p"]["u"]
        except: self.id = None
