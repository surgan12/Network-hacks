from tkinter import *
import logic
import threading 
import os

def run(st):
	output.insert(END,os.popen(st).read())

def run_thread(st):
	output.delete('1.0',END)
	threading.Thread(target=run,args=(st,)).start()

def start_thread(st):
	if st=="ip":
		t1=threading.Thread(target=logic.ip,args=(output,))
		t1.start()
	elif st=="whois":
		t1=threading.Thread(target=logic.whois,args=(output,))
		t1.start()
	elif st=="nmap":
		t1=threading.Thread(target=logic.nmap,args=(output,))
		t1.start()


DATA=["ip","nmap","whois"]
top=Tk()
top.geometry("600x600")

ent=Entry(top)
ent.place(x=100,y=50)
w=Menu(top,bg="black",fg='white')
top.config(menu=w)
output=Text(top)
output.configure(font="italics")
output.place(x=0,y=80)
w.add_command(label="ip",command= lambda: start_thread("ip"))
w.add_separator()
w.add_command(label="whois",command= lambda: start_thread("whois"))
w.add_separator()
w.add_command(label="nmap",command= lambda: start_thread("nmap"))
w.add_separator()
go=Button(top,text="go",command=lambda: run_thread(ent.get()))	
go.place(x=260,y=50)
top.mainloop()


	
