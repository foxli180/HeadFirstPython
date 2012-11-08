import cgi
import json
import athletemodel
import YATE

athletes = athletemodel.get_from_store()
form_data = cgi.FieldStorage()
athlete_name = form_data['which_athlete'].value
print(YATE.start_response('application/json'))
print(json.dumps(athletes[athlete_name].as_dict))
