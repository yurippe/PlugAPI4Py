from plugin import *

class debug(plugin):

    def onRecv(self, data):
        print data
