from Phidget22.Phidget import *
from Phidget22.Devices.LCD import *

lcd0 = None
setupComplete = False

def setup(serialNo):
    lcd0 = LCD()
    lcd0.setChannel(0)
    lcd0.setDeviceSerialNumber(serialNo)
    lcd0.openWaitForAttachment(5000)
    setupComplete=True
    return lcd0

def write(Line1, Line2):
    if(setupComplete):
        lcd0.clear()
        lcd0.writeText(LCDFont.FONT_5x8, 0, 0, Line1)
        lcd0.writeText(LCDFont.FONT_5x8, 0, 1, Line2)
        lcd0.flush()
    return

