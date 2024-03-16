from Phidget22.Devices.RFID import *

def setup(serialNo, isRemote):
    rfid0 = RFID()
    rfid0.setDeviceSerialNumber(serialNo)
    rfid0.setIsRemote(isRemote)
    rfid0.openWaitForAttachment(5000)
    return rfid0