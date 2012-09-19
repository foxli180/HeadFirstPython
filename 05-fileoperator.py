import os


if os.path.exists('sketch1.txt'): #使用if 来对文件是否存在进行逻辑判断
     data = open ('sketch1.txt')

     for each_line in data:
          if each_line.find(':')>0:
               (role,line_spoken) = each_line.split(':',1)
               print(role ,end ='')
               print(' said: ',end ='')
               print(line_spoken,end='')
          else:
               print (each_line,end='')
     data.close()
else:
     print('Data file is missing!')

print('\n------------------------------------')#使用try来尝试文件是否存在

try:
     data = open ('sketch.txt')
     for each_line in data:
          try:
               (role,line_spoken) = each_line.split(':',1)
               print(role ,end ='')
               print(' said: ',end ='')
               print(line_spoken,end='')
          except ValueError:
               pass
     data.close()

except IOError:
     print ('Data file is missing!')
     
          

print('\n------------------------------------')
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
     try: # try to split each_line, if get exception print the whole line
          (role, line_spoken) = each_line.split (':',1)
          print (role ,end='')
          print (' said: ', end='')
          print (line_spoken, end='')
     except:
          #pass # pass: you can pass the exception
          print (each_line, end='')


data.close()
