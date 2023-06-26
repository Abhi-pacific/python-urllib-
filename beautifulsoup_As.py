import requests
def scraping(url, file):
    r = requests.get(url)
    with open (file,'w') as f:
        f.write(r.text)
    with open(file,'r') as f:
        data = f.read()
def main():
    url = 'http://py4e-data.dr-chuck.net/comments_1738511.html'
    scraping(url, 'D:/python-urllib-/data.html')
main()
