import cgi
import cgitb #开启浏览器追踪 cig 信息

import athletemodel
import YATE

cgitb.enable()#cgitb #开启浏览器追踪 cig 信息
athletes = athletemodel.get_from_store()#从pickle获取信息
form_data = cgi.FieldStorage()#获取请求的form的内容
athlete_name = form_data['which_athlete'].value#从内容中得到请求控件name 为:which_athlete的值
                         
print(YATE.start_response())
print(YATE.include_header('Timing Data'))
print(YATE.header('Althlete:'+athlete_name+' ,DOB: '
                  +athletes[athlete_name].dob+'.'))
print(YATE.para('The top times for this athlete are:'))
print(YATE.u_list(athletes[athlete_name].top3))#这里需要在top3方法那加入@property将类方法表现得像个类属性
print(YATE.include_footer({'Home':'/index.html',
                           'Select another athlete':'generate_list.py'}))
