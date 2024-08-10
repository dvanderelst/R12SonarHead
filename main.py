import usocket
import time
import gc
import misc
import measure
import server
import ujson    
import settings

from machine import Pin

green = settings.green # connecting to wifi
red = settings.red # create server, wait for input
blue = settings.blue # do measurement
# all on: error in server


gc.collect()

#misc.boot_display_robot()
#swich on 3V pin
Pin.board.EN_3V3.value(1)


while True:
    green.on()
    server.connect2wifi()
    green.off()
    
    red.on()
    data_server = server.Server()
    red.off()
    
    message = data_server.receive_data()
    message = message.split(settings.data_sep)
    first = int(message[0])
    second = int(message[1])
    sample_rate = int(message[2])
    duration = int(message[3])
    
    blue.on()
    buffer = measure.measure_both(first, second, sample_rate, duration)
    blue.off()

    buffer = ujson.dumps(buffer)
    data_server.send_data(buffer)
    
    data_server.disconnect()
    del(data_server)
    gc.collect()

