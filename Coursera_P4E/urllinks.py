# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input('Enter count: '))
pos = int(input('Enter position: '))
def open_url(x):
    html = urllib.request.urlopen(x, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    y = soup('a')
    return y


counter = 0
while counter < count:
    print("Retrieving:",url)
    tags = open_url(url)
    i = 1
    for tag in tags:
        if i == pos:
            url = tag.get('href', None)
            name = tag.contents[0]
            print("Position", i,":",name)
            break
        i = i + 1
    counter = counter + 1
print("Final name:", name,"\nDone!")
