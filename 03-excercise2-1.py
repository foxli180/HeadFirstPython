import nester
cast = ['Palin','Cleese','Idle','Jone','Gilliam']
try:
     with open ('test.txt','w') as out1:
          nester.print_lol(cast,fh = out1)
except IOError as err:
     print('Error: '+str(err))
