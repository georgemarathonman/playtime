#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""This module compares two words to see if they are an anangram."""
__author__ = "George"

word1 = "a"
word2 = "aa"
matchcount = 0

while ( len(word1) != len(word2) ):
    word1 = list(input("Enter word one: "))
    word2 = list(input("Enter word two: "))
    if ( len(word1) != len(word2) ):
        print("Try again, both words must have an equal number of characters!")

#countx = county = len(word1)

for countx in range(len(word1)):
    print("countx = ", countx)
    print("word1 countx = ",word1[countx])
    for county in range(len(word1)):
        print("county = ", county)
        print("word2 county = ",word2[county])
        if (word1[countx] == word2[county]):
            print("we have a match with at: ", word1[countx])
            matchcount += 1
            print("matchcount = ", matchcount)
            print("1 ",word1[countx])
            print("2 ",word2[county])
            print("purposefully mismatch match so they are not reconsidered")
            word1[countx] = "+"
            word2[county] = "="
            print("1 ",word1[countx])
            print("2 ",word2[county])


if (matchcount == 3) + (matchcount == len(word1)):
    print("We have an anagram!")
else:
    print("No anagram was detected.")
print("matchcount = ", matchcount)


