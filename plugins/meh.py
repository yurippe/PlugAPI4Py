from plugin import *

class meh(plugin):

    def onChat(self, data):
        if data.message == ".meh":
            self.sendMeh()
            
