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

def plineReportable():
    reportable = input("Has the pipeline experienced two or more reportable releases, as defined in 195.50, within the previous five years? Answer with y/n: ")
    if reportable == "y":
        return True
    elif reportable == "n": 
        return False
    else:
        print("Answer with only y or n")
        print(plineReportable())

def plineWeld():
    weld = input("Does the pipeline contain any electric resistance welded pipe manufactured prior to 1970 and if so, does it operate at a maximum operating pressure establisehd under 195.406 that corresponds to a stress level greater than 50 percent of the specified minimum yield strenght of the pipe. Answer with y/n: ")
    if weld == "y":
        return True
    elif weld == "n": 
        return False
    else:
        print("Answer with only y or n")
        print(plineWeld())   

def plineHca():
    hca = input("Is the pipeline within 5 miles of public drinking water intakes or within 1 mile of environmentally senstitive areas? Answer with y/n: ")
    if hca == "y":
        return True
    elif hca == "n": 
        return False
    else:
        print("Answer with only y or n")
        print(plineHca())
        
def exception(pipeDiameter, pipeLength):
    """
This function will take pipeline diameter and pipeline length to determine Exception under 194.101(b).

    """
    if (pipeDiameter <= 6.625) or (pipeLength < 10):
        if plineRelease() == True:
            return False
        elif plineReportable() == True:
            return False
        elif plineWeld() == True:
            return False
        elif plineHca() == True:
            return False
        else:
            return True
    else:
        return False

print(exception(4, 5))