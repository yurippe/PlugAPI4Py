import time
import json
import glob
import os
import sys
sys.dont_write_bytecode = True

from ws4py.client.threadedclient import WebSocketClient
import requests
class WebSock(WebSocketClient):

    def init(this, bot):
        this.bot = bot

    def opened(this):
        #authenticate
        this.send(json.dumps({"a": "auth", "p": this.bot.authkey, "t": this.bot.getServerTime()}))

    def received_message(this, m):
        this.bot.onRecv(this, m)
                  
class Bot():
    def __init__(this, username, password, roomslug):
        this.username = username
        this.password = password
        this.roomslug = roomslug
        this.authkey = None
        this.ws = WebSock("wss://godj.plug.dj:443/socket")
        this.ws.init(this)
        this.plugins = {}

    def loadPlugins(this, folder):
        if folder.endswith("/"): slashornot = ""
        else: slashornot = "/"
        print "Appending '" + folder + slashornot + "' to sys.path"
        sys.path.append(folder + slashornot)
        print "Loading plugins from " + folder + slashornot
        for fil in glob.glob(folder + slashornot + "*.py"):
            friendly_name = ".".join(os.path.basename(fil).split(".")[:-1])
            print "Loading '" + friendly_name + "' ..."
            this.plugins[friendly_name] = {"import": __import__(friendly_name), "name":friendly_name}
            try:
                exec('this.plugins[friendly_name]["instance"] = this.plugins[friendly_name]["import"].' +
                 friendly_name + "(this)")
                print "Successfully loaded '" + friendly_name + "'"
                this.plugins[friendly_name]["instance"].onEnable()
            except:
                print "Failed loading plugin '" + friendly_name + "'(Class name must be the same as filename for plugins)"
                del this.plugins[friendly_name]

            
            
        #print this.plugins

        
    def onRecv(this, websocket, message):
        #print message
        for plugin in this.plugins.keys():
            this.plugins[plugin]["instance"].onRecv(message)

    def sendChat(this, msg):
        this.ws.send(json.dumps({"a":"chat", "p":msg, "t":this.getServerTime()}))

    def sendRawData(this, raw_data):
        this.ws.send(raw_data)
        
    def getServerTime(this):
        return int(time.time())
        
    def generateAuthkey(this):
        url = 'https://plug.dj/'
        with requests.Session() as my_session:
            dat = my_session.get(url)
            data = dat.text
            f1 = '_csrf = "'
            f2 = '", _fb'
            csrf = data[data.find(f1) + len(f1):data.find(f2)]
            #print "CSRF:" + csrf
            url = 'http://localhost:8000'
            url = 'https://plug.dj/_/auth/login'
            payload = {
            'csrf': csrf,
            'email': this.username,
            'password': this.password
            }
            dat_2 = my_session.post(url, headers={"User-Agent":"plugapi_1",
                                                  "Referer":"https://plug.dj",
                                                  "X-Requested-With": "XMLHttpRequest",
                                                  "Accept":"application/json, text/javascript, */*; q=0.01",
                                                  "Accept-Encoding":"gzip, deflate",
                                                  "Cache-Control":"no-cache",
                                                  "Accept-Language":"en-US,en;q=0.5",
                                                  "Pragma":"no-cache",
                                                  "Content-Type":"application/json;charset=UTF-8"}
                                    ,data=json.dumps(payload))
            data_2 = dat_2.text

            url = "https://plug.dj/" + this.roomslug
            dat_3 = my_session.get(url)
            data_3 = dat_3.text

            f1_3 = '_jm="'
            f2_3 = '",_st'
            authkey = data_3[data_3.find(f1_3) + len(f1_3):data_3.find(f2_3)]
            #print "Authkey: " + authkey
            this.authkey = authkey

    def start(this):
        this.generateAuthkey()
        this.ws.connect()
        this.ws.run_forever()
    
if __name__ == "__main__":
    bot = Bot("yurippenet@gmail.com", "password123", "thenightcoreclub")
    bot.loadPlugins("plugins")
    bot.start()
