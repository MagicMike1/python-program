from time import sleep
from ax12 import Ax12
from threading import Lock
import json


class movement:
	
	servoMutex = Lock()
	
	run = False
	slope = False
	previous_command = 'none'
	current_command = 'forward'
	
	servo = Ax12()
	legs = [[1,2,3], [13,14,15], [7,8,9], [10, 11, 12], [4, 5, 6], [16, 17, 18]]
	speeds = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
	voltage = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
	temperature = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
	position = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
	positions = [[servo.readPosition(1), servo.readPosition(2), servo.readPosition(3)], [servo.readPosition(13), servo.readPosition(14), servo.readPosition(15)], [servo.readPosition(7), servo.readPosition(8), servo.readPosition(9)], [servo.readPosition(10), servo.readPosition(11), servo.readPosition(12)], [servo.readPosition(4), servo.readPosition(5), servo.readPosition(6)], [servo.readPosition(16), servo.readPosition(17), servo.readPosition(18)]]
	
	
	def __init__(self):
		#Checks if readPosition didnt throw errors, if it did, it changes it's value to 512
		for x in range(0, 6):
			for y in range(0, 3):
				try:
					temp = int(self.positions[x][y])
				except:
					self.positions[x][y] = 512
					
	def readServoData(self):
		for x in range (0,6):
			for y in range (0,3):
				calc = ((y+1) *3)- (2+(y*2)) + (3*x) #calculates index from 1 untill and including 18
				if(calc != 9 and calc != 17 ): #reading servo 9 and 17 is not possible. So we exclude those.						
					try:
						self.servoMutex.acquire(1)
						self.position[x][y] = self.servo.readPosition(calc) * 300 / 1024
					except:
						print 'value:', self.position[x][y]
					finally:
						self.servoMutex.release()
					try:
						self.servoMutex.acquire(1)
						self.voltage[x][y] = self.servo.readVoltage(calc)/10.0
					except:
						print 'value:', self.voltage[x][y]
					finally:
						self.servoMutex.release()
					try:
						self.servoMutex.acquire(1)
						self.temperature[x][y] = int(self.servo.readTemperature(calc))
					except:
						print 'value:', self.temperature[x][y]
					finally:
						self.servoMutex.release()

				else:
					a,b = 2,2
					for z in range(0,2):
						self.position[a][b] = 0
						self.voltage[a][b] = 0
						self.temperature[a][b] = 0
						a + 3, b - 1
            
	def sendData(self):
		jsonString = {"heisenberg":{
		"battery": 76,
		"status": "OndersteBoven",
		"helling": 54,
		"servos": [
			{"id": 1, "power": self.voltage[0][0], "temp": self.temperature[0][0], "pos": self.position[0][0], "speed": self.speeds[0][0], "error": "no error" },
			{"id": 2, "power": self.voltage[0][1], "temp": self.temperature[0][1], "pos": self.position[0][1], "speed": self.speeds[0][1], "error": "no error" },
			{"id": 3, "power": self.voltage[0][2], "temp": self.temperature[0][2], "pos": self.position[0][2], "speed": self.speeds[0][2], "error": "no error" },
			{"id": 4, "power": self.voltage[1][0], "temp": self.temperature[1][0], "pos": self.position[1][0], "speed": self.speeds[1][0], "error": "no error" },
			{"id": 5, "power": self.voltage[1][1], "temp": self.temperature[1][1], "pos": self.position[1][1], "speed": self.speeds[1][1], "error": "no error" },
			{"id": 6, "power": self.voltage[1][2], "temp": self.temperature[1][2], "pos": self.position[1][2], "speed": self.speeds[1][2], "error": "no error" },
			{"id": 7, "power": self.voltage[2][0], "temp": self.temperature[2][0], "pos": self.position[2][0], "speed": self.speeds[2][0], "error": "no error" },
			{"id": 8, "power": self.voltage[2][1], "temp": self.temperature[2][1], "pos": self.position[2][1], "speed": self.speeds[2][1], "error": "no error" },
			{"id": 9, "power": self.voltage[2][2], "temp": self.temperature[2][2], "pos": self.position[2][2], "speed": self.speeds[2][2], "error": "no error" },
			{"id": 10, "power": self.voltage[3][0], "temp": self.temperature[3][0], "pos": self.position[3][0], "speed": self.speeds[3][0], "error": "no error" },
			{"id": 11, "power": self.voltage[3][1], "temp": self.temperature[3][1], "pos": self.position[3][1], "speed": self.speeds[3][1], "error": "no error" },
			{"id": 12, "power": self.voltage[3][2], "temp": self.temperature[3][2], "pos": self.position[3][2], "speed": self.speeds[3][2], "error": "no error" },
			{"id": 13, "power": self.voltage[4][0], "temp": self.temperature[4][0], "pos": self.position[4][0], "speed": self.speeds[4][0], "error": "no error" },
			{"id": 14, "power": self.voltage[4][1], "temp": self.temperature[4][1], "pos": self.position[4][1], "speed": self.speeds[4][1], "error": "no error" },
			{"id": 15, "power": self.voltage[4][2], "temp": self.temperature[4][2], "pos": self.position[4][2], "speed": self.speeds[4][2], "error": "no error" },
			{"id": 16, "power": self.voltage[5][0], "temp": self.temperature[5][0], "pos": self.position[5][0], "speed": self.speeds[5][0], "error": "no error" },
			{"id": 17, "power": self.voltage[5][1], "temp": self.temperature[5][1], "pos": self.position[5][1], "speed": self.speeds[5][1], "error": "no error" },
			{"id": 18, "power": self.voltage[5][2], "temp": self.temperature[5][2], "pos": self.position[5][2], "speed": self.speeds[5][2], "error": "no error" },
		]
		}}

		return json.dumps(jsonString)
			
		
	def action(self):
		self.servoMutex.acquire()
		self.servo.action()
		self.servoMutex.release()
		
	#Moves a given leg to a position in a certain amount of "time"
	def moveLeg(self, leg, pos1, pos2, pos3, time):
		dist = [abs(self.positions[leg][0] - pos1), abs(self.positions[leg][1] - pos2), abs(self.positions[leg][2] - pos3)]
		speed1 = int(dist[0] / time)
		speed2 = int(dist[1] / time)
		speed3 = int(dist[2] / time)
		if(speed1 == 0):
			speed1 = 1
		if(speed2 == 0):
			speed2 = 1
		if(speed3 == 0):
			speed3 = 1

		arrPos = int(self.legs[leg][0] / 3)
		self.speeds[arrPos][0] = speed1
		self.speeds[arrPos][1] = speed2
		self.speeds[arrPos][2] = speed3

		self.servoMutex.acquire(1)
		self.servo.moveSpeedRW(self.legs[leg][0], pos1, speed1)
		self.servo.moveSpeedRW(self.legs[leg][1], pos2, speed2)
		self.servo.moveSpeedRW(self.legs[leg][2], pos3, speed3)
		self.servoMutex.release()
		
		self.positions[leg][0] = pos1
		self.positions[leg][1] = pos2
		self.positions[leg][2] = pos3
		
	#Sets spider to idle
	def idle(self):
		if(self.previous_command != 'idle'):
			for x in range (0, 6):
				self.moveLeg(x, 512, 819, 810, 1)
				self.action()
				sleep(0.4)
			else:
				sleep(0.1)
	
	#Sets spider to stand
	def stand(self):
		if(self.previous_command != 'stand'):
			for x in range (0, 6):
				self.moveLeg(x, 512, 733, 674, 1)
				self.action()
				sleep(0.4)
			else:
				sleep(0.1)
	
	#Moves spider in a given direction (forward or backward)
	def walk(self, dir):
		print 'START WALKING'
		moves1 = [[418, 691, 604], [452, 720, 656], [505, 743, 700], [585, 751, 717], [675, 749, 713], [505, 800, 600]]
		moves2 = [[364, 728, 672], [425, 747, 708], [512, 752, 718], [598, 747, 708], [659, 728, 672], [512, 800, 600]]
		moves3 = [[348, 749, 713], [438, 751, 717], [518, 743, 700], [571, 720, 656], [605, 691, 604], [519, 800, 600]]

		leg1 = 5
		leg2 = 4
		leg3 = 3
		leg4 = 2
		leg5 = 1
		leg6 = 0
		
		#Sets spider to first step position
		self.moveLeg(0, moves1[leg1][0], moves1[leg1][1], moves1[leg1][2], 1)
		self.action()
		sleep(0.15)
		self.moveLeg(1, moves2[leg2][0], moves2[leg2][1], moves2[leg2][2], 1)
		self.action()
		sleep(0.15)
		self.moveLeg(2, moves3[leg3][0], moves3[leg3][1], moves3[leg3][2], 1)
		self.action()
		sleep(0.15)
		self.moveLeg(3, moves1[leg4][0], moves1[leg4][1], moves1[leg4][2], 1)
		self.action()
		sleep(0.15)
		self.moveLeg(4, moves2[leg5][0], moves2[leg5][1], moves2[leg5][2], 1)
		self.action()
		sleep(0.15)
		self.moveLeg(5, moves3[leg6][0], moves3[leg6][1], moves3[leg6][2], 1)
		self.action()
		sleep(0.15)
		
		if(dir == 'forward'):
			leg1 = 0
			leg2 = 5
			leg3 = 4
			leg4 = 3
			leg5 = 2
			leg6 = 1
		else:
			leg1 = 4
			leg2 = 3
			leg3 = 2
			leg4 = 1
			leg5 = 0
			leg6 = 5
		
		while self.current_command == 'forward' or self.current_command == 'backward':
			
			if(self.run == True):
				speed = 0.5
				delay = 0.15
			else:
				speed = 1
				delay = 0.4
			
			self.moveLeg(0, moves1[leg1][0], moves1[leg1][1], moves1[leg1][2], speed)
			self.moveLeg(1, moves2[leg2][0], moves2[leg2][1], moves2[leg2][2], speed)
			self.moveLeg(2, moves3[leg3][0], moves3[leg3][1], moves3[leg3][2], speed)
			self.moveLeg(3, moves1[leg4][0], moves1[leg4][1], moves1[leg4][2], speed)
			self.moveLeg(4, moves2[leg5][0], moves2[leg5][1], moves2[leg5][2], speed)
			self.moveLeg(5, moves3[leg6][0], moves3[leg6][1], moves3[leg6][2], speed)
			if(dir == 'forward'):
				leg1 += 1
				if(leg1 > 5):
					leg1 = 0
				leg2 += 1
				if(leg2 > 5):
					leg2 = 0
				leg3 += 1
				if(leg3 > 5):
					leg3 = 0
				leg4 += 1
				if(leg4 > 5):
					leg4 = 0
				leg5 += 1
				if(leg5 > 5):
					leg5 = 0
				leg6 += 1
				if(leg6 > 5):
					leg6 = 0
			else:
				leg1 -= 1
				if(leg1 < 0):
					leg1 = 5
				leg2 -= 1
				if(leg2 < 0):
					leg2 = 5
				leg3 -= 1
				if(leg3 < 0):
					leg3 = 5
				leg4 -= 1
				if(leg4 < 0):
					leg4 = 5
				leg5 -= 1
				if(leg5 < 0):
					leg5 = 5
				leg6 -= 1
				if(leg6 < 0):
					leg6 = 5
			self.action()
			sleep(delay)