import requests
from bs4 import BeautifulSoup as bs
import json
import urllib.request
import ssl

# generic cookies
x = {"known_bucket_types":["buckets","delayed_topaz","demand_response","device","device_alert_dialog","geofence_info","kryptonite","link","message","message_center","metadata","occupancy","quartz","safety","rcs_settings","safety_summary","schedule","shared","structure","structure_history","structure_metadata","topaz","topaz_resource","track","trip","tuneups","user","user_alert_dialog","user_settings","where","widget_track"],"known_bucket_versions":[]}

# initial url
url1 = "https://home.nest.com/session"
#fill in your info
d = {"email": "ENTER USERNAME", "password": "ENTER PASSWORD"}
# establish the headers we're sending over
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

# Start requests!!

# Req 1
r = requests.post(url=url1, headers=headers, json=d).json()
print(r) #print it's JSON

#Not sure if this is necessary, but included it for good measure
url2_ok = "https://home.nest.com/js/_vendors_/lib/phoenix-sdk/sdk-d4875ffcb3865568f87f.js "
r12b = requests.get(url=url2_ok)
print(r12b)

# keep pulling info & using it as params
params3 = r["user"][-8:]
headers["Authorization"] = "Basic " + r['access_token']

# print the new important info we get
print(headers["Authorization"])
# print(params3)

# anooothhherrr one
url3 = "https://home.nest.com/api/0.1/user/"+ params3 + "/app_launch"
print(url3)
r2 = requests.post(url=url3, params=x, headers=headers, json=x)
print(r2)


try:
    b = r2.json()
    print(b)

    # fourth time gonna be the charm??
    url4 = "https://home.nest.com/dropcam/api/login"
    acc_tkn = r['access_token']
    url_addtl_data = b["updated_buckets"][0]["object_key"][18:]
    print(acc_tkn)
    p4 = {"access_token": acc_tkn}
    headers["Cookie"] = "eu_compliance=1; _gcl_au=1.1.195008639.1557949721; _ga=GA1.2.226734592.1557949722; _gid=GA1.2.1910414600.1557949722; __ssid=1f80cd586db7fa91a081ae1cfb9de13; _gaexp=GAX1.2.jGMmRTsxQn6WUOowxXM1cw.18102.2!uLZZRoWlS1y9D6mVFO226A.18087.1!mzDk5d9IRbKa2ZuuRSoR1Q.18115.1; viewer-volume=0.5; eu_cookie_accepted=1; n=eyJoYXMiOnsiMTI5MTY1NjQiOnsic3RyIjoxfX0sImlkcyI6WyIxMjkxNjU2NCJdfQ%3D%3D; website_2=0d6f4d63f72246659f699c8a2419b3e22583bc6c22e26c4be7875260e2bcf1f10fe1079f; _gat_UA-19609914-2=1; cztoken=" + acc_tkn
    r3 = requests.post(url=url4, params=p4, headers=headers, json=p4).json()
    session_tkn = r3[0]["session_token"]
    print(r3)


    # Boom, we're finally here!!
    opener = urllib.request.build_opener()
    print("Cookies: ", headers["Cookie"])
    opener.addheaders.append(('Cookie', headers["Cookie"]))
    f = opener.open("https://home.nest.com/home/"+url_addtl_data)
    readible_nest_unlocked = f.read()

    soup = bs(readible_nest_unlocked, features="html.parser")  # make BeautifulSoup
    prettyHTML = soup.prettify()  # prettify the html

    #finally... let's see what we're looking at


    # for good measure..
    print("")

    # Here it is..
    print(prettyHTML)

except ValueError:
    print("Could not decode some JSON response")
