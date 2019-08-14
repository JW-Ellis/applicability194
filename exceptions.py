# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 20:24:13 2019

@author: JW-Ellis
"""

pipeDiameter = 6.625
pipeLength = 9




def plineRelease():
    release = input("Has the pipeline experienced a release greater than 1,000\
                    barrels within the previous five years? Answer with y/n: ")
    if release == "y":
        return True
    elif release == "n": 
        return False
    else:
        print("Answer with only y or n")
        print(plineRelease())

def plineReportable():
    reportable = input("Has the pipeline experienced two or more reportable\
                       releases, as defined in 195.50, within the previous five years? Answer with y/n: ")
    if reportable == "y":
        return True
    elif reportable == "n": 
        return False
    else:
        print("Answer with only y or n")
        print(plineReportable())

def plineWeld():
    weld = input("Does the pipeline contain any electric resistance welded pipe manufactured\
                 prior to 1970 and if so, does it operate at a maximum operating pressure establisehd under 195.406 that\
                 corresponds to a stress level greater than 50 percent of the specified minimum yield strenght of the pipe. Answer with y/n: ")
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

def segmentRelease():
    release = input("Has the line segment experienced a release greater than 1,000 barrels within the previous 5 years? Answer with y/n: ")
    if release == "y":
        return True
    elif release == "n":
        return False
    else:
        print("Answer with only y or n")
        print(segmentRelease())
            
def segmentReportable():
    reportable = input("Has the line segment experienced two or more reportable releases, as defined in 195.50, within the previous five years? Answer with y/n: ")
    if reportable == "y":
        return True
    elif reportable == "n":
        return False
    else:
        print("Answer with only y or n")
        print(segmentReportable())

def segmentElectric():
    electric = input("Does the line segment contain any electric resistance welded pipe, manufactured \
                    prior to 1970, operate at a maximum operating pressure established under 195.406 that corresponds\
                    to a stress level greater than 50 percent of the specified minimum yield strength? Answer with y/n: ")
    if electric == "y":
        return True
    elif electric == "n":
        return False
    else:
        print("Answer with only y or n")
        print(segmentElectric())

def segmentWater():
    water = input("Is the line segment located within a 5 mile radius of potentially affected public\
                  drinking water intakes and could reasonably be expected to reach public\
                  drinking water intakes? Answer with y/n: ")
    if water == "y":
        return True
    elif water == "n":
        return False
    else:
        print("Answer with only y or n")
        print(segmentWater())
        
def segmentEnvironment():
    environment = input("Is the line segment located within a 1 mile radius of potentially\
                        affected environmentally sensitive areas, and could reasonably be expected\
                        to reach these areas? Answer with y/n: ")
    if environment == "y":
        return True
    elif environment == "n":
        return False
    else:
        print("Answer with only y or n")
        print(segmentEnvironment())


"""
Take pipe diameter and semgnet length to determine if system 
causes significant and substantial harm under 194.103(c)
"""

def significantSubstantialHarm(pipeDiameter, segmentLength):
    if (pipeDiameter > 6.625) or (segmentLength > 10):
        if segmentRelease() == True:
            return True
        elif segmentReportable() == True:
            return True
        elif segmentElectric() == True:
            return True
        elif segmentWater() == True:
            return True
        elif segmentEnvironment() == True:
            return True
        else:
            return False
    else:
        return False
#    
    
    
    
    
    
    
    
    
    