def sanitize(time_string): #序列化得到的无规则数据,将其格式化为 mins.secs 的格式
     if '-' in time_string:
          splitter = '-'
     elif ':' in time_string:
          splitter = ':'
     else:
          return(time_string)
     (mins,secs)=time_string.split(splitter)
     return(mins+'.'+secs)

def load_from_file(filename): #读取文件的一行(这个文件只有一行,多行咋办)
     try:
          with open (filename) as f:
               data = f.readline()
               templ = data.strip().split(',')
               return {
                    'Name':templ.pop(0),
                    'DOB':templ.pop(0),
                    'Times':str(sorted(set(sanitize(t) for t in templ))[0:3])
                    }
     except IOError as err:
          print('File Error: '+str(err))
          return (None)

sarah = load_from_file('sarah2.txt')

#sarah_data = {}
#(sarah_data['Name'],sarah_data['DOB']) = (sarah.pop(0),sarah.pop(0))
#sarah_data['Time'] = sarah
#print(sarah['Name']+"'s fastest times are: "+
#      str(sorted(set([sanitize(t) for t in sarah['Times']]))[0:3]))
print(sarah['Name']+"'s fastest times are: "+sarah['Times'])
