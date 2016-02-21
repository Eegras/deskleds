import time
import BaseHTTPServer
import RPi.GPIO as G
import time
from threading import Thread

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

desiredHex = '000000'

ledON = True

HOST_NAME = '192.168.2.4' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 9000 # Maybe set this to 9000.

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("<html><head><title>Title goes here.</title></head>")
        s.wfile.write("<body><p>This is a test.</p>")
        # If someone went to "http://something.somewhere.net/foo/bar/",
        # then s.path equals "/foo/bar/".
        desiredHex = s.path.replace("/","")
        s.wfile.write("<p>You accessed path: %s</p>" % s.path)
        s.wfile.write("</body></html>")

        desiredHex = s.path.replace("/","")

        redval =   float(int(desiredHex[0:2],16))
        greenval = float(int(desiredHex[2:4],16))
        blueval =  float(int(desiredHex[4:6],16))
    
        redfloat = float(redval/255)*100
        greenfloat = float(greenval/255)*100
        bluefloat = float(blueval/255)*100
    
        red.ChangeDutyCycle(redfloat)
        grn.ChangeDutyCycle(greenfloat)
        blu.ChangeDutyCycle(bluefloat)

server_class = BaseHTTPServer.HTTPServer
httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
httpd.server_close()
print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)