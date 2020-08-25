import urllib, urllib.request

def get(url):
    return urllib.request.urlopen(url, None, 5).read().strip().decode()

