#http://www.7timer.info/bin/astro.php?lon=38&lat=121&ac=0&unit=metric&output=json&tzshift=0
import requests
import json

lon = "38"
lat = "131"
urlString = "http://www.7timer.info/bin/api.pl?lon=" + lon + "&lat=" + lat + "&product=civil&output=json"


r = requests.get("http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=civil&output=json")

#print(r.text)
x = {}
x = json.loads(r.text)
print(x['dataseries'][0]['weather'])
