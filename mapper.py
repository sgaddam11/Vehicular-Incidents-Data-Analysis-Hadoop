#!/usr/bin/env python
import sys
words=[]
for line in sys.stdin:
    line = line.strip()
    if(( "DATE")  not in line ):
       words = line.split(",")
       words = words[-5:]
      # print words
      # print ":%d"%len(words)
    for word in words:
                 if len(word) >0 and word[0] !="\"" and word[-1] !="\"":
                      print '%s\t%s'%(word,1)
