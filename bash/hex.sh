#!/bin/bash

echo "enter hostname"
read HOST
if [ -z "$HOST" ]; then
        echo "No host specified, try again"
        exit
fi

ADDR=`cat /etc/hosts | grep $HOST | tr ":" " " | awk '{ print $1 }'`
echo $ADDR

   LIST=`echo ${ADDR} | tr "." " "`
   OUT=""

   for QUAD in ${LIST}
   do
      HEX=`echo ${QUAD} | awk '{ printf ("%.2X", $1) }'`
      OUT="${OUT}${HEX}"
   done

        echo " Hex is ${OUT}"


cp /install/centos6/tftp_install_full /tftpboot/ibm/pxelinux.cfg/$OUT
chmod 777 /tftpboot/pxelinux.cfg/$OUT
