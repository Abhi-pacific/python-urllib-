import requests
import re
from bs4 import BeautifulSoup
def scraping(url, file):
    r = requests.get(url)
    with open (file,'w') as f:
        f.write(r.text)
    with open(file,'r') as f:
        data = f.read()
    a = BeautifulSoup(data,'html.parser')
    mass = a.find_all('td')
    print(re.findall('[0-9]+',mass))

    
def main():
    url = 'http://py4e-data.dr-chuck.net/comments_1738511.html'
    scraping(url, 'D:/python-urllib-/data.html')
main()
