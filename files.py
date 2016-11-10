#!/usr/bin/python

import os

with open('words.txt', 'r') as fh:
	for lines in fh: 
		print lines

with open('testfile.txt', 'a') as testfile: 
	testfile.write('line1\nline2\nline3')

with open('testfile.txt', 'r') as fh:
        for lines in fh:
                print lines

