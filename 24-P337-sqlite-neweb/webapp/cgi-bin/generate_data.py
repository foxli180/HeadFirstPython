import cgi
import json
import athletemodel
import YATE
import sys

#athletes = athletemodel.get_from_store()
form_data = cgi.FieldStorage()
athlete_name = form_data['which_athlete'].value
athletes = athletemodel.get_athlete_from_id(athlete_name)
print (athletes, file=sys.stderr)
print(YATE.start_response('application/json'))
#print(json.dumps(athletes[athlete_name].as_dict))
print(json.dumps(athletes))
