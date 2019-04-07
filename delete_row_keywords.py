'''
import re

list = []
matchPattern = re.compile(r'INVALID PARAMETER')
file = open('movies.xml','r')
while 1:
    line = file.readline()
    if not line:
        print("error")
        break
    elif matchPattern.search(line):
        pass
    else:
        list.append(line)
file.close()
file = open(r'target.xml', 'w')
for i in list:
    file.write(i)
file.close()
'''
file = open('movies.xml','r')
lines = file.readlines()
list=[]
for lines in lines:
   if "xml" in lines:
     print(lines)
   else:
       list.append(lines)
file.close()
file = open(r'target.xml', 'w')
for i in list:
    file.write(i)
file.close()