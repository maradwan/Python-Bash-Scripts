#!/bin/sh
read -p "Please Enter OLD enable Password :" old_enable
read -p "Please Enter OLD root Password (again) :" old_root
while true
do
    read -p "Please Enter NEW enable Password: " new_enable
    echo
    read -p "Please Enter NEW enable Password (again): " new_enable2
    echo
    [ "$new_enable" = "$new_enable2" ] && break
    echo "Please try again"
done
while true
do
    read -p "Please Enter NEW root Password: " new_root
    echo
    read -p "Please Enter NEW root Password (again): " new_root2
    echo
    [ "$new_root" = "$new_root2" ] && break
    echo "Please try again"
done
echo "Please wait"
cat hosts | while read line
do
HOST=$line
CMD1="echo HOSTNAME:$HOST"
./100.sh $HOST $old_enable $old_root $new_enable $new_root > ./logs/$HOST.$(date +%F.%T).log &
done
sleep 60
grep -l "No route" ./logs/* | xargs -I % mv % ./logs/error/
grep -l "Permission denied" ./logs/* | xargs -I % mv % ./logs/permission/
