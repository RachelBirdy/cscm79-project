from Phidget22.Phidget import *
from Phidget22.Devices.RCServo import *

Neutral = 91
MaxRot = 180

def setup(serialNo, isRemote = 0):
    rcServo0 = RCServo()
    rcServo0.setDeviceSerialNumber(serialNo)
    rcServo0.setChannel(0)
    rcServo0.setIsRemote(isRemote)
    rcServo0.openWaitForAttachment(5000)
    rcServo0.setTargetPosition(0)
    rcServo0.setEngaged(True)
    return rcServo0

def rotate(rcServo0, speed:float):
    if((speed > 1) | (speed < -1)):
        raise ValueError("Speed must be between 1.0 ad -1.0")
    if (speed < 0.1 and speed > -0.1):
        speed = 0
    rcServo0.setTargetPosition(Neutral + (MaxRot - Neutral)*speed)

def rotate180(rcServo0, destination):
    rcServo0.setTargetPosition(int(90+(destination*90)))

def rotClockwise(rcServo0, distance):
    rcServo0.setTargetPosition(90+distance)

def rotAntiClockwise(rcServo0, distance):
    rcServo0.setTargetPosition(90-distance)

def setdown(rcServo0):
    rcServo0.close()
