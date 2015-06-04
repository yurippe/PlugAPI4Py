from plugin import *

class ChatPrinter(plugin):

    def onEnable(self):
        print ("Chat printer enabled")
        
    def onChat(self, msg):
        print (msg.user + ": " + msg.message)
