from Phidget22.Phidget import *
from Phidget22.Devices.Dictionary import *
from Phidget22.Net import *
from Phidget22.Devices.Manager import *
from time import *

def onServerAdded(self, server, kv):
    print("Server: " + str(server))
    print("Kv: " + str(kv))

def onNewDevice(self, device):
    print("Device: " + str(device))

def main():
    net = Net()
    net.setOnServerAddedHandler(onServerAdded)
    Net.enableServerDiscovery(PhidgetServerType.PHIDGETSERVER_DEVICEREMOTE)
    sleep(5)
    manager = Manager()
    manager.setOnAttachHandler(onNewDevice)
    manager.open()
    cribDict = Dictionary()
    cribDict.setDeviceLabel("Crib")
    cribDict.setDeviceSerialNumber(1000)
    cribDict.openWaitForAttachment(1000)
    cribDict.set("test", "69")
    print(cribDict.get("test"))
    cribDict.close()
    
main()