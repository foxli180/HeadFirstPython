import cgi
import cgitb #开启浏览器追踪 cig 信息

import athletemodel
import YATE

cgitb.enable()#cgitb #开启浏览器追踪 cig 信息
#athletes = athletemodel.get_from_store()#从pickle获取信息
form_data = cgi.FieldStorage()#获取请求的form的内容
#athlete_name = form_data['which_athlete'].value#从内容中得到请求控件name 为:which_athlete的值
athlete_id = form_data['which_athlete'].value # radio 在 yate.py 里重写了
athletes = athletemodel.get_athlete_from_id(athlete_id)

                         
print(YATE.start_response())
print(YATE.include_header("NUAC's Timing Data"))
print(YATE.header('Althlete:'+athletes['Name']+' ,DOB: '
                  +athletes['DOB']+'.'))
print(YATE.para('The top times for this athlete are:'))
print(YATE.u_list(athletes['top3']))

print(YATE.para("The entire set of timing data is:"+str(athletes['data'])+
                " (duplicates removed)."))

print(YATE.include_footer({'Home':'/index.html',
                           'Select another athlete':'generate_list.py'}))
