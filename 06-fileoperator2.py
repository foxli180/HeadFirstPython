#1.Create a list: man
#2.Create a list: other
#3.Delete unnessary blank in line_spoken
#4.Add line_spoken to diff list via roles
#5.Print man and other

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

try: # 将 man 和other 分别写入文件
    out_man = open('man_data.txt','w')
    out_other = open('other_data.txt','w')
    print(man,file=out_man)
    print(other,file=out_other) #注意,如果这里出现了异常的话,文件无法正常关闭!引入 finally
    #out_man.close() 
    #out_other.close()
except IOError:
    print('Can not write to file')

finally:#确保无论发生了什么都关文件,无论是否有运行时错误
    out_man.close()
    out_other.close()

    
            
            
