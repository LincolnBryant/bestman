#!/usr/bin/env python
#
#   bestman callout adler32
#
#   This reads or sets the extended attribute user.adler32 for files in Lustre
#
#   use:
#
#   adler32.py 
#
#   returns an error if the path is a directory

adlercom = '/usr/local/bin/calc_adler32.py'

import sys
if len(sys.argv)==1: 
        sys.stderr.write('No input path provided\n')
        sys.exit(1)
#
#   get the path of the file to get adler32 of
#
path = sys.argv[1]

#
#    first see if adler32 is stored as an attribute
#
import commands

com1 = 'getfattr --only-values --absolute-names -n user.adler32 '+path
status,output = commands.getstatusoutput(com1)

if status==0 and len(output)>0 and not ' ' in output:
        sys.stdout.write(output+'\n')
        sys.exit(0)
else:
        #-- compute adler32
        com2 = adlercom+' '+path

        status,adler32 = commands.getstatusoutput(com2)

        if status==0 and len(adler32)>0:
                #  attempt to save the answer as an attribute
                com3 = 'setfattr -n user.adler32 -v '+adler32+' '+path
                status,output = commands.getstatusoutput(com3)
                if not status==0: sys.stderr.write("error setting adler32 for "+path+'\n')
                sys.stdout.write(adler32+'\n')
                sys.exit(0)
        else:
                sys.stderr.write("error computing adler32 for "+path+'sys.argv,status,adler32:'+str(sys.argv)+'|'+str(status)+' | '+adler32+'\n')
                sys.exit(1)
