from urllib import request

url = "http://localhost:8000/foundjs"
urlreq = request.urlopen(url)
urlres = urlreq.read()
print(urlres)