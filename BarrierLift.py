from lib import RCFullRotationHelper as RC
from lib import DigitalIOHelper
from lib import LCDHelper
from lib import RFIDHelper
from Phidget22.Devices.RCServo import *
from Phidget22.Net import *
import time

def tagHandler(self, a, b):
    print(self)
    print(a)
    print(b)
    print("READ COMPLETE")

def main():
    Net.enableServerDiscovery(PhidgetServerType.PHIDGETSERVER_DEVICEREMOTE)
    rfid0 = RFIDHelper.setup(63514, 1)
    print("Setup done")
    rfid0.setOnTagHandler(tagHandler)
    time.sleep(10)
    rfid0.close()

main()