#!/usr/bin/python

def most_frequent(string):
    """ word sorting thing"""

    freq = []
    location = 0

    for letter in string:
        if string.index(letter) == location:
            freq += [(string.count(letter), letter)]
        print freq
        location += 1

    freq.sort()
    print freq
    freq.reverse()
    print freq
    return tuple(freq)

if __name__ == "__main__":
    freq_tuples = most_frequent(raw_input("enter word: "))
    for freq,char in freq_tuples:
        print "[%s]" % char,
