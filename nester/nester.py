"""
This can print all the intem in the list or in the list of list
"""
def print_lol(the_list,level=0):
     """
     method 2, printtab is a bool value, if it is ture,in each sub list, it will print
     a TAB 
     """
     for each_item in the_list:
          if (isinstance(each_item,list)):
               print_lol(each_item,level+1)
          else:
               for tab_stop in range (level):
                    print('\t',end='')
               print(each_item)

      
