import robot
import requests as req
import time

def say(data):
    print("saying")
    url = 'http://0.0.0.0:6000/index?source='+data
    resp = req.get(url)
 
robot.eyesforward()
time.sleep(2) 
robot.eyesup()
time.sleep(0.5)

say("hello abdelaaziiz")
robot.wave()
time.sleep(0.2)
time.sleep(1)
say("it's your birthday")
time.sleep(0.2)
say("happy birthday abdelaaziiz")
robot.cutebrows()
say("enjoy it do the max")
time.sleep(0.3)
say("bye bye abdelaaziiz, take care")
# time.sleep(1)
robot.wave()