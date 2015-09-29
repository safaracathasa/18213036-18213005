import re, urllib

textfile = file('test_1.txt', 'wt')
print "Enter the URL you wish to crawl.."
print 'Usage  - "http://phocks.org/stumble/creepy/" <-- With the double quotes'
myurl = input ("@> ")
for i in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(myurl).read(), re.I):
	print i
	textfile.write(i+'\n')
textfile.close()
