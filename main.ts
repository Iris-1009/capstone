basic.forever(function on_forever() {
    let motorSpeed = 15
    // line following
    lineSensors.displaySensors()
    if (lineSensors.checkSensor(IRSensor.MIDDLE, IRColour.BLACK)) {
        motion.driveStraight(motorSpeed)
    } else if (lineSensors.checkSensor(IRSensor.LEFT, IRColour.BLACK)) {
        motion.turnLeft(motorSpeed)
    } else if (lineSensors.checkSensor(IRSensor.RIGHT, IRColour.BLACK)) {
        motion.turnRight(motorSpeed)
    }
    
    //  pausing at obstacle 25cm away
    if (sonar.checkSonar() < 25) {
        motion.stop()
    } else {
        motion.driveStraight(15)
    }
    
    // moving around obstacle 
    let distance = sonar.checkSonar()
    if (distance > 25) {
        motion.driveStraight(20)
    } else {
        motion.driveStraight(-20)
        basic.pause(400)
        if (Math.randomBoolean()) {
            motion.turnLeft(10)
        } else {
            motion.turnRight(10)
        }
        
        basic.pause(400)
    }
    
})
