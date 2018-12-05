* ssh pi@192.168.0.101
* pi:raspberry

	sudo apt update
	sudo apt install apache2
	sudo apt install vim
	
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
                ServerName ------------IPIPIPIPIPIPIPIP--------

                DocumentRoot /var/www/html

                ErrorLog ${APACHE_LOG_DIR}/error.log
                CustomLog ${APACHE_LOG_DIR}/access.log combined

                SSLEngine on

                SSLCertificateFile      /etc/ssl/certs/apache-selfsigned.crt
                SSLCertificateKeyFile /etc/ssl/private/apache-selfsigned.key

                <FilesMatch "\.(cgi|shtml|phtml|php)$">
                                SSLOptions +StdEnvVars
                </FilesMatch>
                <Directory /usr/lib/cgi-bin>
                                SSLOptions +StdEnvVars
                </Directory>

                BrowserMatch "MSIE [2-6]" \
                               nokeepalive ssl-unclean-shutdown \
                               downgrade-1.0 force-response-1.0

		</VirtualHost>
	</IfModule>
	```
	
	sudo vim /etc/apache2/sites-available/000-default.conf
	
	```
	Redirect "/" "https://your_domain_or_IP/"
	```
	
	sudo a2enmod ssl
	sudo a2enmod headers
	sudo a2ensite default-ssl
	sudo a2enconf ssl-params
	sudo apache2ctl configtest
	sudo systemctl restart apache2