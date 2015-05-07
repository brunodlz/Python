#!/usr/bin/python

# -*- coding: utf-8 -*-

#linux: grep 'ba' < text.txt

import sys
import re

banner = '''
+==========================+
|   Just Another 'Filter'  |
+==========================+
	  by v0id 
'''

usage = '''
	use: ./filter.py "ba" < text.txt
        '''

print banner

if len(sys.argv) <= 1:
 print usage
else :
 pattern = sys.argv[1]
 regexp = re.compile(pattern)
 
 print "Found:\n"

 for line in sys.stdin:
  result = regexp.search(line)
  if result:
   sys.stdout.write(line)
  
 print "\n"
