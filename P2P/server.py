import socket 
import pickle
from thread import *
import threading 
def clie(socket,active):
	st=pickle.dumps(active)
	socket.sendall(st)

def user(client,self_ip):

  while (True):
  	command=client.recv(1024)
	d='d'
	q='q'
	if(command.decode()==d):
		ip=client.recv(4096)
		ip=ip.decode()
		file=client.recv(4096)
		file=file.decode()
		client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		client_socket.connect((ip,6002))
			#f={'ip':client[0],'file':l[0][3]}
		client_socket.sendall(file.encode())
		
		client_socket.sendall(self_ip)

	elif (command.decode()==q):
		client.close()
		break

		

host=''
port=5559
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)
active=[]
ad=[]
while (True):
	client,addr=s.accept()
	active.append(client)
	ad.append(addr)
	for cl in active:
		start_new_thread(clie,(cl,ad))
		
	t1=threading.Thread(target=user,args=(client,addr[0]))
	t1.start()
	

s.close()


