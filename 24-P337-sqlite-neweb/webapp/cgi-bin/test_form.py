import YATE
import cgitb

cgitb.enable()
print (YATE.start_response('text/html'))
print (YATE.do_form('add_timing_data.py',['TimeValue'],text='Send'))
