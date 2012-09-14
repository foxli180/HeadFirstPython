"""
This can print all the intem in the list or in the list of list
"""
def print_lol(the_list):
     """
     Input a list 
     """
     for each_item in the_list:
          if (isinstance(each_item,list)):
               print_lol(each_item) #这个递归函数真不赖
          else:
               print(each_item)
