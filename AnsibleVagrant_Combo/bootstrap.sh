#!/bin/sh

# Bootstrapping steps. Here we create needed directories on the guest
mkdir -p ~/.ssh
mkdir -p ~/.ansible
mkdir -p ~/.config
mkdir -p ~/.config/openstack

sudo apt-get update
sudo apt-get install -y python3-pip
sudo python3 -m pip install --upgrade pip setuptools wheel
sudo -H pip3 install --upgrade ansible
sudo -H pip3 install --ignore-installed PyYAML
sudo python3 -m pip install --upgrade openstacksdk
ansible-galaxy collection install openstack.cloud

