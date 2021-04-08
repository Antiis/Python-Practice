import json, urllib.request, urllib.parse, urllib.error

url = input('Enter url: ')
if len(url) < 1: url = "http://py4e-data.dr-chuck.net/comments_42.json"
print('Retrieving:', url)
data = urllib.request.urlopen(url).read()
info = json.loads(data)
print('Retrieved', len(data),'characters')
counter = 0
sum = 0
for item in info['comments']:
    counter = counter + 1
    sum = sum + int(item['count'])

print("Count:", counter, "\nSum:", sum, "\nDone!")
