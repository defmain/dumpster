#!/usr/bin/python

def rotate_word(word, distance):
    """ROT13 Jumbler"""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rotator = (ord('a') - len(alphabet)) * " " + alphabet * 3
    rotated_word = ""
    for letter in word.lower():
	if letter not in rotator: 
		print "INVALID: ", letter
	rotated_letter = rotator[ord(letter) + (int(distance) % 26)]
#	rotated_word = rotated_word + x (this line is the same as the line below with the +=)
	rotated_word += rotated_letter 
    return rotated_word 
	
if __name__ == "__main__":

    prompt = "Enter Word: "
    rotate = "Enter Distance: "
    word = raw_input(prompt)
    distance = raw_input(rotate)
    print rotate_word(word, distance)
