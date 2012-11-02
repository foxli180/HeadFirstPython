class AthleteList(list): #新的AthleteList 类,继承了原有的list类,包含了原list的所有方法 append,extend
     def __init__(self,a_name,a_dob=None,a_times=[]):
          list.__init__([])
          self.name = a_name
          self.dob = a_dob
          self.extend(a_times)
     @property
     def top3(self):
          return(sorted(set([sanitize(t) for t in self]))[0:3])
     @property
     def as_dict(self):
          return({'Name':self.name,
                  'DOB':self.dob,
                  'Top3':self.top3})
          
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
               return (Athlete(templ.pop(0),templ.pop(0),templ))#返回一个Athlete对象,这里已经pop了两次,所以返回值里只有times了
     except IOError as err:
          print('File Error: '+str(err))
          return (None)

