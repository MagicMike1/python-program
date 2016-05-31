#!/usr/bin/env python

from time import sleep
from ax12 import Ax12
import sys

#speed = 2
servo = Ax12()

legs = [[1,2,3], [13,14,15], [7,8,9], [10, 11, 12], [4, 5, 6], [16, 17, 18]]
positions = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

def move(leg, pos1, pos2, pos3, time):
    #maxspeed = 531
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

    servo.moveSpeedRW(legs[leg][0], pos1, speed1)
    servo.moveSpeedRW(legs[leg][1], pos2, speed2)
    servo.moveSpeedRW(legs[leg][2], pos3, speed3)

    positions[leg][0] = pos1
    positions[leg][1] = pos2
    positions[leg][2] = pos3

def idle():
    for x in range (0, 6):
        move(x, 512, 819, 810, 10)
        servo.action()
        sleep(0.75);

def stand():
    for x in range (0, 6):
        move(x, 512, 733, 674, 10)
        servo.action()
        sleep(0.5)

def crawl():
    moves1 = [[614, 769, 769], [614, 761, 738], [614, 744, 702], [614, 724, 664], [614, 703, 625], [614, 800, 702]]
    moves2 = [[512, 703, 625], [512, 724, 664], [512, 744, 702], [512, 761, 738], [512, 769, 769], [512, 800, 702]]
    moves3 = [[410, 769, 769], [410, 761, 738], [410, 744, 702], [410, 724, 664], [410, 703, 625], [410, 800, 702]]
    moves4 = [[614, 703, 625], [614, 724, 664], [614, 744, 702], [614, 761, 738], [614, 769, 769], [614, 800, 702]]
    moves5 = [[512, 769, 769], [512, 761, 738], [512, 744, 702], [512, 724, 664], [512, 703, 625], [512, 800, 702]]
    moves6 = [[410, 703, 625], [410, 724, 664], [410, 744, 702], [410, 761, 738], [410, 769, 769], [410, 800, 702]]
  
    
    leg1 = 5
    leg2 = 4
    leg3 = 3
    leg4 = 2
    leg5 = 1
    leg6 = 0
    speed = 0.5
    
    for x in range (0, 6):
        move(0, moves1[leg1][0], moves1[leg1][1], moves1[leg1][2], speed)
        move(1, moves2[leg2][0], moves2[leg2][1], moves2[leg2][2], speed)
        move(2, moves3[leg3][0], moves3[leg3][1], moves3[leg3][2], speed)
        move(3, moves4[leg4][0], moves4[leg4][1], moves4[leg4][2], speed)
        move(4, moves5[leg5][0], moves5[leg5][1], moves5[leg5][2], speed)
        move(5, moves6[leg6][0], moves6[leg6][1], moves6[leg6][2], speed)
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
        sleep(0.28) #0.02 sleep for every 0.1 speed

#idle()
#sleep(1)

while True:
    crawl()
#move(1, 512, 512, 512, 0.5)
#servo.action()
#servo.ping(13)
#test = servo.readTemperature(13)
#print test



#move(2, 478, 749, 712, 1)
#move(4, 663, 726, 667, 1)
#servo.action()

