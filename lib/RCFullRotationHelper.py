from Phidget22.Phidget import *
from Phidget22.Devices.RCServo import *

#rcServo0 = None
setupComplete = False
Neutral = 91
MaxRot = 180

def setup(serialNo):
    global rcServo0
    global setupComplete
    rcServo0 = RCServo()
    rcServo0.setDeviceSerialNumber(serialNo)
    rcServo0.setChannel(0)
    rcServo0.openWaitForAttachment(5000)
    rcServo0.setTargetPosition(0)
    rcServo0.setEngaged(True)
    setupComplete = True
    return

def rotate(speed:float):
    if((speed > 1) | (speed < -1)):
        raise ValueError("Speed must be between 1.0 ad -1.0")
    if(setupComplete):
        rcServo0.setTargetPosition(Neutral + (MaxRot - Neutral)*speed)

def rotClockwise(distance):
    if(setupComplete):
        rcServo0.setTargetPosition(90+distance)

def rotAntiClockwise(distance):
    global setupComplete
    if(setupComplete):
        rcServo0.setTargetPosition(90-distance)

def setdown():
    global setupComplete
    global rcServo0
    if(setupComplete):
        rcServo0.close()
        setupComplete = False
        rcServo0 = None