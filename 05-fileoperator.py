import os

print (os.getcwd())
data = open('sketch.txt')
print (data.readline(), end='')
data.seek(0) #Go back to the 1st line
for each_line in data:
     print(each_line, end='')

print('\n------------------------------------')
data.seek(0) #Go back to the 1st line
for each_line in data:
     (role, line_spoken) = each_line.split(':')
     print (role ,end='')
     print (' said: ', end='')
     print (line_spoken, end='')

     
data.close()
