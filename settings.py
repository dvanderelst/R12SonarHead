import pyb

# Common settings

red = pyb.LED(1)
green = pyb.LED(2)
blue = pyb.LED(3)

adc_pin1 = 'X7'
trigger_pin1 = 'X1'
adc_pin2 = 'X8'
trigger_pin2 = 'X2'

data_sep = ','

# For field context

servo_pin = 'X6'
servo_pulse_range = [500, 2500] # in usecs

signal_threshold = 2000
sample_rate = 20000
duration = 25
repeats = 3


# For robot context

wifi_ssid = 'batnet'
wifi_password = 'lebowski'
break_character = '*'
port_number = 1000
