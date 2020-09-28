#########################
# Name: Morgan Visnesky
# File: countyCSVDriver.py
# Date: 04/04/2020
#########################
# Driver script for stateScraper.py
# see code below for example method call

from CountyCSVScraper import *

# these will be changed to include all 50 states
stateFileNames = ['PA.csv', 'NY.csv', 'NJ.csv']
stateFileNameToName = {'PA.csv': 'Pennsylvania',\
                    'NY.csv': 'New York',\
                    'NJ.csv': 'New Jersey'}


finalDict = CountyCSVScraper(stateFileNames, stateFileNameToName).makeDictOfAllStates()

print(finalDict)
