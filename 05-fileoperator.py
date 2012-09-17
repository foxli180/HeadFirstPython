import os

print (os.getcwd())
data = open('sketch.txt.txt')
print (data.readline(), end='')
data.seek(0)
for each_line in data:
     print(each_line, end='')
data.close()
