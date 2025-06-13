from microbit import *

def on_forever():
    motorSpeed = 15

    #line following
    lineSensors.display_sensors()
    if lineSensors.check_sensor(IRSensor.MIDDLE, IRColour.BLACK):
        motion.drive_straight(motorSpeed)
    elif lineSensors.check_sensor(IRSensor.LEFT, IRColour.BLACK):
        motion.turn_left(motorSpeed)
    elif lineSensors.check_sensor(IRSensor.RIGHT, IRColour.BLACK):
        motion.turn_right(motorSpeed)
        
    # pausing at obstacle 25cm away
    if sonar.check_sonar() < 25:
        motion.stop()
    else:
        motion.drive_straight(15)

    #moving around obstacle 
    distance = sonar.check_sonar()
    if distance > 25:
        motion.drive_straight(20)
    else:
        motion.drive_straight(-20)
        basic.pause(400)

        if Math.random_boolean():
            motion.turn_left(10)
        else:
            motion.turn_right(10)
        basic.pause(400)
    
basic.forever(on_forever)


