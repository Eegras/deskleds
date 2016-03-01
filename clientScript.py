# Python port of color_pulse.cpp from the CUE SDK examples.
from __future__ import division
import win32api
import win32con
import time
from cue_sdk import *
import socket
from threading import Thread

class cue_client():
    def __init__(self, desiredHex):
        self.desiredHex = desiredHex
        self.colors = self.get_available_keys()
        self.doSocket()


    def doSocket(self):
        s = socket.socket()
        host = ''
        port = 9000
        print ("Listening on ",host,";",port)
        s.bind((host,port))

        s.listen(5)
        while True:
            c, addr = s.accept()
            #s.connect(addr)
            self.desiredHex = c.recv(8)
            print(self.desiredHex)

            colors = self.colors
            for led in colors:
                led.r = int('0x'+self.desiredHex[0:2],0)
                led.g = int('0x'+self.desiredHex[2:4],0)
                led.b = int('0x'+self.desiredHex[4:6],0)
    
            colors_len = len(colors)
            led_array = CorsairLedColor * colors_len
            Corsair.SetLedsColorsAsync(colors_len, led_array(*colors))

    def range_float(self, start, stop, step):
        while start < stop:
            yield start
            start += step
    
    
    def get_available_keys(self):
        allLeds = [];
        Corsair.ErrorCheck()
        for deviceIndex in range(Corsair.GetDeviceCount()):
            deviceInfo = Corsair.GetDeviceInfo(deviceIndex)
            if deviceInfo[0].type == 1:
                numberOfLeds = deviceInfo[0].physicalLayout
                print ("Mouse: %s"%numberOfLeds)
                for x in range(numberOfLeds):
                    ledId = CLM_1+x
                    if ledId > 151:
                        break
                    allLeds.append(CorsairLedColor(ledId,0,0,0))
            else:
                ledPositions = Corsair.GetLedPositions()
                print ("Keyboard: %s" %ledPositions[0].numberOfLed)
                for x in range(ledPositions[0].numberOfLed):
                    ledId = ledPositions[0].pLedPosition[x].ledId
                    allLeds.append(CorsairLedColor(ledId,0,0,0))
        return allLeds
    
    
    
if __name__ == "__main__":
    Corsair = CUE("CUESDK.x64_2013.dll")
    Corsair.RequestControl(CAM_ExclusiveLightingControl)

    cue_client = cue_client('FACA04')