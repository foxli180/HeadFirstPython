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
     if each_line.find(':') > 0:
          (role, line_spoken) = each_line.split(':',1)
          print (role ,end='')
          print (' said: ', end='')
          print (line_spoken, end='')
     else:
          print (each_line, end='')

     
print('\n------------------------------------')
data.seek(0)

for each_line in data:
     try:
          (role, line_spoken) = each_line.split (':',1)
          print (role ,end='')
          print (' said: ', end='')
          print (line_spoken, end='')
     except:
          #pass
          print (each_line, end='')


data.close()
