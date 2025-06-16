from microbit import *

motorSpeed = 15

#Line Following
def on_forever():
    lineSensors.display_sensors() 
    #uses the middle sensor to detect black, proceeds if true
    if lineSensors.check_sensor(IRSensor.MIDDLE, IRColour.BLACK):
        motion.drive_straight(motorSpeed)
    #uses the left sensor to detect black, turns left if true   
    elif lineSensors.check_sensor(IRSensor.LEFT, IRColour.BLACK):
        motion.turn_left(motorSpeed)
    #uses the right sensor to detect black, turns right if true
    elif lineSensors.check_sensor(IRSensor.RIGHT, IRColour.BLACK):
        motion.turn_right(motorSpeed)
    #if white detected, vehicle stops (no path to follow)
    else:
        motion.stop()
basic.forever(on_forever)

# Obstacle Avoidance
def on_forever2():
    distance = sonar.check_sonar() #gets the distance between object and sensor
    if distance > 25: #distance further than 25cm, proceeds 
        motion.drive_straight(20)
    else: #if too close
        motion.drive_straight(-20) #reverse 
        basic.pause(400)
        #picks a random direction to turn
        if Math.random_boolean() == True:  
            motion.turn_left(10)
        else:
            motion.turn_right(10) 
        basic.pause(400)
basic.forever(on_forever2)

#Stopping at Obstacle closer than 20cm
def on_forever3():
    if sonar.check_sonar() < 20: 
        motion.stop()
    else:
        motion.drive_straight(20)
basic.forever(on_forever3)

#Driving Functions based off time
#Forward 
def DriveForward(seconds: number):
    motion.drive_straight(10)
    control.wait_micros(seconds * 1000000) #converts to microseconds
    motion.stop()
    
#Reverse
def DriveBackward(seconds: number):
    motion.drive_straight(-10)
    control.wait_micros(seconds * 1000000)
    motion.stop()
#Turns  
def Turn(direction: str, seconds: numer):
    if direction == "left":
        motion.turn_left(5)
    elif direction == "right":
        motion.turn_right(5)
    control.wait_micros(seconds * 1000000)
    motion.stop()

#Simple Example
def on_button_pressed_a():
    DriveForward(1)
    Turn("left", 0.5)
    DriveForward(2)
    DriveBackward(1)
input.on_button_pressed(Button.A, on_button_pressed_a)

#Driving by following given instructions in N, E, S, W in a list (this could be combined with bfs algorithm)
instructions = ["N", "E", "N", "N", "W"]
def on_button_pressed_a1():
    for direction in instructions:
        if direction == "N":
            DriveForward(1)
        elif direction == "E":
            Turn("right", 0.5)
            DriveForward(0.5)
        elif direction == "W":
            Turn("left", 0.5)
            DriveForward(0.5)
        elif direction == "S":
            DriveBackward(1)
input.on_button_pressed(Button.A, on_button_pressed_a1)

#features 
#1. line following
#2. obstacle avoidance 
#4. maybe just show normal driving abilities (turn, reverse, forward)
#5. go through map, set up with 2d grid