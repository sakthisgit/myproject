"""
	author: Sakthi Saravanakumar P
	Description: Print the List
"""

def print_list(mylist, level=0):
    """ Print the Python List """
    for each_item in mylist:
        if isinstance(each_item, list):
            print_list(each_item,level)
        else:
            for tab_stop in range(level):
                print("\t", end='')
            print(each_item)

