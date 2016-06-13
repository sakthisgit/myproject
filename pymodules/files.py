data=open('sketch.txt')

for each_line in data:
    print "Each line",each_line.find(':')
    if not each_line.find(':') == -1:
        (role, line_spoken) = each_line.split(':',1)
        print "%s said %s " %(role, line_spoken)

data.close()
