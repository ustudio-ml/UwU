# -*- coding: utf-8 -*-

try:
	import os
	import sys
	import random
	import socket
	import time
	import optparse
	from datetime import datetime
except ImportError:
	print "Error la bang/sis"
	
now = datetime.now()
hour = now.minute
minute = now.minute
day = now.day
month = now.month
year = now.year

banner = '''
             .---.        .-----------

            /     \  __  /    ------

           / /     \(  )/    -----

          //////   ' \/ `   ---

         //// / // :    : ---

        // /   /  /`    '--

       //          //..\\

              ====UU====UU====
     ---------------------------------
     | [ Author ] : xMsUwUsMx        |
     | [ Forum  ] : dragonforce.io   |
     ---------------------------------
'''

def usage():
	os.system("clear")
	print '''
	
usage: python2 attack.py [-i] [-p]
-i, --ip : Ip Website
-p, --port : Port

[ Credit ] @waitercinta
	'''

os.system("clear")
print banner
print "[ Time > %d:%d ]"%(hour,minute)
print "[ Date > %d/%d/%d ]"%(day,month,year)
print "----------[ Buatan Anak Malaysia ]----------"
print "-"*44
print "[ 1 ] Help"
print "[ 2 ] Back To Home"
print "[ x ] Exit"
print "-"*44
print
choose = raw_input("Choose : ")

##########
if choose == "1":
	usage()
elif choose == "2":
	os.system("python2 dfm.py")
elif choose == "x" or choose == "X":
	sys.exit()
##########