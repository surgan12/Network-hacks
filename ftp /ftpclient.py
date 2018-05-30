from ftplib import FTP

ftp=FTP('')
ftp.connect('localhost',1026)
ftp.login()
ftp.cwd('/Desktop')
ftp.retrlines('LIST')
filename=input()
localfile = open('/home/surgan/Downloads/'+filename, 'wb')
ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
ftp.quit()
localfile.close()