#1.Create a list: man
#2.Create a list: other
#3.Delete unnessary blank in line_spoken
#4.Add line_spoken to diff list via roles
#5.Print man and other

man = []
other = []
try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role,line_spoken) = each_line.split(':',1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The data file is missing!')
print(man)
print('\n')
print(other)
        
    
            
            
