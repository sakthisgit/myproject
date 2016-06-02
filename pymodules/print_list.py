""" This Module prints the List """

def print_list(mylist):
    """ Print the Python List """
    for each_item in mylist:
        if isinstance(each_item, list):
            print_list(each_item)
        else:
            print each_item
