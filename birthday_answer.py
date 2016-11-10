#!/usr/bin/python

import random

def has_duplicates(the_list):

    for i in range(len(the_list)):
        if the_list.index(the_list[i]) != i: 
	    return True
    return False

if __name__ == "__main__":

    same_birthday_counter = 0 
    trials = 1000

    for trial in range(trials):
        birthdays = []
        for b in range(23): 
	    birthdays.append(random.randint(1, 365))
        
	if has_duplicates(birthdays):
	    same_birthday_counter += 1

    print ("%d sets of 23 people has the same birthday in %d trials" %
	      (same_birthday_counter, trials))
