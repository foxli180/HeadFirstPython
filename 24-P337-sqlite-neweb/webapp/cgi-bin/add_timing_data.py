import cgi
import os
import time
import sys
import YATE
import sqlite3

print (YATE.start_response('text/plain'))
addr = os.environ['REMOTE_ADDR']
host = os.environ['REMOTE_HOST']
method = os.environ['REQUEST_METHOD']
cur_time = time.asctime(time.localtime())

print (host+", "+addr+", "+cur_time+": "+method, file=sys.stderr)

form_data = cgi.FieldStorage()
the_id = form_data['Athlete'].value
the_time = form_data['Time'].value

connection = sqlite3.connect('coachdata.sqlite')
cursor = connection.cursor()
cursor.execute("INSERT INTO timing_data (athlete_id,value) VALUES (?,?)",
               (the_id, the_time))
"""
for each_form_item in form.keys():
     print (each_form_item + '->' + form[each_form_item].value,
            end=' ', file=sys.stderr)
print (file = sys.stderr) #在标准错误输出上换行
"""
connection.commit()
connection.close()
print ('OK.')


