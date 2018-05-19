from tkinter import *
import logic
DATA=["ip","nmap","whois"]
top=Tk()
frame=Frame(top,height=1800,width=1800,bg='white')
frame.pack()
lab2=Label()
ent=Entry(frame)
ent.pack()
w=Menu(top,bg="black",fg='white')
top.config(menu=w)
text=StringVar()
label=Label(frame,text="",bg='grey',fg='white')
label.pack()
w.add_command(label="ip",command= lambda: logic.ip(ent.get(),label))
w.add_separator()
w.add_command(label="whois",command= lambda: logic.whois(ent.get(),label))
w.add_separator()
w.add_command(label="nmap",command= lambda: logic.nmap(ent.get(),label))
w.add_separator()


top.mainloop()


	
