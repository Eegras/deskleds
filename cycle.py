import RPi.GPIO as G
import time
import random

led1 = 18
led2 = led1+1
led3 = led1+2

speed=(1.0/255.0)
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

redi=random.randrange(10,90)
grni=random.randrange(10,90)
blui=random.randrange(10,90)

reddir=random.choice([speed, -1*speed])
grndir=random.choice([speed, -1*speed])
bludir=random.choice([speed, -1*speed])

ledON = True

while (True):
        if (redi<100 and redi>0):
                red.ChangeDutyCycle(redi)
        elif (redi>=100):
                red.ChangeDutyCycle(100)
        elif (redi<=0):
                red.ChangeDutyCycle(0)

        if (grni<100 and grni>0):
                grn.ChangeDutyCycle(grni)
        elif (grni>=100):
                grn.ChangeDutyCycle(100)
        elif (grni<=0):
                grn.ChangeDutyCycle(0)

        if (blui<100 and blui>0):
                blu.ChangeDutyCycle(blui)
        elif (blui>=100):
                blu.ChangeDutyCycle(100)
        elif (blui<=0):
                blu.ChangeDutyCycle(0)

	time.sleep(0.0005)
        #print ("%s | %s | %s" % (redi,grni,blui))
        redi=redi+reddir
        grni=grni+grndir
        blui=blui+bludir
        if (redi>=110 and reddir>0):
                reddir=-1*(speed*random.randrange(1,10))
        if (grni>=120 and grndir>0):
                grndir=-1*(speed*random.randrange(1,10))
        if (blui>=130 and bludir>0):
                bludir=-1*(speed*random.randrange(1,10))

        if (redi<=-10 and reddir<0):
                reddir=(speed*random.randrange(1,10))
        if (grni<=-30 and grndir<0):
                grndir=(speed*random.randrange(1,10))
        if (blui<=-50 and bludir<0):
                bludir=(speed*random.randrange(1,10))
