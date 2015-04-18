import json
from DataTypes import *
class plugin():

    def __init__(self, bot):
        self.bot = bot

    def onRecv(self, message):
        m = str(message)
        if m == "h": return #this is just a ping of some sort
        msg = json.loads(m)[0]
        if msg["a"] == "chat": 
            self.onChat(ChatMessage(msg))
            return
        if msg["a"] == "vote": 
            self.onVote(VoteMessage(msg))
            return
        if msg["a"] == "advance": 
            self.onAdvance(AdvanceMessage(msg))
            return
        if msg["a"] == "userLeave": 
            self.onUserLeave(UserLeaveMessage(msg))
            return
        if msg["a"] == "userJoin": 
            self.onUserJoin(UserJoinMessage(msg))
            return
        if msg["a"] == "djListUpdate":
            self.onDjListUpdate(DjListUpdateMessage(msg))
            return
        if msg["a"] == "grab":
            self.onGrab(UserLeaveMessage(msg))
            return
        
    def onEnable(self):
        pass

    def sendChat(self, message):
        self.bot.sendChat(message)
    
    def getUser(self, id):
        pass
    
    ##############################
    ##  Event Handlers          ##
    ##############################
    def onChat(self, chat_message):
        pass
    
    def onVote(self, vote_message):
        pass
    
    def onAdvance(self, advance_message):
        pass
    
    def onUserLeave(self, leave_message):
        pass
    
    def onUserJoin(self, join_message):
        pass
    
    def onDjListUpdate(self,djListUpdate_message):
        pass
    
    def onGrab(self,grab_message):
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
