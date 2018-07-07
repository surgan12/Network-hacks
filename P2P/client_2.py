import socket 
import pickle
import os
from thread import *
import os.path
import threading 

incomingusers=[] #maintaining an array of incoming connection-threads
def client_to_server(sock,receive):
	
	while (True):
		command=input("enter the command")
		sock.sendall(command.encode())
		d='d'
		q='q' 
		if(command==d):
			ip=input("enter the ip")
			sock.sendall(ip.encode())
			file=input("name of the file")
			sock.sendall(file.encode())
			## accepting the connection for recieving the file 

			client,addr=receive.accept()
			w=client.recv(4096)
			path="Desktop/P2P"
			e=w.decode()
			completepath=os.path.join(path,e)
			file=open(completepath,'wb')
			l=client.recv(1024)
			while(l): 							#receiving the file 
				file.write(l)
				l=client.recv(1024)
			file.close()
			receive.close() 	
		
		elif (command==q):
			sock.close()
			break	 #closing the connection from server.	

def incoming_multiple_users(port_for_server_command):
	while (True):
		cli,addr=port_for_server_command.accept()
		t3=threading.Thread(target=help_receive,args=(cli))
		incomingusers.append(t3)
		t3.start()
def help_receive(cli):
 
	file_name=cli.recv(4096)
	file_name=file_name.decode()
	ip=cli.recv(4096)
	ip=ip.decode()
	data_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	data_sock.connect((ip,6001))

	filepath="Desktop/share"
	completepath=os.path.join(filepath,file_name)
	data_sock.send(file_name)
	file=open(completepath,'rb')
	l=file.read(1024)
	while (l):
		data_sock.sendall(l)
		l=file.read()

	file.close()
	data_sock.close()

'''def recieve_thread(sock):
 # while(True):
  	client,addr=sock.accept()
  	t1=threading.Thread(target=h)		
'''


server_host='127.0.0.1'
server_port=6003
port_2=6004
self_host='127.0.0.1' 
data_port=6005
port_for_server_command=6006

receive=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #fixed port to recieve data on 
receive.bind((server_host,data_port))
receive.listen(5) 	

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)	 #connecting to server
sock.connect((self_host,server_port))  						

socket_for_server_command=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #socket for sending files 
socket_for_server_command.bind((self_host,port_for_server_command))
socket_for_server_command.listen(5)

data=pickle.loads(sock.recv(4096))								 
print(data)	 


t1=threading.Thread(target=client_to_server,args=(sock,receive,)) #thread for sending request to server and recieving files
t1.start()
incoming_multiple_users(socket_for_server_command)
#waiting for the threads to join 
t1.join()
for thread in incomingusers:
	thread.join() 					#waiting for all user connections to end 
