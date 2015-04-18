from plugin import *

class arne(plugin):

    def onEnable(self):
        pass
        
    def onChat(self, msg):
        if "cookies" in msg.message:
            self.sendChat(":cookie::cookie::cookie:")
        if msg.message == ".christie":
            self.sendChat("http://fc02.deviantart.net/fs71/f/2012/157/b/b/pusheen_carameldansen_by_stardustmoondust462-d52grff.png")
        if "HOUDHAKKER" in msg.message:
            self.sendChat("Christie I understand that you want to kill my creator. And if you can please do it quick.")
        if "hello" in msg.message and "@Arne" in msg.message:
            self.sendChat("@" + msg.user + " hello.")
        if "potato" in msg.message:
            self.sendChat("@Darkx143")
    
    def onVote(self,msg):
        if msg.vote == -1:
            self.sendChat("who meh")