#!/usr/bin/python
# Objective: Parse logs, accept input and search for strings. Match IDs and sort by date. 
# AnonID  Query   QueryTime       ItemRank        ClickURLimport os

import os

path = "/home/tilt/python_projects/aol-searcher/AOL-user-ct-collection"
f = os.listdir( path )

prompt = "Enter Word: "
search = raw_input(prompt)
c_var = 30
c = 0

for file in f:
    with open("%s/%s" % (path, file), 'r') as x:
        searchlines = x.readlines()
    for i, line in enumerate(searchlines):
        if search in line:
	    c += 1
            if c == c_var:
                raw_input() 
                c = 0
            print line 
	
            #for l in searchlines[i:i+3]: print l,
            #print
	    
