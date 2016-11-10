#!/usr/bin/env python

guess = raw_input('Guess a number, 1-10: ')

if guess.isdigit() == False:
  print 'A number, dummy.'
elif guess == "2":
  print 'YOU WIN!!!!'
else:
  print 'Try Again'
