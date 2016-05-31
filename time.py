#!/usr/bin/env python

from time import sleep
from ax12 import Ax12
import sys
import json

servo = Ax12()

legs = [[1,2,3], [13,14,15], [7,8,9], [10, 11, 12], [4, 5, 6], [16, 17, 18]]
positions = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

speeds = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
voltage = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
temperature = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
position = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

def getStartPositions():
    for x in range (0, 6):
        for y in range(0, 3):
            positions[x][y] = servo.readPosition(int(legs[x][y]))
    positions[2][2] = 512 #set servo 9 start pos to 512 since its not readable
    positions[5][1] = 512 #set servo 17 start pos to 512 since its not readable
    
def readServoData():
    for x in range (0,6):
        for y in range (0,3):
            calc = ((y+1) *3)- (2+(y*2)) + (3*x) #calculates index from 1 untill and including 18
            if(calc != 9 and calc != 17 ): #reading servo 9 and 17 is not possible. So we exclude those.
                try:
                    position[x][y] = servo.readPosition(calc) * 300 / 1024
                    voltage[x][y] = servo.readVoltage(calc)/10.0
                    temperature[x][y] = servo.readTemperature(calc)
                except Exception, detail:
                    print "inside exception"
                    print detail
                
            else:
                a,b = 2,2
                for z in range(0,2):
                    position[a][b] = 0
                    voltage[a][b] = 0
                    temperature[a][b] = 0
                    a + 3, b - 1
def readVolt():
    for x in range(0,6):
        for y in range(0,3):
            calc = ((y+1) *3)- (2+(y*2)) + (3*x) #calculates index from 1 untill and including 18
            if(calc != 9 and calc != 17 ): #reading servo 9 and 17 is not possible. So we exclude those.
                try:
                    voltage[x][y] = servo.readVoltage(calc)/10.0
                    print 'voltage: ',calc," ", voltage[x][y]
                except Exception, detail:
                    print "inside exception"
                    print detail
                
            else:
                a,b = 2,2
                for z in range(0,2):
                    voltage[a][b] = 0
                    a + 3, b - 1
            
def sendData():
    jsonString = {"heisenberg":{
    "battery": 76,
    "status": "OndersteBoven",
    "helling": 54,
    "servos": [
        {"id": 1, "power": voltage[0][0], "temp": temperature[0][0], "pos": position[0][0], "speed": speeds[0][0], "error": "no error" },
        {"id": 2, "power": voltage[0][1], "temp": temperature[0][1], "pos": position[0][1], "speed": speeds[0][1], "error": "no error" },
        {"id": 3, "power": voltage[0][2], "temp": temperature[0][2], "pos": position[0][2], "speed": speeds[0][2], "error": "no error" },
        {"id": 4, "power": voltage[1][0], "temp": temperature[1][0], "pos": position[1][0], "speed": speeds[1][0], "error": "no error" },
        {"id": 5, "power": voltage[1][1], "temp": temperature[1][1], "pos": position[1][1], "speed": speeds[1][1], "error": "no error" },
        {"id": 6, "power": voltage[1][2], "temp": temperature[1][2], "pos": position[1][2], "speed": speeds[1][2], "error": "no error" },
        {"id": 7, "power": voltage[2][0], "temp": temperature[2][0], "pos": position[2][0], "speed": speeds[2][0], "error": "no error" },
        {"id": 8, "power": voltage[2][1], "temp": temperature[2][1], "pos": position[2][1], "speed": speeds[2][1], "error": "no error" },
        {"id": 9, "power": voltage[2][2], "temp": temperature[2][2], "pos": position[2][2], "speed": speeds[2][2], "error": "no error" },
        {"id": 10, "power": voltage[3][0], "temp": temperature[3][0], "pos": position[3][0], "speed": speeds[3][0], "error": "no error" },
        {"id": 11, "power": voltage[3][1], "temp": temperature[3][1], "pos": position[3][1], "speed": speeds[3][1], "error": "no error" },
        {"id": 12, "power": voltage[3][2], "temp": temperature[3][2], "pos": position[3][2], "speed": speeds[3][2], "error": "no error" },
        {"id": 13, "power": voltage[4][0], "temp": temperature[4][0], "pos": position[4][0], "speed": speeds[4][0], "error": "no error" },
        {"id": 14, "power": voltage[4][1], "temp": temperature[4][1], "pos": position[4][1], "speed": speeds[4][1], "error": "no error" },
        {"id": 15, "power": voltage[4][2], "temp": temperature[4][2], "pos": position[4][2], "speed": speeds[4][2], "error": "no error" },
        {"id": 16, "power": voltage[5][0], "temp": temperature[5][0], "pos": position[5][0], "speed": speeds[5][0], "error": "no error" },
        {"id": 17, "power": voltage[5][1], "temp": temperature[5][1], "pos": position[5][1], "speed": speeds[5][1], "error": "no error" },
        {"id": 18, "power": voltage[5][2], "temp": temperature[5][2], "pos": position[5][2], "speed": speeds[5][2], "error": "no error" },
    ]
    }}
    
    print json.dumps(jsonString)


