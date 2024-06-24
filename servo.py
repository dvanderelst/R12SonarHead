import pyb
import utime
import settings
from array import array
import time



def position(pw, wait_time=1, sleep_time=0.25, check_range=True):
    min_value = settings.servo_pulse_range[0]
    max_value = settings.servo_pulse_range[1]
    if check_range:
        if pw < min_value: pw = min_value
        if pw > max_value: pw = max_value
    servo_pin = pyb.Pin(settings.servo_pin, pyb.Pin.OUT_PP)
    utime.sleep_ms(10)
    start_counter = utime.ticks_ms()
    while True:
        servo_pin.high()
        utime.sleep_us(pw)
        servo_pin.low()
        utime.sleep_ms(20)
        current_counter = utime.ticks_ms()
        if current_counter - start_counter > (wait_time * 1000): break
    time.sleep(sleep_time)
        
        
if __name__ == "__main__":
    position(1500)
    time.sleep(3)
    positions = settings.servo_positions
    for x in positions: position(x)