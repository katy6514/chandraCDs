#!/usr/bin/env python

#you might have to run these two commands first

# >source /soft/SYBASE_OCS15.5/SYBASE.csh
# >setenv LC_ALL C


import numpy
import os
from subprocess import call

#-------------------------#
#   set write path
#-------------------------#
write_path = "/data/doh/kguardado/accepted/"

#-------------------------#
#   set source directory
#-------------------------#
source_directory = "/data/rpc/prop/rps/upload/CHANDRA/merged/"



#--------------------------------------------------#
#   DO THE THING /cycle17/CD/proposals/
#--------------------------------------------------#

proposal_list = raw_input("List?: ")

#fix this next year! skipping 4 rows at the bottom??
proposals = numpy.genfromtxt(proposal_list, skip_header=2, skip_footer=2) 

cycle_num = str(proposals[0])[0:2]

write_directory = write_path+cycle_num+"/CD/proposals/"

directory_exists = os.path.isdir(write_directory)
if directory_exists != True:
    call(["mkdir", write_directory])


for proposal in proposals:
    copy_path = source_directory+(str(proposal)[0:8])+"*"
    ##call(["cp "+copy_path+" "+write_directory]) #figure this out next year
    os.system("cp "+copy_path+" "+write_directory)


