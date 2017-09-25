#!/usr/bin/env python
# -*- coding: utf-8 -*- 

text_file = open('../text/result.txt', 'w')


with open('../text/jap.txt') as f:
   for line in f:
      
       if line.isspace():
		continue

       line = line.replace('（','')
       line = line.replace('）','')
       line = line.replace(' (','')
       line = line.replace(') ','')
       line = line.replace('(','')
       line = line.replace(')','')
	
       line = line + '.'


       text_file.write(line)

       if 'str' in line:
          break

text_file.close()
