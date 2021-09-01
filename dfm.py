# -*- coding: utf-8 -*-

try:
	import os
	import sys
	import time
	import socket
	import requests
	from datetime import datetime
except ImportError:
	os.system("pip2 install requests")

def shell(data):
	os.system(data)
	
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

shell("clear")

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

# ====== Color ====== #
b = "\033[1;30;40m"
r = "\033[1;31;40m"
g = "\033[1;32;40m"
y = "\033[1;33;40m"
b = "\033[1;34;40m"
p = "\033[1;35;40m"
c = "\033[1;36;40m"
w = "\033[1;37;40m"

def black(strike):
	print(b + strike)
	
def red(strike):
	print(r + strike)
	
def green(strike):
	print(g + strike)

def yellow(strike):
	print(y + strike)
	
def blue(strike):
	print(b + strike)

def purple(strike):
	print(p + strike)
	
def cyan(strike):
	print(c + strike)
	
def white(strike):
	print(w + strike)

def show(strike):
	print(strike)

def space():
	print

cyan(banner)
show("[ Time > %d:%d ]"%(hour,minute))
show("[ Date > %d/%d/%d ]"%(day,month,year))
print "----------[ Buatan Anak Malaysia ]----------"
show("-"*44)
time.sleep(1)
show("[ 1 ] DDOS")
show("[ 2 ] Web IP")
show("[ 3 ] Deface")
show("[ x ] Exit")
show("-"*44)
space()
choose = raw_input("Choose : ")

##################
if choose == "1":
	os.system("python2 lib/dos.py")
elif choose == "2":
	os.system("python2 lib/web-ip.py")
elif choose == "3":
	print("Coming Soon")
elif choose == "X" or choose == "x":
	white("")
	os.system("clear")
	sys.exit(0)
##################