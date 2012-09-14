movies = ['The Holy Grail','The Life of Brian','The meaning of life1']
print (movies[1])
print (movies)
print (len(movies))
# print string contains " or ' 单引号和双引号的区别
print ("Hello 'world")
print ('Hello "world')


cast = ['Clesese','Palin','Jones','Idle']
print (cast)
#appped will add a word at the end of the list
cast.append('Gmail')
print (cast)
#pop() will pop the last word
print (cast.pop())
print (cast)
#pop(0) will pop the 1st word
print (cast.pop(0))
print (cast)
#extend can add a new list
cast2=['Yahoo','Chapman']
cast.extend(cast2)
print (cast)

cast.insert (0,'Fox')
print (cast)

#Excise 1 insert years after the movie name
movies = ['The Holy Grail','The Life of Brian','The meaning of life']
print (movies)
movies.insert(1,1975)
movies.insert(3,1979)# after insert 1975, the length of movies changed
movies.append(1983)
print (movies)
#Excise 1 create new list
movies2 = ['The Holy Grail', 1975, 'The Life of Brian', 1979, 'The meaning of life', 1983]
print(movies2)

# deal with the data in the list

# 1. print each var position [x]
fav_movies = ['The Holy Grail','The Life of Brian']
print(fav_movies[0])
print(fav_movies[1])

# 2. print iteration via for
for each_flick in fav_movies:
     print (each_flick)

# 3. print via while
count = 0
while count < len(fav_movies):
     print (fav_movies[count])
     count = count +1

#List in List
print ("-----------------new line-----------------")
movies = [
     'The Holy Grail', 1975, 'Terry Jones&Terry Gilliam', 91,
     ['Graham Chapman',
      ['Michael Palin', 'John Cleese','Terry Gilliam','Eric Idle','Terry Jones']]]
print (movies[4][1][3]) #shows Eric Idle
print (movies)
for each_movie in movies:
     print(each_movie)#这里只能打印第一层的列表
print ("-----------------isinstance()-----------------")
print(isinstance(movies,list))
for each_item in movies:
     if isinstance(each_item,list):
         for each_subitem in each_item: #添加语句后可以打印到第二层
          print(each_subitem)
     else:
          print(each_item)
print ("-----------------new line-----------------")
for each_item in movies:
     if isinstance(each_item, list):
          for each_subitem in each_item:
               if isinstance(each_subitem,list):  #继续添加语句可以打印到第三层 
                    for each_ssubitem in each_subitem:
                         print(each_ssubitem)
               else:
                    print(each_subitem)
     else:
          print (each_item)
                    
print ("-----------------new line-----------------")
#重复的代码用函数代替
def print_lol(the_list):
     for each_item in the_list:
          if (isinstance(each_item,list)):
               print_lol(each_item) #这个递归函数真不赖
          else:
               print(each_item)

print_lol(movies)
         
          


