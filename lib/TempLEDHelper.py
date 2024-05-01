from Phidget22.Devices.DigitalOutput import *

def setup(serialNo, pinR, pinG, pinB, isRemote = 0):
    ledR = DigitalOutput()
    ledG = DigitalOutput()
    ledB = DigitalOutput()
    ledR.setChannel(pinR)
    ledG.setChannel(pinG)
    ledB.setChannel(pinB)
    ledR.setDeviceSerialNumber(serialNo)
    ledG.setDeviceSerialNumber(serialNo)
    ledB.setDeviceSerialNumber(serialNo)
    ledR.setIsRemote(isRemote)
    ledG.setIsRemote(isRemote)
    ledB.setIsRemote(isRemote)
    ledR.openWaitForAttachment(5000)
    ledG.openWaitForAttachment(5000)
    ledB.openWaitForAttachment(5000)
    return (ledR, ledG, ledB)

def setdown(leds):
    ledR, ledG, ledB = leds
    ledR.close()
    ledG.close()
    ledB.close()

def setDistance(dist, leds):
    ledR, ledG, ledB = leds
    print(dist)
    if (dist == 0.0):
        ledR.setDutyCycle(0)
        ledG.setDutyCycle(1)
        ledB.setDutyCycle(0)
    elif (dist > 0.0 and dist <= 0.25):
        ledR.setDutyCycle(0)
        ledG.setDutyCycle(1)
        ledB.setDutyCycle(0)
    elif (dist > 0.25 and dist <= 0.5):
        ledR.setDutyCycle(1)
        ledG.setDutyCycle(1)
        ledB.setDutyCycle(0)
    elif (dist > 0.5 and dist <= 0.75):
        ledR.setDutyCycle(1)
        ledG.setDutyCycle(0)
        ledB.setDutyCycle(0)
    elif (dist > 0.75):
        ledR.setDutyCycle(1)
        ledG.setDutyCycle(0)
        ledB.setDutyCycle(0)
    elif (dist < 0.0 and dist >= -0.25):
        ledR.setDutyCycle(0)
        ledG.setDutyCycle(1)
        ledB.setDutyCycle(0)
    elif (dist < 0.25 and dist >= -0.5):
        ledR.setDutyCycle(0)
        ledG.setDutyCycle(1)
        ledB.setDutyCycle(1)
    elif (dist < 0.5 and dist >= -0.75):
        ledR.setDutyCycle(0)
        ledG.setDutyCycle(0)
        ledB.setDutyCycle(1)
    elif (dist < 0.75):
        ledR.setDutyCycle(0)
        ledG.setDutyCycle(0)
        ledB.setDutyCycle(1)