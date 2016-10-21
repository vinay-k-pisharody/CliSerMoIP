from time import sleep
import thread
import threading
import socket
import os

flag=1;

class ReceiverThread(threading.Thread):

	def __init__(self,c,addr):
		threading.Thread.__init__(self)
		self.c=c
		self.addr=addr

	def run(self):
		msg="initial"
   		while (len(msg)>0) and (flag):
   			try:
				msg=self.c.recv(1024)
				if(len(msg)==1):
					if(ord(msg)==3):
						msg=""
					else:
						print self.addr," says : "+msg
				else:
					print self.addr," says : "+msg
			except Exception:
				break
		self.c.close()
	   	print 'Terminated connection from', self.addr
	   	os._exit(1)

class ServerThread(threading.Thread):
	
	def __init__(self):
		threading.Thread.__init__(self)
	
	def getip(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(('1.1.1.1', 0))
		return s.getsockname()[0]

	def run(self):
		s = socket.socket()
		host = self.getip()
		port = 3400
		s.bind((host, port))
		print "Host : " + host + ":" +str(port)
		
		s.listen(0)
		c, addr = s.accept()
		print "New Server Thread Created"
		print 'Got connection from', addr
		t1=ReceiverThread(c,addr)
	   	t1.start()

class ClientThread(threading.Thread):

	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		s = socket.socket()
		"""
		Replace the address of the host with the host of the Server the Client is connecting to.
		"""
		host="192.168.2.116"
		port=3400
		s.connect((host,port))
		while flag:
			try:
				msg=raw_input()
				if(len(msg)>0):
					s.send(msg)
			except EOFError:
				if(flag):
					continue
				else:
					print "Exception Hit"
		s.close()
		os._exit(1)

print "Press CTRL+C to terminate the application"
server=ServerThread()
server.start()

sleep(5)

client=ClientThread()
print "Client Initialised"
client.start()

try :
	while flag:
		continue
except KeyboardInterrupt:
	flag=0
	os._exit(1)