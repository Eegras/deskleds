import RPi.GPIO as G
import time

led1 = 18
led2 = led1+1
led3 = led1+2

speed=1
hertz = 240


usleep = lambda x: time.sleep(x/1000000.0)

G.setwarnings(False)

G.setmode(G.BCM)

G.setup(led1, G.OUT)
G.output(led1, False)
G.setup(led2, G.OUT)
G.output(led2, False)
G.setup(led3, G.OUT)
G.output(led3, False)


red = G.PWM(led1,hertz)
red.start(0)

grn = G.PWM(led2,hertz)
grn.start(0)

blu = G.PWM(led3,hertz)
blu.start(0)

redi=-0
grni=0
blui=0

reddir=speed
grndir=speed
bludir=speed

redval = 0.0
greenval = 0.0
blueval = 0.0
redfloat = 0.0
greenfloat = 0.0
bluefloat = 0.0

ledON = True

while (True):
        desiredHex = raw_input("#").upper()

        redval =   float(int(desiredHex[0:2],16))
        greenval = float(int(desiredHex[2:4],16))
        blueval =  float(int(desiredHex[4:6],16))

        redfloat = float(redval/255)*100
        greenfloat = float(greenval/255)*100
        bluefloat = float(blueval/255)*100

        red.ChangeDutyCycle(redfloat)
        grn.ChangeDutyCycle(greenfloat)
        blu.ChangeDutyCycle(bluefloat)