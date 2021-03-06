# Prepare Raspberry Pi

## Info

* ssh pi@192.168.0.101
* pi:raspberry
* IP might needs to be changed in the following config
* change SSH password

##  Set up start
	sudo apt update
	
	sudo apt install -y apache2 apache2-utils vim git python-dev swig scons
	
	sudo openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt
	
	sudo openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048
	
	
	sudo vim /etc/apache2/conf-available/ssl-params.conf
	
	```
	# from https://cipherli.st/
	# and https://raymii.org/s/tutorials/Strong_SSL_Security_On_Apache2.html

	SSLCipherSuite EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH
	SSLProtocol All -SSLv2 -SSLv3
	SSLHonorCipherOrder On
	# Disable preloading HSTS for now.  You can use the commented out header line that includes
	# the "preload" directive if you understand the implications.
	#Header always set Strict-Transport-Security "max-age=63072000; includeSubdomains; preload"
	Header always set Strict-Transport-Security "max-age=63072000; includeSubdomains"
	Header always set X-Frame-Options DENY
	Header always set X-Content-Type-Options nosniff
	# Requires Apache >= 2.4
	SSLCompression off 
	SSLSessionTickets Off
	SSLUseStapling on 
	SSLStaplingCache "shmcb:logs/stapling-cache(150000)"

	SSLOpenSSLConfCmd DHParameters "/etc/ssl/certs/dhparam.pem"
	```
	
	sudo cp /etc/apache2/sites-available/default-ssl.conf /etc/apache2/sites-available/default-ssl.conf.bak
	
	sudo vim /etc/apache2/sites-available/default-ssl.conf
	
	```
	<IfModule mod_ssl.c>
        <VirtualHost _default_:443>
                ServerAdmin raspberry@mtimo.de
                ServerName 192.168.0.101

                DocumentRoot /var/www/html

                ErrorLog ${APACHE_LOG_DIR}/error.log
                CustomLog ${APACHE_LOG_DIR}/access.log combined

                SSLEngine on

                SSLCertificateFile     /etc/ssl/certs/apache-selfsigned.crt
                SSLCertificateKeyFile /etc/ssl/private/apache-selfsigned.key

                <FilesMatch "\.(cgi|shtml|phtml|php)$">
                                SSLOptions +StdEnvVars
                </FilesMatch>
                <Directory /usr/lib/cgi-bin>
                                SSLOptions +StdEnvVars
                </Directory>
		
		ProxyPreserveHost On
    		ProxyPass / http://127.0.0.1:8080/
    		ProxyPassReverse / http://127.0.0.1:8080/
    
		<Location />
			AuthType Basic
			AuthName "Restricted Content"
			AuthUserFile /etc/apache2/.htpasswd
			Require valid-user
  		 </Location>
		</VirtualHost>
	</IfModule>
	```
	
	sudo vim /etc/apache2/sites-available/000-default.conf (add following)
	
	```
	Redirect "/" "192.168.0.101/"
	```
	
	sudo a2enmod ssl
	
	sudo a2enmod headers
	
	sudo a2ensite default-ssl
	
	sudo a2enconf ssl-params
	
	sudo a2enmod proxy
	
	sudo a2enmod proxy_http
	
	sudo a2enmod proxy_balancer
	
	sudo a2enmod lbmethod_byrequests
	
	sudo apache2ctl configtest
	
	sudo htpasswd -c /etc/apache2/.htpasswd admin
	
	
	sudo systemctl restart apache2
	
	
	git clone https://github.com/timoles/rpi_ws281x.git
	
	git clone https://github.com/timoles/LEDRest.git
	
	cd rpi_ws281x/
	
	scons
	
	cd python/
	
	python ./setup.py build
	
	sudo python ./setup.py install
	
	sudo python examples/strandtest.py
