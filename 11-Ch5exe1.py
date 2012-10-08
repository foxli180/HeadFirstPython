def sanitize(time_string): #将不同的时间分隔符统一为: .
     if ':' in time_string:
          splitter = ':'
     elif '-' in time_string:
          splitter = '-'
     else:
          return time_string
     (misn,secs) = time_string.split(splitter)

     return(misn+'.'+secs)


def uniquelist(old_list): #其实用set() 也可以解决问题
     unique_list = []
     for each_data in old_list:
          if each_data not in unique_list:
               unique_list.append(each_data)
     return unique_list

def load_from_file(filename):
     try:
          with open(filename) as input_file:
               data = input_file.readline()
               return(data.strip().split(','))
     except IOError as err:
          print('File Error: '+str(err))
          return (None)


james = []
julie = []
mikey = []
sarah = []
try:
     with open('james.txt') as james_file:
          data = james_file.readline()
          james = data.strip().split(',')
except IOError as err:
     print('File Error: '+str(err))
try:
     with open('julie.txt') as julie_file:
          data = julie_file.readline()
          julie = data.strip().split(',')
except IOError as err:
     print('File Error: '+str(err))

try:
     with open('mikey.txt') as mikey_file:
          data = mikey_file.readline()
          mikey = data.strip().split(',')
except IOError as err:
     print('File Error: '+str(err))

try:
     with open('sarah.txt') as sarah_file:
          data = sarah_file.readline()
          sarah = data.strip().split(',')
except IOError as err:
     print('File Error: '+str(err))


clean_james = []
clean_julie = []
clean_mikey = []
clean_sarah = []

#for each_t in james:
#     clean_james.append(sanitize(each_t))

clean_james = sorted([sanitize(each_t) for each_t in james])

#for each_t in julie:
#     clean_julie.append(sanitize(each_t))

clean_julie = sorted([sanitize(each_t) for each_t in julie])

#for each_t in mikey:
#     clean_mikey.append(sanitize(each_t))

clean_mikey = sorted([sanitize(each_t) for each_t in mikey])

#for each_t in sarah:
#     clean_sarah.append(sanitize(each_t))

clean_sarah = sorted([sanitize(each_t) for each_t in sarah])
     
#print (sorted(james))
#print (sorted(julie))
#print (sorted(mikey))
#print (sorted(sarah))
#print (sorted(clean_james))
#print (sorted(clean_julie))
#print (sorted(clean_mikey))
#print (sorted(clean_sarah))

print(clean_james)
print(clean_julie)
print(clean_mikey)
print(clean_sarah)



unique_james = []
unique_julie = []
unique_mikey = []
unique_sarah = []

unique_james = uniquelist(clean_james)
print(unique_james[0:3])


clean_james = sorted(set([sanitize(each_t) for each_t in james]))[0:3]
clean_julie = sorted(set([sanitize(each_t) for each_t in julie]))[0:3]
clean_mikey = sorted(set([sanitize(each_t) for each_t in mikey]))[0:3]
clean_sarah = sorted(set([sanitize(each_t) for each_t in sarah]))[0:3]

print(clean_james)
print(clean_julie)
print(clean_mikey)
print(clean_sarah)
