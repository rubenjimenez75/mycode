#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

def main():
    """ Run-time code"""
    #create a small string
    lilstring = "Alta3 Research offers classes on Python coding"
    newlist = lilstring.split(" ") # this returns a list
    print(newlist)

    #create  list of strings
    myiplist = ["192", "168", "0", "12"]
    #set singleip as the result of joining the list myiplist around the "."
    singleip = ".".join(myiplist)
    #display single ip
    print(singleip)

    #call our main function
main()


