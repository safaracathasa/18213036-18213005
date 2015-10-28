#Import Library
import os
import urllib
import urllib2
from bs4 import BeautifulSoup

#Variabel
url = 'http://www.itb.ac.id'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page)
tags = soup.findAll('img')

#Checking Image in Webpage
for tag in tags:
	filename = tag["src"].split("/")[-1]
	print tag['src']
	urllib.urlretrieve(url + tag['src'], filename)

#Do sync
os.system('rsync -r "/home/safara/Documents/Progif" "/home/safara/Documents/Progif/Gambar"')
