import string

text_file = open('../text/result.txt', 'w')


with open('../text/jap.txt') as f:
   for line in f:
	
       line = line + '!'

       text_file.write(line)

       if 'str' in line:
          break

text_file.close()
