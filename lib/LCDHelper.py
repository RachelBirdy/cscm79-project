from Phidget22.Phidget import *
from Phidget22.Devices.LCD import *


def setup(serialNo, isRemote = 0):
    lcd0 = LCD()
    lcd0.setChannel(0)
    lcd0.setDeviceSerialNumber(serialNo)
    lcd0.setIsRemote(isRemote)
    lcd0.openWaitForAttachment(5000)
    lcd0.setBacklight(1)
    return lcd0

def write(lcd0, Line1, Line2):
    lcd0.clear()
    lcd0.writeText(LCDFont.FONT_5x8, 0, 0, Line1)
    lcd0.writeText(LCDFont.FONT_5x8, 0, 1, Line2)
    lcd0.flush()

def setdown(lcd0):
    lcd0.close()
