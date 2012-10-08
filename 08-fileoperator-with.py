#2.Create a list: other
#3.Delete unnessary blank in line_spoken
#4.Add line_spoken to diff list via roles
#5.Print man and other
from nester import print_lol
man = []
other = []
try:
    data = open('sketch.txt') #打开文件
    for each_line in data:#遍历文件
        try:
            (role,line_spoken) = each_line.split(':',1) #将每行按照:分成2部分
            line_spoken = line_spoken.strip()#去除多余空格
            if role == 'Man':#如果role是man, 把line_spken 压入man list
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()#关闭I/O
except IOError:
    print('The data file is missing!')

try:
    with open('man_data3.txt','w') as out_man:
        print_lol(man,fh=out_man)
    with open('other_data3.txt','w') as out_other:
        print_lol(other,fh=out_other)
except IOError as err:
    print('File Error: '+str(err))


try:
    with open('man_data3.txt','w') as out_man,open('other_data3.txt','w') as out_other:
        print_lol(man, fh=out_man)
        print_lol(other,fh=out_other)
except IOError as err:
    print('File Error: '+str(err))    
