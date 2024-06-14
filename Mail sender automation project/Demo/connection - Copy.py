import urllib.request as urllib2
def is_connected():
    print("Inside connection")
    try:
        urllib2.urlopen('http://www.google.com',timeout=1)
        return True
    except urllib2.URLError as err:
        return False
