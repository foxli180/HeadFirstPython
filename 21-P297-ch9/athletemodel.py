import pickle
import json# 加载 json 模块
from athletelist import AthleteList


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


def get_names_from_store():
     athletes = get_from_store()
     response = [athletes[each_ath].name for each_ath in athletes]
#从数据中抽取选手名作为一个列表
     return (response)



"""
测试代码
files = ['sarah2.txt','james2.txt','mikey2.txt','julie2.txt']
data = put_to_store(files)#data 是一个字典
print(data)
for each_ath in data:
     #print(data[each_ath].name + ' ' +data[each_ath].dob )
     print(data[each_ath].name)
data = get_names_from_store()
print(data)
"""
