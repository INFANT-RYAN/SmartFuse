from  pyfirmata import Arduino
import psutil
import time

board = Arduino('COM5')
led_pin = board.get_pin("d:7:o")

while True:
   battery = psutil.sensors_battery()
    print(battery.percent)
    if battery.percent < 80:
        led_pin.write(0)
        print("on")
    else:
        led_pin.write(1)
        print("off")
    time.sleep(10)
