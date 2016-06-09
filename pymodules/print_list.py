"""
	author: Sakthi Saravanakumar P
	Description: Print the List
"""
def print_list(list):
    """ Print the Python List """
    for each_item in list:
        if isinstance(list,list):
            print_list(list)
         else:
             print each_item
