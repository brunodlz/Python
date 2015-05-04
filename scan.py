#!/usr/bin/python

import socket
import sys

def main():
 if len(sys.argv)<=3:
  print "use: ./portscanner.py example.com 1 1024"
  sys.exit()
 else: 
  remoteServer = str(sys.argv[1])
  remoteServerIP = socket.gethostbyname(remoteServer)

  in_port = int(sys.argv[2])
  out_port = int(sys.argv[3])

  try:
   print "please wait..."
   for port in range(in_port,out_port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    result = sock.connect_ex((remoteServerIP,port))
    if result == 0:
     print "\033[1m port {}:\t Open".format(port)
    sock.close()

  except KeyboardInterrupt:
   print "you pressed ctrl+c"
   sys.exit()

  except socket.gaierror:
   print "hostname could not be resolved.exiting"
   sys.exit()

  except socket.error:
   print "couldn't connect to server"
   sys.exit()

main()
