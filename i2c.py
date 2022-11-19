import os 
import time
def forward():
    os.system("python3 ~/Desktop/i2c.py 1")
    time.sleep(0.6)
    os.system("python3 ~/Desktop/i2c.py 5")
    
def stop():
    os.system("python3 ~/Desktop/i2c.py 1")
    
    
def back():
    os.system("python3 ~/Desktop/i2c.py 1")
    time.sleep(0.6)
    os.system("python3 ~/Desktop/i2c.py 2")
    
def left():
    os.system("python3 ~/Desktop/i2c.py 1")
    time.sleep(0.6)
    os.system("python3 ~/Desktop/i2c.py 3")
    
def right():
    os.system("python3 ~/Desktop/i2c.py 1")
    time.sleep(0.6)
    os.system("python3 ~/Desktop/i2c.py 4")
    
def move():
    left()
    time.sleep(1)
    right()
    time.sleep(1)
    stop()
    

#bus.write_byte(addr, 0x0) # switch it on