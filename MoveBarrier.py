import sys
from Phidget22.Devices.Dictionary import *
from Phidget22.Net import *
from lib import LCDHelper as LCD
from lib import VoltageInputHelper as VI
import time
line1 = ""
line2 = ""

def barrierMove(self, vRatio):
    self.cribDict.set("barrierPosition", str(vRatio))

def swingMove(self, vRatio):
    self.cribDict.set("swingPosition", str(vRatio))

def targetTempSet(self, vRatio):
    self.cribDict.set("targetTemperature", str(10+(vRatio*25)))

def dictUpdate(self, key, value):
    global line1, line2
    if (key == "isTooMuch"):
        print("Update babycry" + value)
        line1 = "Baby is crying" if (value == "True") else ""
    if (key == "isWet"):
        line2 = "Bed is wet" if (value == "True") else ""
    LCD.write(self.lcd, line1, line2)

def main():
    Net.enableServerDiscovery(PhidgetServerType.PHIDGETSERVER_DEVICEREMOTE)
    lcd0 = LCD.setup(29773)
    targetTemp = VI.setup(29773, 0)
    swingPos = VI.setup(29773, 1)
    barrierPos = VI.setup(29773, 2)
    targetTemp.setVoltageRatioChangeTrigger(0.05)
    swingPos.setVoltageRatioChangeTrigger(0.05)
    barrierPos.setVoltageRatioChangeTrigger(0.05)


    cribDict = Dictionary()
    cribDict.setDeviceLabel("Crib")
    cribDict.setIsRemote(True)
    cribDict.openWaitForAttachment(5000)
    cribDict.setOnUpdateHandler(dictUpdate)
    cribDict.lcd = lcd0

    lcd0.cribDict = cribDict
    targetTemp.cribDict = cribDict
    swingPos.cribDict = cribDict
    barrierPos.cribDict = cribDict

    barrierPos.setOnVoltageRatioChangeHandler(barrierMove)
    targetTemp.setOnVoltageRatioChangeHandler(targetTempSet)
    swingPos.setOnVoltageRatioChangeHandler(swingMove)
    while(True):
        time.sleep(1)

    print(str(cribDict.get("barrierPosition")))
    cribDict.close()

main()