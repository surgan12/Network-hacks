from tkinter import *
import urllib.request ,json
import logic

top=Tk()
frame=Frame(top,width=400,height=400,background="blue")
frame.pack(fill="both")
entry=Entry(frame)
entry.pack()
entry2=Entry(frame)
entry2.pack()
button2=Button(frame,text='go',command=lambda : logic.back(entry.get(),entry2))


button2.pack()


top.mainloop()
