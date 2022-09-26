import requests
import json 
from requests.auth import HTTPBasicAuth

# I found this URL in the console, but then removed everything after the query string (the "?"), and used that for the requests URL
# "/m/signin?operation=login&amp;redirect=https%3A%2F%2Fmedium.com%2F&amp;source=--------------------------lo_home_nav-----------"

url = "https://medium.com/m/signin"
# I found this to work for me even if I typically sign on through the Google Single-sign on. I just used the same email/password 
# that I do when I login directly to google (gmail). 
user = "[Your login/email]"
password = "[Your password]"


r = requests.get(url, auth=HTTPBasicAuth(user, password))

print(r)

# https://medium.com/@[Username]/stats?filter=not-response
# This looks to be the URL for individual article metrics. Need to explore further. 




