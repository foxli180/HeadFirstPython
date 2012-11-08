#创建ath_list页面,这里有运动员的列表
import athletemodel
import YATE
import glob #可以获取文件列表

data_files = glob.glob("data/*.txt")#获取data 目录下的所有txt
athletes = athletemodel.put_to_store(data_files)#将txt的内容存入 pickle,并返回字典

print(YATE.start_response())
print(YATE.include_header('List of Athletes')) #web的头
print(YATE.start_form('generate_timing_data.py'))#需要进一步处理表单的表单,即submit后处理请求的页面
print(YATE.para('Select an Athlete!'))

for each_ath in athletes:
     print(YATE.radio_button('which_athlete',athletes[each_ath].name))#which_athlete是radiobutton的name属性,
print(YATE.end_form('Select'))
print(YATE.include_footer({'Home':'/index.html'}))
      
      
