#!/usr/bin/env python

import csv
import numpy

#toolist = open('TOOs.csv', "rb")
#toolist = csv.reader(toolist)
toolist = numpy.loadtxt('TOOs', skiprows=0)

onDiskList = numpy.loadtxt('onDisk', skiprows=0)

print len(onDiskList)
print len(toolist)


#onDisk =[]

#for item in onDiskList:
#    print item
#item = int(str(item)[2:10])
    #onDisk.append(item)


for i in toolist:
#    if i not in onDisk:
        print "ls "+str(i)[0:8]+"*"
