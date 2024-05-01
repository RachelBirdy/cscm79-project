from Phidget22.Devices.CapacitiveTouch import *

def setup(serialNo, isRemote = 0):
    vi0 = CapacitiveTouch()
    vi0.setDeviceSerialNumber(serialNo)
    vi0.setIsRemote(isRemote)
    vi0.openWaitForAttachment(5000)
    return vi0