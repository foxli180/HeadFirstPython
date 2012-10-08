class Athlete:
     def __init__(self,a_name,a_dob=None,a_times=[]):
          self.name = a_name
          self.dob= a_dob
          self.times = a_times

sarah = Athlete('Sarah Sweeney','2002-6-17',['2:58','2.58','1.56'])
print(type(sarah))
print (sarah.name)
