from plugin import *

class ookamimeh(plugin):
    def onEnable(self):
        self.historyID = ""
    
    def onAdvance(self, data):
        self.historyID = data.historyId

        print self.historyID

    def onChat(self, data):
        if data.message == ".i":
            self.sendMeh()
            
