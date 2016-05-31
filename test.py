#!/usr/bin/env python

from time import sleep
from ax12 import Ax12
import sys

speed = 2
servo = Ax12()

legs = [[1,2,3], [13,14,15], [7,8,9], [10, 11, 12], [4, 5, 6], [16, 17, 18]]
positions = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

def move(leg, pos1, pos2, pos3, speed):
        dist = [abs(positions[leg][0] - pos1), abs(positions[leg][1] - pos2), abs(positions[leg][2] - pos3)]
        if(dist[0] >= dist[1] and dist[0] >= dist[2]):
                time = dist[0] / speed
                if(time < 1):
                        time = 1
                speed1 = speed
                speed2 = dist[1] / time
                speed3 = dist[2] / time
        elif(dist[1] >= dist[0] and dist[1] >= dist[2]):
                time = dist[1] / speed
                if(time < 1):
                        time = 1
                speed1 = dist[0] / time
                speed2 = speed
                speed3 = dist[2] / time
        else:
                time = dist[2] / speed
                if(time < 1):
                        time = 1
                speed1 = dist[0] / time
                speed2 = dist[1] / time
                speed3 = speed
        if(speed1 == 0):
                speed1 = 1
        if(speed2 == 0):
                speed2 = 1
        if(speed3 == 0):
                speed3

        servo.moveSpeedRW(legs[leg][0], pos1, speed1)
        servo.moveSpeedRW(legs[leg][1], pos2, speed3)
        servo.moveSpeedRW(legs[leg][2], pos3, speed3)

def idle():
        for x in range (0, 6):
            move(x, 512, 819, 810, 100)
            sleep(1);
            servo.action()

def stand():
        for x in range (0, 6):
            move(x, 512, 743, 658, 200)
            sleep(0.2)
            servo.action()

def walk():
        moves = [[561, 726, 667], [499, 746, 707], [410, 752, 718], [320, 746, 707], [258, 726, 667], [410, 819, 650]]
        leg1 = 5
        leg2 = 4
        leg3 = 3
        leg4 = 2
        leg5 = 1
        leg6 = 0
        speed = 75

        for x in range (0, 6):
                #move(0, moves[leg1][0], moves[leg1][1], moves[leg1][2], speed)
                #move(1, moves[leg2][0], moves[leg2][1], moves[leg2][2], speed)
                move(2, moves[leg3][0], moves[leg3][1], moves[leg3][2], speed)
                #move(3, moves[leg4][0], moves[leg4][1], moves[leg4][2], speed)
                #move(4, moves[leg5][0], moves[leg5][1], moves[leg5][2], speed)
                move(5, moves[leg6][0], moves[leg6][1], moves[leg6][2], speed)
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
                sleep(1)

print servo.readTemperature(8)
