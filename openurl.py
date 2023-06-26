import urllib.request, urllib.parse
from bs4 import BeautifulSoup
counts = dict()
file = urllib.request.urlopen('http://www.dr-chuck.com/page1.html').read()
soup = BeautifulSoup(file,'file.parser')
tags = soup('a')
for tag in tags:
    print(tag.get('href',None))
#for data in file:
 #   counts[data] = counts.get(data,0)+1
print(counts)