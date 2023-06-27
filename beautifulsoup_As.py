import requests
import re
from bs4 import BeautifulSoup

def scraping(url,file):
    sum1 = 0
    r = requests.get(url)
    with open (file,'w') as r1:
        r1.write(str(r.text))
    with open (file,'r') as r2:
        mass = r2.read()
        soup = BeautifulSoup(mass,'html.parser')
        max1 = re.findall('[0-9]+',str(soup('span')))
        for max in max1:
            sum1 += int(max)
        print(sum1)
            

def main():
    url = 'http://py4e-data.dr-chuck.net/comments_1738511.html'
    scraping(url,'D:/python-urllib-/data.html')
main()
