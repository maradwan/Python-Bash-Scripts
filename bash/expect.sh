#!/usr/bin/expect -f
set timeout 60
set HOST [lrange $argv 0 0]
spawn ssh admin@$HOST
expect "password:" 
 send "abc123\r" 
expect ">" 
 send "enable\r" 
expect "Password:" 
 send "123abc\r" 
expect "#" 
 send "config terminal\r" 
 send "exit\r"
interact
exit
