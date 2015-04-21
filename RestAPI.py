import json
import requests

def REST(bot, method, endpoint, data):
    url = 'https://plug.dj/_/' + endpoint
    Cookies = {'session': 'cb87722d-91ca-4008-be9a-9cf8175b634a|2592000|cecaf6f29ee4aedad668c29f7d612c9245505984863cd8fda2cadf427aa255b4',
               }
    x =       { "doxygen_width" : "382", "__insp_slim":"1410877868274", "__insp_nv":"true",
               "__insp_ref":"aHR0cHM6Ly9wbHVnLmRqL3RoZW5pZ2h0Y29ZWNsdWl%3D",
               "wooTracker":"PapkJAwe1foy", "ajs_anonymous_id":"%220fc78d1e-0d1e-441e-8f96-435d4ffb0fca%22", "ajs_user_id":"4769627",
               "ajs_group_id":"null"}
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
    print data

REST(None, "POST", "votes", {"direction":-1, "historyID": "bf5f748d-3049-4f56-9998-d60b62969880"})
REST(None, "GET", "users/" + "4769627", "")
