import tkinter
from tkinter import BOTH, END, LEFT
import ftplib
import threading 
import datetime 
#import ImageTk, Image

ftp = ftplib.FTP() #creating a ftp object 
current_path=""
  
def connectServer(): 
    ip = ent_ip.get() 
    port = int(ent_port.get())
    try: 
        msg = ftp.connect(ip,port)
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,msg)
        username.place(x=150,y=20)
        e_username.place(x=150,y=40)
        password.place(x=150,y=60)
        e_password.place(x=150,y=80)
        login.place(x=182,y=110)
    except: 
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"connection failed")

def loginServer():
    user = e_username.get()
    pas=e_password.get()
    msg = ftp.login(user,pas)
    text_servermsg.insert(END,"\n")
    text_servermsg.insert(END,msg)
    displayDir()
    username.place_forget()
    e_username.place_forget()
    password.place_forget()
    e_password.place_forget()
    login.place_forget()
   
        
        
def displayDir():
    listitems.delete(0,END)
    listitems.insert(0," ") 
    dirlist = []
    dirlist = ftp.nlst() #for getting the list of items in current directory of the ftp server 
    for item in dirlist:
        listitems.insert(0, item)


#Commands
def changeDirectory(current_path,ref):
    directory = ent_input.get()
    
    try:
        msg = ftp.cwd(directory)
        current_path=ftp.pwd() #getting the current directory of the server 
        ref.configure(text=current_path)
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,msg)
    except:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Unable to change directory")
    displayDir()

def createDirectory():
    directory = ent_input.get()
    try:
        msg = ftp.mkd(directory)
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,msg)
    except:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Unable to create directory")
    displayDir()
    
def deleteDirectory():
    directory = ent_input.get()
    try:
        msg = ftp.rmd(directory)
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,msg)
    except:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Unable to delete directory")
    displayDir()
    
def down_thread():

    t1=threading.Thread(target=downloadFile,args=())
    t1.start()

def downloadFile():
    ip = ent_ip.get() 
    port = int(ent_port.get())
    ft=ftplib.FTP()
    msg = ft.connect(ip,port)
    file = ent_input.get()
    user = e_username.get()
    pas=e_password.get()
    msg =ft.login(user,pas)
    ft.cwd(ftp.pwd())
    down = open(file, "wb")
    try:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Downloading " + file + "...")
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,ft.retrbinary("RETR " + file, down.write))
    except:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Unable to download file")
    ft.quit()
    
def uploadFile():
    file = ent_input.get()
    try:
        up = open(file, "rb")
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Uploading " + file + "...")
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,ftp.storbinary("STOR " + file,up))
    except:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Unable to upload file")
    displayDir()
    
def closeconn():    
    
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Closing connection...")
        ftp.quit()
        text_servermsg.insert(END,"Connection closed at "+str(datetime.datetime.now().time()))
    
def OnDouble(event):
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        ent_input.delete(0,END)
        ent_input.insert(0,value)

    

window = tkinter.Tk()
window.title("FTP Client")
window.geometry("1000x600")
window.configure(bg="black")

#adding image 
path="ftp.png"
img = tkinter.PhotoImage(file=path)
panel=tkinter.Label(window,image=img)
panel.configure(highlightbackground="white")
panel.place(x=270,y=10)

#label for current path
curr=tkinter.Label(window,text=current_path)
curr.place(x=800,y=20)
    

lbl_ip = tkinter.Label(window, text="IP Address")

ent_ip = tkinter.Entry(window) #entering the ip of the server to connect 

lbl_port = tkinter.Label(window, text="Port") 
ent_port = tkinter.Entry(window) #port on which the server is listening for requests 

btn_connect = tkinter.Button(window, text="Connect", command=connectServer)


#Server response text box
text_servermsg = tkinter.Text(window)


username = tkinter.Label(window, text="Username")
e_username = tkinter.Entry(window)
password = tkinter.Label(window, text="Password")
e_password = tkinter.Entry(window)
login = tkinter.Button(window, text="Login", command=loginServer)

#Directory listing
lbl_dir = tkinter.Label(window, text="Directory listing:")
listitems = tkinter.Listbox(window,width=40,height=14)
listitems.bind("<Double-Button-1>",OnDouble)
#for commands on the ftp server 

lbl_input = tkinter.Label(window, text="Input")
ent_input = tkinter.Entry(window)

btn_chdir = tkinter.Button(window, text="Change Directory",bg="grey", command=lambda: changeDirectory(current_path,curr),width=15)
btn_crdir = tkinter.Button(window, text="Create Directory",bg="grey", command=createDirectory,width=15)
btn_deldir = tkinter.Button(window, text="Delete Directory", bg="grey",command=deleteDirectory,width=15)
btn_downfile = tkinter.Button(window, text="Download File",bg="grey" ,command=down_thread,width=15)
btn_upfile = tkinter.Button(window, text="Upload File",bg="grey", command=uploadFile,width=15)

quit = tkinter.Button(window, text="Disconnect",bg="grey", command=closeconn,width=15)

#Place widgits
lbl_ip.place(x=20,y=20)
ent_ip.place(x=20,y=40)
lbl_port.place(x=20,y=60)
ent_port.place(x=20,y=80)
btn_connect.place(x=52,y=110)
text_servermsg.place(x=20,y=150)
 


lbl_dir.place(x=700,y=143)
listitems.place(x=700,y=165)

lbl_input.place(x=700,y=400)
ent_input.place(x=700,y=420)
btn_chdir.place(x=700,y=450)
btn_crdir.place(x=700,y=480)
btn_deldir.place(x=700,y=510)

btn_downfile.place(x=850,y=450)
btn_upfile.place(x=850,y=480)

quit.place(x=850,y=510)


#Create
window.mainloop()
