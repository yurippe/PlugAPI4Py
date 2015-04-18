from plugin import *

class SimpelPlugin(plugin):
 """a simpel chat plugin"""

 def onChat(self,chatmessage):
  if chatmessage.message == "cookie":
   sendChat(":cookie:")

  if chatmessage.message == ".omg":
   sendChat("http://dumpshare.net/images/4334790omg_really.png")
