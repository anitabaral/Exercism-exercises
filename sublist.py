"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3



def sublist(list_one, list_two):
    first = str(list_one)[1: -1]
    second = str(list_two)[1: -1]

    if (first == second):
        return EQUAL
    elif(first in second):
        return SUBLIST
    elif(second in first):
        return SUPERLIST
    else:
        return UNEQUAL
