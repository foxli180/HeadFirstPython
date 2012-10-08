def sanitize(time_string):
     if ':' in time_string:
          splitter = ':'
     elif '-' in time_string:
          splitter = '-'
     else:
          return time_string
     (misn,secs) = time_string.split(splitter)

     return(misn+'.'+secs)
     
     
