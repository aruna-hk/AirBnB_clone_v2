#!/usr/bin/env bash
#install nginx
#setup server directories

apt-get update -y
apt-get install nginx -y

#server configuration
#configure listening port /etc/nginx/sites-available/default file

#directories and file setup
mkdir -p /data/; #root web directory
mkdir -p /data/web_static; #static web pages directory
mkdir -p /data/web_static/shared; #shared directory --pracexp
mkdir -p /data/web_static/releases; #released for production
mkdir -p /data/web_static/releases/test; # test for directory
#test file
echo "text file " > /data/web_static/releases/test/index.html

#create symlink to test directory
rm -f /data/web_static/current;
ln -s /data/web_static/releases/test /data/web_static/current

#changing owner of data folder to ubuntu
chown -R hk:hk /data

#remove nginx default serving folder
rm -rf /var/www

#server config file content
echo "#server config file
#listen port 80 all ip addresses -- http requests
server {
	#port
	listen 80 default_server;
	server_name _;

	#header setup
	add_header X-Served-y \$hostname;

	#location block to be served

	location /hbnb_static {
		alias /data/web_static/current/;
	}
}" > /etc/nginx/sites-available/default

#write config file

service nginx restart
