import os

"""
    1) Open a Files and Read the contenets
    2) Split the lines based on special characters and print
"""
def fileread():
    try:
        data=open('sketch.txt')
        for each_line in data:
            try:
                if not each_line.find(':') == -1:
                    (role, line_spoken) = each_line.split(':',1)
                    print "%s said %s " %(role, line_spoken)
            except ValueError:
                print 'Value has not been processed'
                
        
    except IOError:
        print 'File Not Found'
    finally:
        data.close()

"""
    1) Create a Empty list Man and others
    2) Add a line of code to remove unwanted whitespace from the
        line-spoken variable
    3) Print the list on the screen
"""
def filewrite():
    man=[]
    other=[]
    try:
        data=open('sketch.txt')
        for each_line in data:
            try:
                if not each_line.find(':') == -1:
                    (role, line_spoken) = each_line.split(':',1)
                    line_spoken = line_spoken.strip()
                    if role == 'Man':
                        man.append(line_spoken)
                    elif role == 'Other Man':
                        other.append(line_spoken)
            except ValueError:
                print 'Value Parsing  Error'
        data.close()         
    except IOError:
        print 'File Not Found'
    try:
        outfile=open('output.txt','w')        
	for i in (man+other):
	 print>>outfile, i

    except IOError:
        print "Error"
    finally:
        outfile.close()



"""

        Test the program

"""
if __name__== '__main__':
    os.chdir('/mnt/workspace/Myworkspace/myproject/pymodules')
    filewrite()
