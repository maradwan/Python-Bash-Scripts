#!/bin/bash

#Fix network config so that it has proper hostame and IP.

HOSTNAME=`grep $(ifconfig | grep 'inet addr:' | head -1 | sed 's/inet addr:/ /' | awk '{ print $1}') /install/centos6/config_files/hosts | awk '{ print $2}'`

echo "
NETWORKING=yes
HOSTNAME=$HOSTNAME
GATEWAY=172.16.1.1
NISDOMAIN=nis.example.eg" > /etc/sysconfig/network

echo "Post installation script complete."
exit 0
