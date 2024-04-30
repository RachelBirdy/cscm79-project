from Phidget22.Devices.DCMotor import *
from Phidget22.Devices.RCServo import *
from time import *
dcMotor0 = RCServo()
dcMotor0.setDeviceSerialNumber(14875)
dcMotor0.openWaitForAttachment(5000)
dcMotor0.setTargetPosition(0)
dcMotor0.setEngaged(True)
sleep(5)
dcMotor0.setTargetPosition(180)
sleep(5)
dcMotor0.close()