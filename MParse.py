import json

class IncomingParser():

    def __init__(self, bot):
        self.bot = bot
        self.actions = {}
        self.actions["chat"] = self.chat
        self.actions["vote"] = self.vote

        
    def onRecv(self, message):
        m = str(message)
        if m == "h":return
        msg = json.loads(m)[0]

        if "a" in msg.keys():
            if msg["a"] in self.actions:
                self.actions[msg["a"]](msg)
                return
        print message
            
    def chat(self, msg):
        print msg["p"]["un"] + ": " + msg["p"]["message"]
        if msg["p"]["message"] == ".test":
            self.bot.sendChat("test you")

    def vote(self, msg):
        if msg["p"]["v"] == 1:
            print str(msg["p"]["i"]) + " woot'ed"
        elif msg["p"]["v"] == -1:
            print str(msg["p"]["i"]) + " meh'd"
        else:
            print str(msg["p"]["i"]) + " " + str(msg["p"]["v"])
