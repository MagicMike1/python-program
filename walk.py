#!/usr/bin/env python

from time import sleep
from ax12 import Ax12
import sys

speed = 2
servo = Ax12()

legs = [[1,2,3], [13,14,15], [7,8,9], [10, 11, 12], [4, 5, 6], [16, 17, 18]]
positions = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

speeds = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
voltage = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
temperature = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
position = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

def move(leg, pos1, pos2, pos3, time):
	dist = [abs(positions[leg][0] - pos1), abs(positions[leg][1] - pos2), abs(positions[leg][2] - pos3)]
	speed1 = int(dist[0] / time)
	speed2 = int(dist[1] / time)
	speed3 = int(dist[2] / time)
	if(speed1 == 0):
		speed1 = 1
	if(speed2 == 0):
		speed2 = 1
	if(speed3 == 0):
		speed3 = 1

	arrPos = int(legs[leg][0] / 3)
	speeds[arrPos][0] = speed1
	speeds[arrPos][1] = speed2
	speeds[arrPos][2] = speed3
	positions[leg][0] = pos1
	positions[leg][1] = pos2
	positions[leg][2] = pos3

	servo.moveSpeedRW(legs[leg][0], pos1, speed1)
	servo.moveSpeedRW(legs[leg][1], pos2, speed2)
	servo.moveSpeedRW(legs[leg][2], pos3, speed3)

def idle():
	for x in range (0, 6):
		move(x, 512, 819, 810, 100)
		sleep(1);
		servo.action()

def stand():
	for x in range (0, 6):
		move(x, 512, 733, 674, 200)
		sleep(0.2)
		servo.action()

def walk():
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
	move(0, moves1[leg1][0], moves1[leg1][1], moves1[leg1][2], 0.5)
	servo.action()
	sleep(0.1)
	move(1, moves2[leg2][0], moves2[leg2][1], moves2[leg2][2], 0.5)
	servo.action()
	sleep(0.1)
	move(2, moves3[leg3][0], moves3[leg3][1], moves3[leg3][2], 0.5)
	servo.action()
	sleep(0.1)
	move(3, moves1[leg4][0], moves1[leg4][1], moves1[leg4][2], 0.5)
	servo.action()
	sleep(0.1)
	move(4, moves2[leg5][0], moves2[leg5][1], moves2[leg5][2], 0.5)
	servo.action()
	sleep(0.1)
	move(5, moves3[leg6][0], moves3[leg6][1], moves3[leg6][2], 0.5)
	servo.action()
	sleep(0.15)


	speed = 1
	delay = 1
	while True:
		move(0, moves1[leg1][0], moves1[leg1][1], moves1[leg1][2], speed)
		move(1, moves2[leg2][0], moves2[leg2][1], moves2[leg2][2], speed)
		#move(2, moves3[leg3][0], moves3[leg3][1], moves3[leg3][2], speed)
		#move(3, moves1[leg4][0], moves1[leg4][1], moves1[leg4][2], speed)
		#move(4, moves2[leg5][0], moves2[leg5][1], moves2[leg5][2], speed)
		#move(5, moves3[leg6][0], moves3[leg6][1], moves3[leg6][2], speed)
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

		servo.action()
		sleep(delay)
                
walk()
