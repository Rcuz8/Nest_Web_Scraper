# importing the requests library
import requests

# def main():
#
#     try :
#
#         # http://d8b674b7.ngrok.io?id=*&name=Ryan+Cocuzzo
#
#         # api-endpoint
#         URL = "http://d8b674b7.ngrok.io"  # "localhost:1234"
#
#         query_str = "/query_from_name"
#
#         URL += query_str
#
#         # location given here
#         name = "Ryan Cocuzzo"
#
#         id = "*"
#         # defining a params dict for the parameters to be sent to the API
#         PARAMS = {'name': name, 'id': id}
#
#         # sending get request and saving the response as response object
#         r = requests.get(url=URL, params=PARAMS)
#
#         print(r)
#         # # extracting data in json format
#         # data = r.json()
#         #
#         # print(data)
#
#     except NameError as error:
#
#         print("There was an error: ", error)
#
#
# main()

x = {"known_bucket_types":["buckets","delayed_topaz","demand_response","device","device_alert_dialog","geofence_info","kryptonite","link","message","message_center","metadata","occupancy","quartz","safety","rcs_settings","safety_summary","schedule","shared","structure","structure_history","structure_metadata","topaz","topaz_resource","track","trip","tuneups","user","user_alert_dialog","user_settings","where","widget_track"],"known_bucket_versions":[]}

import json

url1 = "https://home.nest.com/session"
d = {"email": "ryan.cocuzzo@gmail.com", "password": "Ryancocuzzo8"}

headers={
    "Accept": "*/*",
    "content-type":"application/json",
    "connection": "keep-alive",
    "Cookie": "eu_compliance=1; _gcl_au=1.1.195008639.1557949721; _ga=GA1.2.226734592.1557949722; _gid=GA1.2.1910414600.1557949722; __ssid=1f80cd586db7fa91a081ae1cfb9de13; _gaexp=GAX1.2.jGMmRTsxQn6WUOowxXM1cw.18102.2!uLZZRoWlS1y9D6mVFO226A.18087.1!mzDk5d9IRbKa2ZuuRSoR1Q.18115.1; viewer-volume=0.5; eu_cookie_accepted=1; n=eyJoYXMiOnsiMTI5MTY1NjQiOnsic3RyIjoxfX0sImlkcyI6WyIxMjkxNjU2NCJdfQ%3D%3D; _gat_UA-19609914-2=1",
    "host": "home.nest.com",
    "HostName": "home.nest.com",
    "Origin": "https://home.nest.com",
    "Referer": "https://home.nest.com/",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Mobile Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
}

r = requests.post(url=url1, headers=headers, json=d).json() # Response: 400 Bad request
print(r)
url2_ok = "https://home.nest.com/js/_vendors_/lib/phoenix-sdk/sdk-d4875ffcb3865568f87f.js "
r12b = requests.get(url=url2_ok)
print(r12b)
params3 = r["user"][-8:]
headers["Authorization"] = "Basic " + r['access_token']
print(headers["Authorization"])
# print(params3)
url3 = "https://home.nest.com/api/0.1/user/"+ params3 + "/app_launch"
print(url3)
r2 = requests.post(url=url3, params=x, headers=headers, json=x)
print(r2)
try:
    b = r2.json()
    print(b)
    url4 = "https://home.nest.com/dropcam/api/login"
    acc_tkn = r['access_token']
    url_addtl_data = b["updated_buckets"][0]["object_key"][18:]
    print(acc_tkn)
    p4 = {"access_token": acc_tkn}
    headers["Cookie"] = "eu_compliance=1; _gcl_au=1.1.195008639.1557949721; _ga=GA1.2.226734592.1557949722; _gid=GA1.2.1910414600.1557949722; __ssid=1f80cd586db7fa91a081ae1cfb9de13; _gaexp=GAX1.2.jGMmRTsxQn6WUOowxXM1cw.18102.2!uLZZRoWlS1y9D6mVFO226A.18087.1!mzDk5d9IRbKa2ZuuRSoR1Q.18115.1; viewer-volume=0.5; eu_cookie_accepted=1; n=eyJoYXMiOnsiMTI5MTY1NjQiOnsic3RyIjoxfX0sImlkcyI6WyIxMjkxNjU2NCJdfQ%3D%3D; website_2=0d6f4d63f72246659f699c8a2419b3e22583bc6c22e26c4be7875260e2bcf1f10fe1079f; _gat_UA-19609914-2=1; cztoken=" + acc_tkn
    r3 = requests.post(url=url4, params=p4, headers=headers, json=p4).json()
    session_tkn = r3[0]["session_token"]
    print(r3)

    #import urllib, urllib2, cookielib

    username = 'myuser'
    password = 'mypassword'

    import urllib.request

    opener = urllib.request.build_opener()
    print("Cookies: ", headers["Cookie"])
    opener.addheaders.append(('Cookie', headers["Cookie"]))
    f = opener.open("https://home.nest.com/home/"+url_addtl_data)
    print(f)
    # cj = cookielib.CookieJar()
    # opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    # login_data = urllib.urlencode({'username': username, 'j_password': password})
    # opener.open('http://www.example.com/login.php', login_data)
    # resp = opener.open('http://www.example.com/hiddenpage.php')
    # print
    # resp.read()



except ValueError:
    print("Could not decode Second JSON response")


