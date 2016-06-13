"""
	author: Sakthi Saravanakumar P
	Description: Print the List
"""

def print_list(mylist):
    """ Print the Python List """
    for each_item in mylist:
        if isinstance(each_item, list):
            print_list(each_item)
        else:
            print(each_item)


def printv2(mylist):
    """ Improved Version of Print list """
    printf("The V2 Function is under developing")
