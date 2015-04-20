#{u'a': u'userJoin', u'p': {u'username': u'Eldevin', u'gRole': 0, u'language': u'en', u'level': 4, u'avatarID': u'base12',
#u'joined': u'2015-04-16 02:31:47.846923', u'slug': u'eldevin', u'role': 0, u'badge': None, u'id': 6322241, u'sub': 0},
#u's': u'thenightcoreclub'}
class UserJoinMessage():
    def __init__(self, data):
        self.data = data

        ##parse it here
        try: self.userData = data["p"]
        except: self.userData = None

        try: self.user = data["p"]["username"]
        except: self.user = None

        try: self.gRole = data["p"]["gRole"]
        except: self.gRole = None

        try: self.level = data["p"]["level"]
        except: self.level = None

        try: self.avatar = data["p"]["avatarID"]
        except: self.avatar = None
        
        try: self.slug = data["p"]["slug"]
        except: self.slug = None

        try: self.role = data["p"]["role"]
        except: self.role = None
        
        try: self.badge = data["p"]["badge"]
        except: self.badge = None
        
        try: self.uid = data["p"]["id"]
        except: self.uid = None
        
        try:
            if data["p"]["sub"] == 0: self.subscriber = data["p"]["sub"] = False
            else: self.subscriber = True
        except: self.subscriber = None
        
