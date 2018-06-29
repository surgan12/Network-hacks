import socket
import os
import threading 
from tkinter import *
def ip(label):
	label.delete('1.0',END)

	label.insert(END,os.popen('ip -h').read()+'\n')

def whois(label):
	st='whois -h'
	proc=os.popen(st)
	label.delete('1.0',END)
	label.insert(END,proc.read())

def nmap(label):
	st='nmap -h'
	proc=os.popen(st)
	label.delete('1.0',END)
	label.insert(END,proc.read())
