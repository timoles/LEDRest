# LED Strip control with ESP8266 ESP-12 E

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

## Notes

* The old directory contains stuff to controll the LED strip through a raspberry pi 