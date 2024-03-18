from Phidget22.Devices.VoltageRatioInput import *

def setup(serialNo, channel, isRemote = 0):
    vi0 = VoltageRatioInput()
    vi0.setDeviceSerialNumber(serialNo)
    vi0.setIsRemote(isRemote)
    vi0.setChannel(channel)
    vi0.openWaitForAttachment(5000)
    return vi0