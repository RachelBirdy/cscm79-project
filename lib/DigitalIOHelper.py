from Phidget22.Devices.DigitalInput import *
from Phidget22.Devices.DigitalOutput import *

def setupInput(serialNo, channel, isRemote = 0):
    digIn = DigitalInput()
    digIn.setChannel(channel)
    digIn.setDeviceSerialNumber(serialNo)
    digIn.setIsRemote(isRemote)
    digIn.openWaitForAttachment(5000)
    return digIn

def setupOutput(serialNo, channel, isRemote = 0):
    digOut = DigitalOutput()
    digOut.setChannel(channel)
    digOut.setDeviceSerialNumber(serialNo)
    digOut.setIsRemote(isRemote)
    digOut.openWaitForAttachment(5000)
    return digOut
