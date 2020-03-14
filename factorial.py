#!/usr/bin/python3
# -*- coding: utf-8 -*-
#testing a new branch mynewbranch
"""This module calculates a factorial based on user input."""
__author__ = "George"
__version__ = "1.4"


myinput = int(input("Enter your number: "))
answer = myinput

while (myinput != 1):
    myinput -= 1
    answer = answer * myinput

print("Your factorial is: ", answer)


