from nester import print_lol
try:
    with open('man_data3.txt') as mdf:
        for each_line in mdf:
            print(each_line,end='')
except IOError as err:
    print('file error: '+str(err))

print('\n')

try:
    
    with open('sarah2.txt') as mdf:
        data=mdf.readlines()
        print(data)
except IOError as err:
    print('file error: '+str(err))
