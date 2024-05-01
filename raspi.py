from Phidget22.Phidget import *
from Phidget22.Devices.Dictionary import *
from Phidget22.Net import *
from Phidget22.Devices.Manager import *
from time import *
from lib import LCDHelper as LCD
from lib import RCFullRotationHelper as RC
from lib import TempLEDHelper as LED
from lib import VoltageInputHelper as VI
from lib import RFIDHelper as RF
from lib import CapacitiveTouchHelper as CT

TempControl = False
RFIDtag = False
BarrierControl = False
SwingControl = False
LCDConnected = False
TouchConnected = False

lcd0 = None
leds = None
tempSlider = None
swingJoystick = None
barrierThingy = None
wetSlider = None
volumePot = None
rfid0 = None
barrierMotor0 = None
swingMotor0 = None
capacitiveTouch0 = None

RGBpins = {
    "Red": 7,
    "Green": 6,
    "Blue": 5
}

cribDict = None
babyDict = {
    "010693444f": "Number 1"
}

targetTemp = 25
currentTemp = 25

lcdStatus = {
    "babyName":"",
    "temperature":25,
    "isWet":False,
    "newBaby":False,
    "babyAccepted":None
}

def tagHandler(self, tag, protocol):
    global cribDict
    global lcdStatus
    if (cribDict.get("newBaby") == str(False)):
        if (babyDict.get(tag)):
            cribDict.set("babyName", babyDict.get(tag))
        else:
            cribDict.set("babyName", "FAKE BABY ALERT")
    else:
        babyDict[tag] = cribDict.get("newBaby")
        lcdStatus["babyAccepted"] = True
        cribDict.set("newBabyAccepted", str(True))
        cribDict.set("newBaby", str(False))
        sleep(0.5)
        cribDict.set("newBabyAccepted", str(False))
        lcdStatus[""]
    return

def tempHandler(self, voltage):
    global cribDict
    cribDict.set("currentTemperature", str(10 + (voltage * 25)))
    lcdStatus["temperature"] = 10 + (voltage*25)
    LCDupdater()

def swingHandler(self, voltage):
    global cribDict, swingMotor0
    cribDict.set("swingPosition", str(voltage))
    RC.rotate180(swingMotor0, (int(voltage)*2)-1)

def barrierHandler(self, voltage):
    global cribDict, barrierMotor0
    cribDict.set("barrierPosition", str(voltage))
    RC.rotate180(barrierMotor0, (int(voltage)*2)-1)

def wetHandler(self, voltage):
    global cribDict
    cribDict.set("isWet", str(True) if voltage > 0.7 else str(False))
    lcdStatus["isWet"] = True if voltage > 0.7 else False
    LCDupdater()

def soundHandler(self, voltage):
    global cribDict
    cribDict.set("isTooMuch", str(True) if voltage > 0.7 else str(False))

def onNewDevice(self, device):
    global lcd0, leds, rfid0, barrierMotor0, swingMotor0
    global tempSlider, swingJoystick, barrierThingy, wetSlider, volumePot, capacitiveTouch0
    global TempControl, RFIDtag, BarrierControl, SwingControl, LCDConnected, TouchConnected
    print("Device: " + str(device))
    if (device.getDeviceSerialNumber() == 39830): LCDConnected = True
    if (device.getDeviceSerialNumber() == 63514): RFIDtag = True
    if (device.getDeviceSerialNumber() == 14875): BarrierControl = True
    if (device.getDeviceSerialNumber() == 19875): SwingControl = True
    if (device.getDeviceSerialNumber() == 52930): TouchConnected = True
    if(LCDConnected and (lcd0 == None)):
        lcd0 = LCD.setup(39830, 0)
        leds = LED.setup(39830, 7, 6, 5, 0)
        tempSlider = VI.setup(39830, 0, 0)
        tempSlider.setVoltageRatioChangeTrigger(0.05)
        tempSlider.setOnVoltageRatioChangeHandler(tempHandler)
        swingJoystick = VI.setup(39830, 1, 0)
        swingJoystick.setVoltageRatioChangeTrigger(0.05)
        swingJoystick.setOnVoltageRatioChangeHandler(swingHandler)
        wetSlider = VI.setup(39830, 3, 0)
        wetSlider.setVoltageRatioChangeTrigger(0.1)
        wetSlider.setOnVoltageRatioChangeHandler(wetHandler)
        volumePot = VI.setup(39830, 2, 0)
        volumePot.setVoltageRatioChangeTrigger(0.05)
        volumePot.setOnVoltageRatioChangeHandler(soundHandler)
    if(RFIDtag and (rfid0 == None)):
        rfid0 = RF.setup(63514, 1)
        rfid0.lcd = lcd0
        rfid0.setOnTagHandler(tagHandler)
        global waitingForNewBaby 
        waitingForNewBaby = False
    if(BarrierControl and (barrierMotor0 == None)):
        barrierMotor0 = RC.setup(14875, 1)
    if(SwingControl and (swingMotor0 == None)):
        swingMotor0 = RC.setup(19875, 1)
    if(TouchConnected and (barrierThingy == None)):
        barrierThingy = CT.setup(52930, 0)
        #print(str(barrierThingy.getSensitivity()))
        #barrierThingy.setTouchValueChangeTrigger(0.05)
        barrierThingy.setOnTouchHandler(barrierHandler)


def LCDupdater():
    global lcdStatus, lcd0
    if (lcdStatus["newBaby"]):
        if (lcdStatus["babyAccepted"] == 1):
            LCD.write(lcd0, "Waiting for tag...", "")
        elif(lcdStatus["babyAccepted"] == 2):
            LCD.write(lcd0, "Baby accepted", "")
        elif(lcdStatus["babeAccepted"] == 3):
            LCD.write(lcd0, "Nope.", "")
    else:
        LCD.write(lcd0, lcdStatus["babyName"], str(lcdStatus["temperature"]) + " " + "Wet bed" if lcdStatus["isWet"] else "")

def dictUpdate(self, key, value):
    global lcd0, leds, rfid0, barrierMotor0, swingMotor0
    global targetTemp, currentTemp
    print(key)
    if (key == "swingPosition"):
        RC.rotate180(swingMotor0, (int(value)*2)-1)
    elif (key == "barrierPosition"):
        print("Hewo " + value)
        RC.rotate180(barrierMotor0, (float(value)*2)-1)
    elif (key == "targetTemperature"):
        targetTemp = min(int(value), 30)
        targetTemp = max(targetTemp, 20)
    elif (key == "currentTemperature"):
        currentTemp = int(value)
        lcdStatus["temperature"] = currentTemp
        LCDupdater()
    elif (key == "babyName"):
        lcdStatus["babyName"] = value
        LCDupdater()
    elif(key == "newBaby"):
        lcdStatus["newBaby"] = value
        LCDupdater()
    elif (key == "newBabyAccepted"):
        lcdStatus["babyAccepted"] = int(value)
        LCDupdater()
    

def main():

    global cribDict
    net = Net()
    Net.enableServerDiscovery(PhidgetServerType.PHIDGETSERVER_DEVICEREMOTE)
    sleep(5)
    manager = Manager()
    manager.setOnAttachHandler(onNewDevice)
    manager.open()
    cribDict = Dictionary()
    cribDict.setDeviceLabel("Crib")
    cribDict.setDeviceSerialNumber(1000)
    cribDict.openWaitForAttachment(1000)
    cribDict.setOnUpdateHandler(dictUpdate)

    while(True):
        sleep(1)

main()