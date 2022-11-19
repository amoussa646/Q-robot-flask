from flask import Flask, render_template
from flask_socketio import SocketIO

import robot
import i2c
import requests as req
import speech_recognition
import sys
from rasaclient import rasaint,rasatext, ga , say
from actions import action

app = Flask(__name__)
socketio = SocketIO(app,cors_allowed_origins=['http://0.0.0.0:5000'])


recognizer = speech_recognition.Recognizer()
say("What can I do for you?")

@app.route("/")
def home():
    return render_template("voice.html")


@app.route("/remote")
def remote():
    return render_template("remote.html")



@socketio.on('forward')
def forward(data):
    ## When we receive a new event of type
    ## 'message' through a socket.io connection
    ## we print the socket ID and the message
    print(data['data'])
    print("Forward")
    i2c.forward()

@socketio.on('left')
def left(data):
    print(data['data'])
    print("left")
    i2c.left()

@socketio.on('right')
def right(data):
    print(data['data'])
    print("right")
    i2c.right()

@socketio.on('stop')
def stop(data):
    print(data['data'])
    print("stop")
    i2c.stop()

@socketio.on('backward')
def backward(data):
    print(data['data'])
    print("backward")
    i2c.back()
    

@socketio.on('up')
def look_up(data):
    print(data['data'])
    print("look up")
    robot.eyesup()    
@socketio.on('look_left')
def look_left(data):
    print(data['data'])
    print("look left")
    robot.eyesleft()

@socketio.on('look_right')
def look_right(data):
    print(data['data'])
    print("look right")
    robot.eyesright()
@socketio.on('nature')
def nature(data):
    print(data['data'])
    print("look nature")
    robot.eyesforward()

@socketio.on('down')
def look_down(data):
    print(data['data'])
    print("look down")
    robot.eyesdown()

@socketio.on('cute')
def cute(data):
    print(data['data'])
    print("look cute")
    robot.cutebrows()

@socketio.on('uncute')
def uncute(data):
    print(data['data'])
    print("look uncute")
    robot.uncute()

@socketio.on('browse_up')
def browse_up(data):
    print(data['data'])
    print("browse_up")
    robot.browsup()

@socketio.on('browse_down')
def browse_down(data):
    print(data['data'])
    print("browse_down")
    robot.browsdown()

@socketio.on('home')
def home(data):
    print(data['data'])
    print("Arm is home")
    robot.armhome()

@socketio.on('pick')
def pick(data):
    print(data['data'])
    print("Arm is picking")
    robot.armpick()


@socketio.on('sing')
def sing(data):
    print(data['data'])
    print("Arm is singing")
    robot.armsing()

@socketio.on('say')
def say(data):
    print("saying")
    try:
        url = 'http://0.0.0.0:6000/index?source='+data
        resp = req.get(url)
    except:
        url = 'http://0.0.0.0:6000/index?source='+data['data']
        resp = req.get(url)
        
    
@socketio.on('wave')
def wave(data):
    print(data['data'])
    print("saying")
    robot.wave()
    
@socketio.on('listen')
def listen(data):
    try:  
        with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                message = recognizer.recognize_google(audio)
                message = message.lower()
                print(message)
                intent=""
                entityName=""
                entityValue=""
                answer = rasatext(message)
                try:
                    text = answer[0]['text']
                    print(text)
                    say(text)         
                except:
                    print("Didn't recieve text from server")
                    nlu= rasaint(message)
                    print(nlu)
                    
                    
                nlu= rasaint(message)
                print(nlu)
                action(nlu)
                
                        
                
                
    except speech_recognition.UnknownValueError:
      print("erroooooor")
    
if __name__ == "__main__":
    socketio.run(app,host='0.0.0.0')
