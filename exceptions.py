# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 20:24:13 2019

@author: JW-Ellis
"""

pipeDiameter = 6.625
pipeLength = 9




def plineRelease():
    release = input("Has the pipeline experienced a release greater than 1,000 barrels within the previous five years? Answer with y/n: ")
    if release == "y":
        return True
    elif release == "n": 
        return False
    else:
        print("Answer with only y or n")
        print(plineRelease())


def exception(pipeDiameter, pipeLength):
""" 
The function will take pipeline length and diameter to determine
if it meets exception 194.101(b)(1).

"""
    if (pipeDiameter <= 6.625) or (pipeLength < 10):

        
        
        

