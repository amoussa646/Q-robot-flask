from adafruit_servokit import ServoKit
import time
import sys
from main import say
import requests as req
kit = ServoKit(channels=16)
browsl=kit.servo[15]
browsr=kit.servo[14]
neckh=kit.servo[13]
neckv=kit.servo[9]
cutel=kit.servo[11]
cuter=kit.servo[10]
link1=kit.servo[7]
link2=kit.servo[5]
wrist1=kit.servo[3]
wrist2=kit.servo[1]
gripper=kit.servo[0]

def armhome():  
    link2.angle=120
    time.sleep(1)
    link1.angle=180
    time.sleep(1)
    wrist1.angle=90
    time.sleep(1)
    wrist2.angle=0
    time.sleep(1)
    gripper.angle=0
    time.sleep(1)
def wave():
    
    wrist2.angle=180
    time.sleep(0.5)
    wrist1.angle=90
    time.sleep(0.5)
    wrist1.angle=180
    time.sleep(0.5)
    wrist1.angle=0
    time.sleep(0.5)
    wrist1.angle=90
    
def armtest():
    link2.angle=120
    time.sleep(1)
    

def armtest2():
    link2.angle=135
    time.sleep(1)
    link1.angle=90
    time.sleep(1)
    link2.angle=30
    time.sleep(1)
    wrist2.angle=180
    time.sleep(1)
    wrist1.angle=50
    
def armsing():
    link2.angle=135
    time.sleep(1)
    link1.angle=90
    time.sleep(1)
    link2.angle=30
    time.sleep(1)
    wrist2.angle=180
    time.sleep(1)
    wrist1.angle=50
    
def armpick():
    wrist2.angle=155
    time.sleep(1)
    link2.angle=120
    time.sleep(1)
    link1.angle=15
    time.sleep(1)
    
    link2.angle=0
    time.sleep(1)
    wrist1.angle=90
    time.sleep(1)
    link1.angle=0
    
    gripper.angle=0


def gripperopen():
    gripper.angle=100

def gripperclose():
    gripper.angle=20

def cute():
    cutel.angle=85
    cuter.angle=95
    time.sleep(0.4)

def uncute():
    cutel.angle=135
    cuter.angle=45
    time.sleep(0.4)

def browsdown():
    browsr.angle = 10
    browsl.angle = 170
    time.sleep(0.4)
    
def browsup():
    browsr.angle = 90
    browsl.angle = 100
    time.sleep(0.4)
    
def browstest():
    browsup()
    time.sleep(0.4)
    browsdown()
    time.sleep(0.4)
    
def eyesforward():
    neckh.angle=90
    time.sleep(0.4)
    neckv.angle=180
    time.sleep(0.4)
    

def eyesleft():
    neckh.angle=180
    time.sleep(0.4)
    
def eyesright():
    neckh.angle=0
    time.sleep(0.4)
def eyesup():
    neckv.angle=20
def eyesdown():
    neckv.angle=180
def cutetest():
    cute()
    time.sleep(0.4)
    uncute()
    time.sleep(0.4)
    cute()
    time.sleep(0.4)
def cutebrows():
    cute()
    time.sleep(0.4)
    uncute()
    time.sleep(0.4)
    browstest()
    time.sleep(0.4)
    cute()
    time.sleep(0.4)
def eyesn():
    eyesforward()
    time.sleep(0.4)
    cute()
    time.sleep(0.4)
    browsdown()
    time.sleep(0.4)
def eyestest():
    cutebrows()
    time.sleep(0.4)
    eyesleft()
    time.sleep(0.4)
    eyesforward()
    time.sleep(0.4)
    eyesright()
    time.sleep(0.4)
    eyesforward()
    time.sleep(0.4)
    eyesup()
    time.sleep(0.4)
    eyesforward()
    time.sleep(0.4)
    eyesdown()
    time.sleep(0.4)
    eyesforward()
    time.sleep(0.4)
    

