import athletemodel
import YATE
import json
import cgitb #开启浏览器追踪 cig 信息

cgitb.enable()#cgitb #开启浏览器追踪 cig 信息
ath_names = athletemodel.get_names_from_store()
print(YATE.start_response('application/json'))
print(json.dumps(sorted(ath_names)))