def move(leg, pos1, pos2, pos3, time):
    maxspeed = 531
    dist = [abs(positions[leg][0] - pos1), abs(positions[leg][1] - pos2), abs(positions[leg][2] - pos3)]
    speed1 = int(dist[0] / time)
    speed2 = int(dist[1] / time)
    speed3 = int(dist[2] / time)
    if(speed1 == 0):
        speed1 = 80
    if(speed2 == 0):
        speed2 = 80
    if(speed3 == 0):
        speed3 = 80

    firstServo = legs[leg][0]
    speeds[int(firstServo / 3)][0] = speed1
    speeds[int(firstServo / 3)][1] = speed2
    speeds[int(firstServo / 3)][2] = speed3

    servo.moveSpeedRW(legs[leg][0], pos1, speed1)
    servo.moveSpeedRW(legs[leg][1], pos2, speed2)
    servo.moveSpeedRW(legs[leg][2], pos3, speed3)

    positions[leg][0] = pos1
    positions[leg][1] = pos2
    positions[leg][2] = pos3

def idle():
    for x in range (0, 6):
        move(x, 512, 819, 810, 4)
        servo.action()
        sleep(0.75);

def stand():
    for x in range (0, 6):
        move(x, 512, 733, 674, 4)
        servo.action()
        sleep(0.5)

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
    speed = 1

    for x in range (0, 6):
        move(0, moves1[leg1][0], moves1[leg1][1], moves1[leg1][2], speed)
        move(1, moves2[leg2][0], moves2[leg2][1], moves2[leg2][2], speed)
        move(2, moves3[leg3][0], moves3[leg3][1], moves3[leg3][2], speed)
        move(3, moves1[leg4][0], moves1[leg4][1], moves1[leg4][2], speed)
        move(4, moves2[leg5][0], moves2[leg5][1], moves2[leg5][2], speed)
        move(5, moves3[leg6][0], moves3[leg6][1], moves3[leg6][2], speed)
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

        servo.action()
        sleep(0.6) #0.02 sleep for every 0.1 speed
#print positions
#getStartPositions()
#print positions
'''        
while True:
    readServoData()
    try:
        sendData()
    except:
        sleep(0)
    sleep(2)
'''

#read()
#isValid = True
#while True:
#if(isValid):
    #fill()
    #isValid = False

    #walk()
#read()
#print positions
#idle()
#stand()
#sleep(1)

#while True:
   # walk()
#move(1, 512, 512, 512, 0.5)
#servo.action()


#while True:

#test = servo.readTemperature(1)
#print test

#move(2, 478, 749, 712, 1)
#move(4, 663, 726, 667, 1)
#servo.action()
while True:
        walk()
