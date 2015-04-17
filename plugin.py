import json
from DataTypes import *
class plugin():

    def __init__(self, bot):
        self.bot = bot

    def onRecv(self, message):
        m = str(message)
        if m == "h": return #this is just a ping of some sort
        msg = json.loads(m)[0]
        if msg["a"] == "chat": self.onChat(ChatMessage(msg))

    def onEnable(self):
        pass

    def sendChat(self, message):
        self.bot.sendChat(message)

    ##############################
    ##  Event Handlers          ##
    ##############################
    def onChat(self, chat_message):
        pass

##def EventHandler(event):
##    def wrap(func):
##        def wrapped_f(data):
##            data = str(data)
##            dat = json.loads(data)[0]
##            if(dat["a"] == event):
##                func(data)
##
##        return wrapped_f
##    return wrap
