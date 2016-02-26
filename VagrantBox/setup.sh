#!/usr/bin/env bash

apt-get update
apt-get install -y apache2 python-pip git
git clone https://github.com/2ajoyce/ThePetEmporium.git
if ! [ -L /var/www ]; then
  rm -rf /var/www
  ln -fs /vagrant /var/www
fi