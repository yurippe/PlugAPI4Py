import time
import json
import glob
import os
import sys

import urllib2
import httplib

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
        this.cookies = {}
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
            try:
                this.plugins[plugin]["instance"].onRecv(message)
            except Exception as e:
                tempel1 = "|------------Error in plugin: %s-------------"%(this.plugins[plugin]["name"])
                print  tempel1 + "-|"
                print "|" + " "*((len(tempel1)-len(str(e)))/2) + str(e) + " "*((len(tempel1)-len(str(e)))/2) + "|"
                print "|" + "-"*len(tempel1) + "|"
                pass

    def sendChat(this, msg):
        #this.ws.send(json.dumps({"a":"chat", "p":msg[index:index+x], "t":this.getServerTime()}))
        if len(msg) <= 130:
            this.ws.send(json.dumps({"a":"chat", "p":msg, "t":this.getServerTime()}))
        else:
            index = 0
            while len(msg) > index:
                x = 130
                if index + x >= len(msg): x = len(msg) - index
                this.ws.send(json.dumps({"a":"chat", "p":msg[index:index+x], "t":this.getServerTime()}))
                index += x

    def sendRawData(this, raw_data):
        this.ws.send(raw_data)
        
    def getServerTime(this):
        return int(time.time())

    def getUser(this, userId):
        return this.REST("GET", "users/" + str(userId), "")

    def REST(this, method, endpoint, data):
        url = 'https://plug.dj/_/' + endpoint
        Cookies = this.cookies
        headers = {"Accept" : "application/json, text/javascript, */*; q=0.01",
                   "Content-Type": "application/json",
                   "User-Agent": "plugapi_1"}

        if(method.upper() == "GET"):
            resp = requests.get(url, data = json.dumps(data),
                         headers=headers, cookies=Cookies)
        elif(method.upper() == "POST"):
            print json.dumps(data)
            resp = requests.post(url, data = json.dumps(data),
                         headers=headers, cookies=Cookies)
        else: return

        data = resp.text
        return data

    def urllibGenerateAuthKey(this):
        def getCookies(urllibresponse):
            cookies = {}
            for header in urllibresponse.headers:
                header = header.strip()
                if header == "set-cookie":
                    h = urllibresponse.headers[header]
                    kv = h.split(";")[0]
                    k, v = kv.split("=")
                    cookies[k] = v
            return cookies
        url = "https://plug.dj/"
        resp1 = urllib2.urlopen(url)
        cookies = getCookies(resp1)
        data = resp1.read()
        f1 = '_csrf = "'
        f2 = '", _fb'
        csrf = data[data.find(f1) + len(f1):data.find(f2)]

        url = 'https://plug.dj/_/auth/login'
        payload = {
            'csrf': csrf,
            'email': this.username,
            'password': this.password
            }


        handler = urllib2.HTTPSHandler()
        opener = urllib2.build_opener(handler)
        Headers = {"User-Agent":"plugapi_1",
        "Referer":"https://plug.dj",
        "X-Requested-With": "XMLHttpRequest",
        "Accept":"application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding":"gzip, deflate",
        "Cache-Control":"no-cache",
        "Accept-Language":"en-US,en;q=0.5",
        "Pragma":"no-cache",
        "Content-Type":"application/json;charset=UTF-8",
        "Cookie":""}
        for cookie in cookies.keys():
            Headers["Cookie"] = Headers["Cookie"] + cookie + "=" + cookies[cookie] + ";"
        request = urllib2.Request(url, data=json.dumps(payload), headers=Headers )
        request.get_method = lambda: "POST"

        con = opener.open(request)
        print con.headers
        print con.read()
        return

            
    def generateAuthkey(this):
        url = 'https://plug.dj/'
        with requests.Session() as my_session:
            dat = my_session.get(url)
            data = dat.text
            f1 = '_csrf = "'
            f2 = '", _fb'
            csrf = data[data.find(f1) + len(f1):data.find(f2)]
            #print "CSRF:" + csrf
            #url = 'http://localhost:8000'
            url = 'https://plug.dj/_/auth/login'
            payload = {
            'csrf': csrf,
            'email': this.username,
            'password': this.password
            }
            tmpcookies = requests.utils.dict_from_cookiejar(my_session.cookies)
            tmpcookies["ajs_user_id"] = "null"
            dat_2 = my_session.post(url, headers={"User-Agent":"plugapi_1",
                                                  "Referer":"https://plug.dj",
                                                  "X-Requested-With": "XMLHttpRequest",
                                                  "Accept":"application/json, text/javascript, */*; q=0.01",
                                                  "Accept-Encoding":"gzip, deflate",
                                                  "Cache-Control":"no-cache",
                                                  "Accept-Language":"en-US,en;q=0.5",
                                                  "Pragma":"no-cache",
                                                  "Content-Type":"application/json;charset=UTF-8"}
                                    ,data=json.dumps(payload), cookies=tmpcookies)
            data_2 = dat_2.text

            url = "https://plug.dj/" + this.roomslug
            dat_3 = my_session.get(url)
            data_3 = dat_3.text

            this.cookies = requests.utils.dict_from_cookiejar(my_session.cookies)
            
            me = json.loads(this.getUser("me"))
            this.cookies["ajs_user_id"] = str(me["data"][0]["id"])
            f1_3 = '_jm="'
            f2_3 = '",_st'
            authkey = data_3[data_3.find(f1_3) + len(f1_3):data_3.find(f2_3)]
            #print "Authkey: " + authkey

            this.authkey = authkey
    def join(this):
        this.REST("POST", "rooms/join", {"slug": this.roomslug })
        
    def start(this):
        this.generateAuthkey()
        this.join()
        #this.urllibGenerateAuthKey()
        this.ws.connect()
        this.ws.run_forever()
    
if __name__ == "__main__":
    bot = Bot("yurippenet@gmail.com", "password123", "thenightcoreclub")
    bot.loadPlugins("plugins")
    bot.start()
