import os
import socket
import sys
import time
import settings
import network


green = settings.green
blue = settings.blue
red = settings.red


def connect2wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        green.on()
        sta_if.active(True)
        sta_if.connect(settings.wifi_ssid, settings.wifi_password)
        while not sta_if.isconnected(): pass
        green.off()


class Server:
    def __init__(self):
        self.break_character = settings.break_character
        self.buffer_size = 1024
        self.skt = socket.socket()
        self.skt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.skt.bind(('', settings.port_number))
        self.skt.listen(1)       
        try:
            self.connection, self.address = self.skt.accept()
        except Exception as e:
            red.on()
            blue.on()
            green.on()
            self.skt.close()
            raise e
 
    def disconnect(self):
        try:
            if self.connection:
                self.connection.close()
        finally:
            if self.skt:
                self.skt.close()
                
    def receive_data(self):
        data = ''
        try:
            while True:
                packet = self.connection.recv(self.buffer_size)
                if not packet: break
                data += packet.decode()
                if data.endswith(self.break_character): break
        except Exception as e:
            print(f"Error receiving data: {e}")
        data = data.rstrip(self.break_character + '\n')
        return data
    
    def send_data(self, message):
        if not message.endswith(self.break_character):
            message += self.break_character
        try:
            self.connection.sendall(message.encode())
        except Exception as e:
            print(f"Error sending data: {e}")