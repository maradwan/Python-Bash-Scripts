#!/usr/bin/python
import MySQLdb
import os
def cls(): os.system('clear')
cls()
print"-----------------Welcome To Address Book----------------"
def menu():
        print "1) Add New User"
        print "2) Find User"
        print "3) Update User"
        print "4) Delete User"
        print "5) Quit from Address Book"
        return input ("Choose Your Option: ")

loop =1
choice = 0
while loop == 1:
        choice = menu()
        if choice ==1:
                cls()
                var1 = raw_input("Please Enter Your Name ")
                var2 = raw_input("Please Enter Your Phone Number ")
                var3 = raw_input("Please Enter Your Email ")
                db = MySQLdb.connect("localhost","root","","users")
                cursor = db.cursor()
                sql = "INSERT INTO address(name,phone,email) VALUES ('%s','%s','%s') " % (var1,var2,var3)
                print "Name:" ,var1 ,"Phone:", var2 ,"Email:", var3
                try:
                        cursor.execute(sql)
                        db.commit()
                except:

                        db.rollback()
                db.close()
        elif choice ==2:
                cls()
                print"-----------------Find Address Book----------------"
                var1 = raw_input("Please Enter the email ")
                db = MySQLdb.connect("localhost","root","","users")
                cursor = db.cursor()
                sql = "SELECT * from address where email = '%s'" % var1

                try:
                        cursor.execute(sql)
                        results = cursor.fetchall()
                        for row in results:
                                name = row[0]
                                phone = row[1]
                                email = row[2]
                                print "Name=%s,Phone=%s,Email=%s" % (name,phone,email)
                except:
                        print " failed"
                        db.close()
        elif choice ==5:
                loop=0
print " Thank You"
