import requests
import json
from secrets import lat,lon 
import socket
from ipgeo import ipgeo

info = ipgeo.query('182.138.127.93')
print(info.latitude)

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(ip_address)


urlString = "http://www.7timer.info/bin/api.pl?lon=" + lon + "&lat=" + lat + "&product=civil&output=json"



r = requests.get(urlString)

#print(r.text)
x = {}
x = json.loads(r.text)
print(x['dataseries'][0]['weather'])
