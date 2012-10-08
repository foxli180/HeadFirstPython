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
               return (data.strip().split(','))
     except IOError as err:
          print('File Error: '+str(err))
          return (None)

james = load_from_file('james.txt')
julie = load_from_file('julie.txt')
mikey = load_from_file('mikey.txt')
sarah = load_from_file('sarah.txt')

#列表推导: 先将james 里的每个t格式化为统一的时间,再使用set()剔除重复值,再使用sort进行排序
#使用[0:3]获得列表的前三位
print(sorted(set([sanitize(t) for t in james]))[0:3])
print(sorted(set([sanitize(t) for t in julie]))[0:3])
print(sorted(set([sanitize(t) for t in mikey]))[0:3])
print(sorted(set([sanitize(t) for t in sarah]))[0:3])
