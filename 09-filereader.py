try:
    with open('man_data0.txt') as mdf:
        print(mdf.readline())
except IOError as err:
    print('file error: '+str(err))
