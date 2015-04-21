from plugin import *

class ookamimeh(plugin):
    def onEnable(self):
        self.historyID = ""
    
    def onAdvance(self, data):
        self.historyID = data.historyId

        print self.historyID

    def onChat(self, data):
        if data.message == ".i":
            r = self.getUser(data.uid)
            print r
            self.sendChat(r)
            

    def meh(self):
        print self.bot.REST("POST", "votes", {"direction":-1, "historyID": self.historyID})
        
        print "--------------------------------------"
