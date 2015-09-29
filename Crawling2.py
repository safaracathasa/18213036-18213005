import urllib
import urllib2
from bs4 import BeautifulSoup

urllib.urlretrieve("http://viva.co.id/", "index.html")
soup = BeautifulSoup(open("index.html"))

i = 1

for anchor in soup.findAll('a', href=True):
	w = anchor['href']
	if (str(w).startswith( 'http' )):
		print w
		x = "Link ke-" + str(i) +" : " +soup.title.string +".html"
		urllib.urlretrieve( w, x)
		i = i+1
