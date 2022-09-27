import requests 
import json 
from requests import auth


# url = "https://medium.com/m/signin"

user = "chrishoina@gmail.com"
password = "Easterntime#14rf@"

url = "https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F&source=--------------------------lo_home_nav-----------"

r = requests.get(url, auth = (user, password))
print(r.headers)
print(r.status_code)
print(r.cookies)
print(r.text)

# I found this URL in the console, but then removed everything after the query string (the "?"), and used that for the requests URL
# "/m/signin?operation=login&amp;redirect=https%3A%2F%2Fmedium.com%2F&amp;source=--------------------------lo_home_nav-----------"

# I found this to work for me even if I typically sign on through the Google Single-sign on. I just used the same email/password 
# that I do when I login directly to google (gmail). 


res =  ur.urlopen(url)
endres = res.geturl()
print(endres)


requests.get(url, auth = (user, password), stre am=True)
r2 = 
# r = s.get("https://medium.com/@chrishoina/stats/total/1661659200000/1664211293629")
print(r.content)
print(r2)

# https://medium.com/m/signin?redirect=https://medium.com/@chrishoina/stats/total/1661659200000/1664211293629&loginType=default
requests.s
s = requests.Sess

r = requests.get(url, auth = (user, password))

# print(s.cookies)

r2 = requests.get("https://medium.com/@chrishoina/stats/total/1661659200000/1664211293629")

print(r2.content)

def get_medium_stats(x):
    url = f'https://medium.com/m/signin/{}'
    r = s.get(url)
    sp = r.text
    print(sp)
    return
 

if__name-- == '__main__':
s = requests.Session()
x = 
    get_medium_stats()
# https://medium.com/@[Username]/stats?filter=not-response
# This looks to be the URL for individual article metrics. Need to explore further. 




/m/signin?operation=login&amp;redirect=https://medium.com/&;source=--------------------------lo_home_nav-----------