import threading
import socket
import sys
import json
from time import sleep

from movement import movement

mutex = threading.Lock()
move = movement()

connected = False
while connected == False: #Keeps trying to establish a connection
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create socket

		server_adress = ('localhost', 13371)
		print >>sys.stderr, 'connecting to %s port %s' %server_adress
		sock.connect(server_adress) #connect socket
		sock.send("LEGMODE") #handshake
		if(sock.recv(1024) == 'spiderlegs connected'):
			connected = True
			print 'Connection established'
	except:
		print >>sys.stderr, 'Error: unable to start socket\nTrying again in 5 seconds\n'
		sleep(5)
	"""		finally:
			print >>sys.stderr, 'closing socket'
			sock.close()"""
			


#This function sends data to c++
def writeData():
	while True:
		move.readServoData()
		sock.send(move.sendData())
		sleep(1)	

#This function creates a socket that listens to commands from the c++ server	
def connection():			
	while True:
		data = sock.recv(1024)
		if(data != move.current_command):
			if(data == 'run enabled'):
				move.run = True
			elif(data == 'run disabled'):
				move.run = False
			elif(data == 'slope enabled'):
				move.slope = True
			elif(data == 'slope disabled'):
				move.slope = False
			else:
				mutex.acquire(1)
				move.previous_command = move.current_command
				move.current_command = data
				mutex.release()
		print >>sys.stderr, 'received: "%s"' % data			
	

#Create a thread to manage socket
try:
	t = threading.Thread(target=connection)
	t.start()
	sleep(0.01)
except:
	print 'Error: unable to start reading thread'

'''
#Create a thread to send data to c++ server
try:
	t = threading.Thread(target=writeData)
	t.start()
	sleep(0.01)
except:
	print 'Error: unable to start writing thread'
'''
	
while True:
	if(move.current_command == 'forward'):
		move.walk('forward')
	elif(move.current_command == 'backward'):
		move.walk('backward')
	elif(move.current_command == 'idle'):
		move.idle()
	elif(move.current_command == 'stand'):
		move.stand()
		
	sleep(0.1)
		
		
		
		