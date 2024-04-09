#!/usr/bin/env bash
############SERVER CONFIG SCRIPT###################

apt-get update -y
apt-get install nginx -y

service nginx start

#prepare serving directory

#remove default root
rm -rf /var/www


#############SITE CONFIGURATION ##########################
#remove default config sites -- sites available directory
rm -rf /etc/nginx/sites-available

#root directory preparation
mkdir -p /data; mkdir -p /data/web_static
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases
mkdir -p /data/web_static/releases/test

#test file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

#remove symlink if exist
rm -rf /data/web_static/current
#create symlink to shared version
ln -s /data/web_static/releases/test/ /data/web_static/current


#config string
echo "#===nginx config file==
#----------------------------
user x230;
worker_processes auto;
pid /run/nginx.pid;
error_log /var/log/nginx/error.log;

events {
	worker_connections 768;
	# multi_accept on;
}

http {

	#server
	server {
		#listen on port 80 all ip addresses
		listen 80 default_server;
		#ipv6 all
		listen [::]:80 default_server;

		#access log file
		access_log /var/log/nginx/access.log;
		#add header servicing server in server farm
		add_header X-Served_By \$hostname;
		location /hbnb_static {
			alias /data/web_static/current;
		}
	}
}
" > /etc/nginx/nginx.conf

#give nginx directories to user/ non root
chown -R x230 /data
chown -R x230 /etc/nginx

service nginx restart
