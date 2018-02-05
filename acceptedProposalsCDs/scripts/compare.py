#!/usr/bin/env python

# compare.py compares the list of proposals returned from a DB query
# and compares the list to what's been successfully copied. Ideally, 
# there will be no differences but in an ideal world, I would have 
# all ten fingers on my left hand so my right hand could just be a 
# fist for punching. We can't always get what we want.

# This will be incorporated into gather.py which does the copying 


import os
import sys

write_directory = "/data/doh/wyman/CDs/acceptedProposalsCDs/cycle17/CD/proposals/"
DB_list_file = "/data/doh/wyman/CDs/acceptedProposalsCDs/scripts/cycle17axafocat.txt"


copied_proposals = os.listdir(write_directory)
copied_list = []

for proposal in copied_proposals:
    copied_list.append(proposal[0:8])
  
DB_list = [line.strip(' \t\n\r') for line in open(DB_list_file, 'r')]

print "Proposals returned from DB Query but not found/copied: "
for val in DB_list:
    if val not in copied_list:
        print val


                                                                    
                                                                 

