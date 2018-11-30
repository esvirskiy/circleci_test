#!/usr/bin/env python3
import requests, re

r = requests.get('http://httpbin.org/get')
data = r.text

ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', data)
ip2 = str(ip)
cleanIp = re.sub('\ |\[|\]|\'', '', ip2)
#f = open( 'request.log', 'w' )
#f.write(cleanIp)
#f.close()
print(cleanIp)
