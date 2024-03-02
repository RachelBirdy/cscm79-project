from lib import LCDHelper as LCD
from lib import RCFullRotationHelper as RC
import time

def main():
    RC.setup(14875)
    print("Setup done?")
    RC.rotate(1.0)
    time.sleep(1)
    RC.rotate(0.1)
    time.sleep(1)
    RC.rotate(0)
    time.sleep(1)
    RC.rotate(-0.5)
    time.sleep(1)
    RC.setdown()

main()