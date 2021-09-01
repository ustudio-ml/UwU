try:
	import os
	import sys
	import requests
	import optparse
	import json
except ImportError:
	print "Error bang/sis :("

try:
	parser = optparse.OptionParser()
	parser.add_option("-u", "--url", help="website url", dest="urlpro")
	opt, args = parser.parse_args()
	if opt.urlpro:
		url = opt.urlpro
except NameError:
	print "Error bang/sis :("

##########
res = requests.get("http://ip-api.com/json/%s"%(url))
getdata = res.json()
status = getdata["status"]
ip = getdata["query"]
country = getdata["country"]
os.system("clear")
print "-"*44
print "Status : "+status
print "Ip : "+ip
print "Country : "+country
print "-"*44
again = raw_input("Retry? [y/n]: ")
if again == "y" or again == "Y":
	os.system("clear")
	os.system("python2 wi.py -u "+url)
	sys.exit()
elif again == "n" or again == "N":
	pass
save = raw_input("Save? [y/n]: ")
if save == "y" or save == "Y":
	f = open("ip.txt", "w")
	f.write('''====================
Ip : %s
Country : %s
====================\n'''%(ip,country))
	f.close()
elif save == "n" or save == "N":
	sys.exit()
##########