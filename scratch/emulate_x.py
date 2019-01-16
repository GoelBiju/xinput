import pyxinput
import time

MyVirtual = pyxinput.vController(percent=False)

while True:
    for x in range(10):
        MyVirtual.set_value('BtnX', 1)
        time.sleep(0.5)
        print("Pressed X")

    for x in range(10):
        MyVirtual.set_value('BtnX', 0)
        time.sleep(0.5)
        print("Released X")
