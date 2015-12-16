#!/usr/bin/expect -f
set timeout 60
set HOST [lindex $argv 0 ]
set OLDENABLE [lindex $argv 1]
set OLDROOT [lindex $argv 2]
set NEWENABLE [lindex $argv 3]
set NEWROOT [lindex $argv 4]
spawn ssh admin@$HOST
sleep 2
expect "yes/no" {
    send "yes\r"
    expect "*?assword" { send "$OLDROOT\r" }
    } "*?password" { send "$OLDROOT\r" }
expect ">" { send "enable\r" }
expect "Password:" { send "$OLDENABLE\r" }
expect "#" { send "config terminal\r" }
sleep 2
expect "#" { send "system user admin $NEWROOT\r" }
sleep 2
expect "#" { send "enable secret $NEWENABLE\r" }
sleep 2
expect "#" { send "end\r" }
sleep 2
expect "#" { send "write\r" }
sleep 2
expect "#" { send "end\r" }
expect ">" { send "exit\r" }
interact
