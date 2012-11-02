import android
import json
import time

from urllib.parse import urlencode
from urllib.request import urlopen

#app 的所有消息
hello_msg    = "Welcome to Coach Kelly's Timing App"
list_title   = 'Here is your list of athletes'
quit_msg     = "Quitting Coach Kelly's App."
web_server   = 'http://192.168.1.180:8082'
get_name_cgi = '/cgi-bin/generate_name.py'

get_data_cgi = '/cgi-bin/generate_data.py'


#send to server 取一个web地址(url) 和一些可选数据(post_data)
#它向web 服务器发送一份web请求(urlopen)
#web响应返回给调用者(return)
def send_to_server(url, post_data=None):
     if post_data:
          page = urlopen(url, urlencode(post_data))
     else:
          page = urlopen(url)
     return(page.read().decode("utf8"))

app = android.Android()

def status_update(msg, how_long = 2 ):
     app.makeToast(msg)
     time.sleep(how_long)

status_update(hello_msg)
athlete_names = sorted (json.loads(send_to_server(web_server + get_name_cgi)))
app.dialogCreateAlert(list_title)
app.dialogSetSingleChoiceItems(athlete_names)
app.dialogSetPositiveButtonText('Select')
app.dialogSetNegativeButtonText('Quit')
app.dialogShow()
resp = app.dialogGetResponse().result


if resp['which'] in ('positive'):
     selected_athlete = athlete_names[selected_athlete]
     athlete = json.loads(send_to_server(web_server + get_data_cgi,{'which_athlete':which_athlete}))
     athlete_title = athlete['Name'] + '(' +athlete['DOB'] + '), top3 times'
     app.dialogCreateAlert(athlete_title)
     app.dialogSetItems(athlete['Top3'])
     app.dialogSetPositiveButtonText('OK')
     resp = app.dialogGetResponse().result
     
status_update(quit_msg)
