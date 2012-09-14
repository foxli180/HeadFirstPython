"""
This can print all the intem in the list or in the list of list
"""
def print_lol(the_list,indent=False,level=0):
     """
     method 2, printtab is a bool value, if it is ture,in each sub list, it will print
     a TAB
     the_list: type:list
     indent: if this true, will print tab
     level: 缩进的起始量,负数的话不缩进
     """
     for each_item in the_list:
          if (isinstance(each_item,list)):
               print_lol(each_item,indent,level+1)
          else:
               if indent:
                    for tab_stop in range (level):
                         print('\t',end='')
               print(each_item)

      
