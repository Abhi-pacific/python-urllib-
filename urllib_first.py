import urllib.request
import urllib.parse


url = 'https://www.google.com/search'
values = {'q':'pyhton programming tutorials'}

#Converting string string to url 
data = urllib.parse.urlencode(values)
#print(data)
data = data.encode('utf-8') #note internet understand utf-8

# Building request
req = urllib.request.Request(url, data)
# when we make request we get a responce 
resp = urllib.request.urlopen(req)
