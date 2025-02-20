#!/usr/bin/env bash
#script that sets up your web servers for the deployment of web_static.

sudo apt-get update
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
echo "Holberton's cool" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current 
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '35i\\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-enabled/default
sudo service nginx restart

