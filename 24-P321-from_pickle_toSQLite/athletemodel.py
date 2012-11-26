#import pickle
import sqlite3

from athletelist import AthleteList

db_name = 'coachdata.sqlite'


def get_names_from_store():
     connection = sqlites3.connect(db_name)
     cursor = connection.cursor()
     results = cursor.execute("""SELECT name FROM athletes""")
     response = [row[0] for row in results.fetchall()]
     connection.close()
     return (response)

def get_athlete_from_id(athlete_id):
     connection = sqlite3.connect(db_name)
     cursor = conenction.cursor()
     results = cursor.execute("""SELECT name, dob FROM athletes WHERE id=?""",
                              (athlete_id,))
     (name, dob) = results.fetchone()
     results = cursor.execute("""SELECT value FROM timing_data WHERE athlete_id=?""",
                              (athlete_id,))
     response = {   'Name':   name,
                    'DOB':    dob,
                    'data':   data,
                    'top3':   data[0:3]}
     connection.close()
     return(response)



def get_coach_data(filename): #从文件中获取数据

     try:
          with open (filename) as f:
               data = f.readline()
               templ = data.strip().split(',')
               return (AthleteList(templ.pop(0),templ.pop(0),templ))
     except IOError as ioerr:
          print ('File Error: ' + str(ioerr))
          return (None)
     

def put_to_store(file_list):

     all_athletes = {}
     for each_f in file_list:
          ath = get_coach_data(each_f) #这里ath 返回的 athletelist 的对象(athletelist 是一个list)
          #all_athletes['Name'] = ath.name
          #all_athletes['DOB'] = ath.dob
          #all_athletes['Times']= ath
          all_athletes[ath.name] = ath #将ath name 作为键,将ath作为值
          
     try:
          with open ('athletes.pickle','wb') as ath_f:
               pickle.dump (all_athletes,ath_f)
     except IOError as ioerr:
          print('File Error(put_to_store): '+str(ioerr))
     return (all_athletes)

def get_from_store():

     all_athletes = {}
     try:
          with open ('athletes.pickle','rb') as ath_f:
               all_athletes = pickle.load(ath_f)
     except IOError as ioerr:
          print('File Error(get_from_store): '+str(ioerr))
          
     return (all_athletes)

"""
测试代码
files = ['sarah2.txt','james2.txt','mikey2.txt','julie2.txt']
data = put_to_store(files)#data 是一个字典
print(data)
for each_ath in data:
     #print(data[each_ath].name + ' ' +data[each_ath].dob )
     print(data[each_ath].name)
"""
