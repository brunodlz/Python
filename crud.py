#!/usr/bin/python
# by v0id

# -*- coding: utf-8 -*-

"""
  _____                _           ______      _   _                 
 /  __ \              | |          | ___ \    | | | |                
 | /  \/_ __ _   _  __| |  ______  | |_/ /   _| |_| |__   ___  _ __  
 | |   | '__| | | |/ _` | |______| |  __/ | | | __| '_ \ / _ \| '_ \ 
 | \__/\ |  | |_| | (_| |          | |  | |_| | |_| | | | (_) | | | |
  \____/_|   \__,_|\__,_|          \_|   \__, |\__|_| |_|\___/|_| |_|
                                          __/ |                 
                                         |___/      
"""

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
 print "bye ... "
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
 print "Successfully"

###############################################

def update():
 name = raw_input("qual nome trocar: ")
 alterName = raw_input("por: ")

 cursor.execute('UPDATE USERS SET NAME = ? WHERE NAME = ?',[alterName,name]);
 conn.commit()
 print "Sucessfully"

##############################################

def delete():
 id = raw_input("deletar por qual id: ")

 cursor.execute('DELETE FROM USERS WHERE ID = ?',id)
 conn.commit()
 print "Successfully"

#############################################

def listView():
 list = cursor.execute("SELECT * FROM USERS");
 
 print "+------------------------+"
 for row in list:
  print "id   : ",row[0]
  print "name : ",row[1]
  print "email: ",row[2]
  print "age  : ",row[3],"\n"
 print "+------------------------+"

############################################

def createTable():
 conn.execute('''CREATE TABLE IF NOT EXISTS USERS
 		(ID    INTEGER  PRIMARY KEY,
		 NAME  TEXT             NOT NULL,
		 EMAIL TEXT             NOT NULL,
		 AGE   INT              NOT NULL);''')

##########################################

clear()
print banner()
createTable()

op = int(raw_input("Option: "))
validate_option(op)

while op!=0:
 if op==1:
  insert()
  clear()
  print banner()
 elif op==2:
  listView()
  update()
 elif op==3:
  listView()
  delete()
 elif op==4:
  listView()
 
 op = int(raw_input("Option: "))
 validate_option(op)
 clear()
 print banner()

exit()
