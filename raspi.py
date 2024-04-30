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

TempControl = False
RFIDtag = False
BarrierControl = False
SwingControl = False
LCDConnected = False

lcd0 = None
leds = None
voltage0 = None
rfid0 = None
barrierMotor0 = None
swingMotor0 = None

def onServerAdded(self, server, kv):
    print("Server: " + str(server))
    print("Kv: " + str(kv))

def onNewDevice(self, device):
    print("Device: " + str(device))
    if (device.getDeviceSerialNumber() == 39830): LCDConnected = True
    if (device.getDeviceSerialNumber() == 63514): RFIDtag = True
    if (device.getDeviceSerialNumber() == 14875): BarrierControl = True
    if (device.getDeviceSerialNumber() == 19875): SwingControl = True

RGBpins = {
    "Red": 7,
    "Green": 6,
    "Blue": 5
}

def main():


    net = Net()
    net.setOnServerAddedHandler(onServerAdded)
    Net.enableServerDiscovery(PhidgetServerType.PHIDGETSERVER_DEVICEREMOTE)
    sleep(5)
    manager = Manager()
    manager.setOnAttachHandle(onNewDevice)
    manager.open()
    cribDict = Dictionary()
    cribDict.setDeviceLabel("Crib")
    cribDict.setDeviceSerialNumber(1000)
    cribDict.openWaitForAttachment(1000)
    cribDict.set("test", "69")
    print(cribDict.get("test"))
    cribDict.close()

    while(True):
        time.sleep(1)

main()