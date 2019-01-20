# LED Strip control with ESP8266 ESP-12 E

## Features 

### Controll features for the strip:

* Set brightness

* Set color

* Turn strip on

* Turn strip off

* Save color and brightness state throughout power cycles

## Usage

1. Download and install Arduino IDE

2. Import `esp8266_ledstrip.ino` sketch from this repo

3. Update Wifi SSID and password

3. Compile and upload sketch to ESP8266

5. Wire the ESP8266 with a WS2811b LED strip

6. Connect power

7. Check in router settings which IP was assigned to the ESP8266

8. cd into the `webserver` directory

9. Upload the index.html file

	```bash
	for file in `ls -A1`; do curl -F "file=@$PWD/$file" <IP_of_ESP8266>/edit; done
	```

10. Access `http://<ip>/`

11. Controll the Strip

## Wiring

* A 6.2V capacitor is installed inbetween the negative and positive connection to the LED strip to absorb voltage spikes.


* I used a 5V 2Amp power supply to power both the LED strip (Strip PIN `VIN`)
 and the ESP8266 (PIN `D1`)
* A resistor ~500 ohm is inbetween the ESP8266 and the `DIN`

* The ground of the LED strip should aditionaly to the normal ground be connected to the ESP8266 ground (don't know if redundancy is needed, but the ground at the ESP8266 is definetly needed)

* Tested with a strip the size of 30 LED

## Notes

* The old directory contains stuff to controll the LED strip through a raspberry pi

* All these things should be used with caution because I'm not an electrical engineer

* Also there are no authentication and encryption features (the `old` directory contains a setup with a reverse proxy, encryption and authentication (tested on a raspberry pi))
