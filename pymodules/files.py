import os

os.chdir('/mnt/workspace/Myworkspace/myproject/pymodules')

try:
    data=open('sketch.txt')

    for each_line in data:
        try:
            if not each_line.find(':') == -1:
                (role, line_spoken) = each_line.split(':',1)
                print "%s said %s " %(role, line_spoken)
        except ValueError:
            print 'Value has not been processed'
            
    data.close()
except IOError:
    print 'File Not Found'
