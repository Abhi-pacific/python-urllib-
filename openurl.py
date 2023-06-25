import urllib.request
counts = dict()
file = urllib.request.urlopen('https://www.google.com/')
for data in file:
    counts[data] = counts.get(data,0)+1
print(counts)