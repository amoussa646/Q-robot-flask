import sys

from smbus import SMBus
import time
addr = 0x6 # bus address
bus = SMBus(1) # indicates /dev/ic2-1

numb = 1

def forward():
    stop()
    bus.write_byte(addr,5)
    
def stop():
    bus.write_byte(addr,1)
    
def back():
    stop()
    bus.write_byte(addr,2)
    
def left():
    stop()
    bus.write_byte(addr,3)
    
def right():
    stop()
    bus.write_byte(addr,4)
    

#bus.write_byte(addr, 0x0) # switch it on