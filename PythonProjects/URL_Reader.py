import urllib.request
import urllib.parse
import csv

url = 'https://ftp.onechicago.com'
values = ('/position_limits/POSITION.LIMITS.20180213.csv')
webpage = urllib.request.urlopen(url)

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
csvData = csv.read()

print(csvData)
