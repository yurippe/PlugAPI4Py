class ChatMessage():
    #{"a":"chat","p":{"cid":"4769627-1429306171276","message":"a","sub":0,"uid":4769627,"un":"OokamiHolo"},"s":"thenightcoreclub"}
    def __init__(self, data):
        self.data = data

        ##parse it here
        try: self.message = data["p"]["message"]
        except: self.message = None

        try: self.cid = data["p"]["cid"]
        except: self.cid = None

        try: self.uid = data["p"]["uid"]
        except: self.uid = None

        try: self.user = data["p"]["un"]
        except: self.user = None

        try: self.room = data["s"]
        except: self.room = None
    
