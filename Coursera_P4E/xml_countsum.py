import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
if len(url) < 1: url = "http://py4e-data.dr-chuck.net/comments_42.xml"
print('Retrieving:', url)
xml = urllib.request.urlopen(url).read().decode()
print('Retrieved', len(xml), 'characters')
tree = ET.fromstring(xml)
counts = tree.findall('comments/comment')
counter = 0
sum = 0
for item in counts:
    #print("Num:", item.find("count").text)
    sum = sum + int(item.find("count").text)
    counter = counter + 1
print("Count:", counter, "\nSum:", sum, "\nDone!")
