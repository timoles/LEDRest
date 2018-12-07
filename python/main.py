#!env python

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import os
import urlparse
import threading

import time
from neopixel import *

PORT_NUMBER = 7070

# LED strip configuration:
LED_COUNT      = 16      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

colorR = 0
colorG = 0
colorB = 0
#This class will handles any incoming request from
#the browser


def runLedStrip():
	while True:
		colorWipe(strip, Color(255, 0, 0))

def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)


class myHandler(BaseHTTPRequestHandler):

	#Handler for the GET requests
	def do_GET(self):
		# do some stuff
		global colorR
		global colorG
		global colorB
		# continue doing stuff
		print download_thread.isAlive()
		# Get parameter
		imsi = urlparse.parse_qs(urlparse.urlparse(self.path).query).get('imsi', None)
		print imsi  # Prints None or the string value of imsi
		
		# Split path to get base path
		path = self.path.split("?")
		print path

		return
		if self.path=="/on":
			pass
		if self.path=="/off":
			pass
		if self.path=="/modify":
			pass

		self.send_response(404)
		self.send_header('Content-type','text/html')
		self.end_headers()
		# Send the html message
		self.wfile.write("Not found")
		return

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
	#Wait forever for incoming htto requests

	download_thread = threading.Thread(target=runLedStrip, args="")
	download_thread.start()
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()
