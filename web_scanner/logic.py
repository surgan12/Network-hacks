import socket
import os

def ip(url,label):
    return label.config(text=socket.gethostbyname(url)+'\n')

def whois(url,label):
	st='whois '+ url
	proc=os.popen(st)

	label.config(text=proc.read())

def nmap(url,label):
	st='nmap '+url
	proc=os.popen(st)
	label.config(text=proc.read())
