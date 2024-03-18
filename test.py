from lib import LCDHelper as LCD
from lib import RCFullRotationHelper as RC
from lib import TempLEDHelper as LED
from lib import VoltageInputHelper as VI
from lib import RFIDHelper as RF
import time

RFIDtag = False
TempControl = False
BarrierControl = True

RGBpins = {
    "Red": 7,
    "Green": 6,
    "Blue": 5
}

babyDict = {
    "010693444f": "Number 1"
}

def voltChange(self, voltageRatio):
    print(voltageRatio)
    LED.setDistance((voltageRatio*2)-1,self.leds) 

def tagHandler(self, tag, protocol):
    if (babyDict.get(tag)):
        LCD.write(self.lcd, babyDict[tag] + "detected", "")
    else:
        LCD.write(self.lcd, "FAKE BABY ALERT", "")
    return

def barrierMove(self, voltageRatio):
    RC.rotate(self.motor, (voltageRatio*2)-1)

def main():
    lcd0 = LCD.setup(39830, 0)

    if (TempControl):
        leds = LED.setup(39830, 7, 6, 5)
        voltage0 = VI.setup(39830, 0)
        voltage0.leds = leds
        voltage0.setVoltageRatioChangeTrigger(0.1)
        voltage0.setOnVoltageRatioChangeHandler(voltChange)

    if (RFIDtag):
        rfid0 = RF.setup(63514, 0)
        rfid0.lcd = lcd0
        rfid0.setOnTagHandler(tagHandler)

    if (BarrierControl):
        barrierMotor0 = RC.setup(14875)
        voltage1 = VI.setup(39830, 0)
        voltage1.motor = barrierMotor0
        voltage1.setOnVoltageRatioChangeHandler(barrierMove)


    while(True):
        time.sleep(1)
    

main()