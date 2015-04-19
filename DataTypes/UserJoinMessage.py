#{u'a': u'userJoin', u'p': {u'username': u'Eldevin', u'gRole': 0, u'language': u'en', u'level': 4, u'avatarID': u'base12',
#u'joined': u'2015-04-16 02:31:47.846923', u'slug': u'eldevin', u'role': 0, u'badge': None, u'id': 6322241, u'sub': 0},
#u's': u'thenightcoreclub'}
class UserJoinMessage():
    def __init__(self, data):
        self.data = data

        ##parse it here
        try: self.user = data["p"]
        except: self.user = None
