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
write_directory = raw_input("Write Directory?: ")


#-------------------------#
#   load list
#-------------------------#
proposal_list = raw_input("List? (include path if necessary): ")

#-------------------------#
#   set source directory
#-------------------------#
source_directory = "/data/rpc/prop/rps/upload/CHANDRA/merged/"


#fix this next year! skipping 4 rows at the bottom??
proposals = numpy.genfromtxt(proposal_list) 


for proposal in proposals:
    copy_path = source_directory+(str(proposal)[0:8])+"*"
    ##call(["cp "+copy_path+" "+write_directory]) #figure this out next year
    os.system("cp "+copy_path+" "+write_directory)
