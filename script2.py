import robot
import requests as req
import time
import i2c2
def say(data):
    print("saying")
    url = 'http://0.0.0.0:6000/index?source='+data
    resp = req.get(url)
 
robot.eyesforward()
time.sleep(2) 
robot.eyesup()
time.sleep(0.5)

say("hello beezo and solly")
time.sleep(0.2)
say("have a good day")
robot.cutebrows()
say("bye beezo, bye solly")
# time.sleep(1)
robot.wave()