self implemented P2P file sharing protocol (quite different from those available online) using python.

goals of this project:

1.Learning proper implementation and working of sockets.
2.Used multithreading.
3.Working with network buffers.
4.Handling requests from multiple users and responding them using different threads.
---------
Tested on Localhost by taking different sockets as clients.
---------
To use first run server.py .
In this, protocol i have used three sockets per user i.e one for server, second for recieving data from any user , third for sending files.
Since a user should be able to simultaneously send or recieve files to any user on the internet , i used 2 separate sockets (I know there would be better solutions but i am new to network programming ,so as a starti decided to use this)
From the code you can see the bound ports in case of all

In case of running on terminal, you can make two/more separate client.py and change the ports accordingly as each set of three ports would act as one client.


Working on a better solution of it using better framework.
