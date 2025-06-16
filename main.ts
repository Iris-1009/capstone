let motorSpeed = 15
// Line Following
basic.forever(function on_forever() {
    lineSensors.displaySensors()
    // uses the middle sensor to detect black, proceeds if true
    if (lineSensors.checkSensor(IRSensor.MIDDLE, IRColour.BLACK)) {
        motion.driveStraight(motorSpeed)
    } else if (lineSensors.checkSensor(IRSensor.LEFT, IRColour.BLACK)) {
        // uses the left sensor to detect black, turns left if true   
        motion.turnLeft(motorSpeed)
    } else if (lineSensors.checkSensor(IRSensor.RIGHT, IRColour.BLACK)) {
        // uses the right sensor to detect black, turns right if true
        motion.turnRight(motorSpeed)
    } else {
        // if white detected, vehicle stops (no path to follow)
        motion.stop()
    }
    
})
//  Obstacle Avoidance
basic.forever(function on_forever2() {
    let distance = sonar.checkSonar()
    // gets the distance between object and sensor
    if (distance > 25) {
        // distance further than 25cm, proceeds 
        motion.driveStraight(20)
    } else {
        // if too close
        motion.driveStraight(-20)
        // reverse 
        basic.pause(400)
        // picks a random direction to turn
        if (Math.randomBoolean() == true) {
            motion.turnLeft(10)
        } else {
            motion.turnRight(10)
        }
        
        basic.pause(400)
    }
    
})
// Stopping at Obstacle closer than 20cm
basic.forever(function on_forever3() {
    if (sonar.checkSonar() < 20) {
        motion.stop()
    } else {
        motion.driveStraight(20)
    }
    
})
// Driving Functions based off time
// Forward 
function DriveForward(seconds: number) {
    motion.driveStraight(10)
    control.waitMicros(seconds * 1000000)
    // converts to microseconds
    motion.stop()
}

// Reverse
function DriveBackward(seconds: number) {
    motion.driveStraight(-10)
    control.waitMicros(seconds * 1000000)
    motion.stop()
}

// Turns  
function Turn(direction: string, seconds: number) {
    if (direction == "left") {
        motion.turnLeft(5)
    } else if (direction == "right") {
        motion.turnRight(5)
    }
    
    control.waitMicros(seconds * 1000000)
    motion.stop()
}

// Simple Example
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    DriveForward(1)
    Turn("left", 0.5)
    DriveForward(2)
    DriveBackward(1)
})
// Driving by following given instructions in N, E, S, W in a list (this could be combined with bfs algorithm)
let instructions = ["N", "E", "N", "N", "W"]
input.onButtonPressed(Button.A, function on_button_pressed_a1() {
    for (let direction of instructions) {
        if (direction == "N") {
            DriveForward(1)
        } else if (direction == "E") {
            Turn("right", 0.5)
            DriveForward(0.5)
        } else if (direction == "W") {
            Turn("left", 0.5)
            DriveForward(0.5)
        } else if (direction == "S") {
            DriveBackward(1)
        }
        
    }
})
