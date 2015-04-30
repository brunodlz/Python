#!/usr/bin/python
# by v0id

###################################################

import os
import re
import sys
import time
import sqlite3

###################################################

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

###################################################

def banner():
 print "+------------------------+"
 print "|     CRUD - by v0id     |"
 print "+------------------------+"
 print "| 1 - INSERT             |"
 print "| 2 - UPDATE             |"
 print "| 3 - DELETE             |"
 print "| 4 - LIST VIEW          |"
 print "| 0 - EXIT               |"
 print "+------------------------+\n"

###################################################

def clear():
 os.system('cls' if os.name == 'nt' else 'clear')

##################################################

def validate_option(op):
 if op > 4 or op < 0:
  print "value incorrect"
  exit()

#################################################

def exit():
 print "bye ... :( "
 time.sleep(2)
 conn.close()
 sys.exit()

################################################

def insert():
 name = raw_input("whats your name: ")
 email = raw_input("whats your email: ")
 age = int(raw_input("whats old age: "))

 cursor.execute('INSERT INTO USERS (NAME,EMAIL,AGE) VALUES (?,?,?)',(name,email,age));

 conn.commit()

 print "records created successfully\n"

###############################################

def update():
 print "update now"

##############################################

def delete():
 print "delete now"

#############################################

def listView():
 list = cursor.execute("SELECT * FROM USERS");
 
 print "+------------------------+"
 for row in list:
  print "name : ",row[1]
  print "email: ",row[2]
  print "age  : ",row[3],"\n"
 print "+------------------------+"
 print "operation done sucessfully"
 conn.close()
############################################

def createTable():
 conn.execute('''CREATE TABLE IF NOT EXISTS USERS
 		(ID    INTEGER  PRIMARY KEY,
		 NAME  TEXT             NOT NULL,
		 EMAIL TEXT             NOT NULL,
		 AGE   INT              NOT NULL);''')
 print "table created successfully"

##########################################

clear()
print banner()

createTable()

op = int(raw_input("Option: "))
validate_option(op)

while op!=0:
 if op&1:
  insert()
 elif op&2:
  update()
 elif op&3:
  delete()
 elif op&4:
  listView()

 print banner()
 op = int(raw_input("Option: "))
 validate_option(op)
 clear()
 print banner()

exit()
