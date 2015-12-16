#!/bin/sh

read -p "Please put the user :" user1
read -p "Please put the old password :" oldpw1
read -p "Please put the new password :" newpw1
cat hosts | while read line
do
ip=$line
CMD1="echo HOSTNAME:$ip"
content="$(curl -k -i -u ${user1}:${oldpw1} -X PUT https://${ip}/api/authentication/users/${user1}?newpassword=${newpw1})"
content2=$(echo "$content" | grep "Password changed successfully for user")
content3=$(echo "$content" | grep "Unable")
content4=$(echo "$content" | grep "Authentication Failed")
echo $(date +%Y/%m/%d:%H:%M:%S) "$ip" "$content"  >> log_full.txt
if [ -n "$content2"  ]; then
	echo $(date +%Y/%m/%d:%H:%M:%S) "$ip" "$content2" >> log.txt
fi
if [ -n "$content3"  ]; then
	echo $(date +%Y/%m/%d:%H:%M:%S) "$ip" "$content3" >> log_error.txt
fi
if [ -n "$content4"  ]; then
	echo $(date +%Y/%m/%d:%H:%M:%S) "$ip" "$content4" >> log_error.txt
fi
done

