#########################
# Name: Morgan Visnesky
# File: CountyCSVScraper.py
# Date: 04/04/2020
#########################
# Classes with methods to format data from .csv files filled with county
# information for each state.
# See stateScraperDriver.py for example of how to call classes together

import csv
from CountyStats import *


class CountyCSVScraper(object):
    # takes a list of csv files, and a dictionary mapping those file names
    # to the proper names and spelling of states.
    # uses helper class CountyStats()
    # EX list(): ['PA.csv','NY.csv','NJ.csv']
    # EX dict(): {'PA.csv':'Pennsylvania','NY.csv':'New York','NJ.csv':'New Jersey'}
    def __init__(self, stateCsvList, fileToNameDict):
        self.states = stateCsvList
        self.stateNames = fileToNameDict


    def makeDictOfAllStates(self):
        # creates a new dictionary mapping state name to
        # the dictionary of counties and thier corresponding stats
        self.dataDict = dict()
        for state in self.states:
            stateName = self.stateNames.get(state,'')
            self.dataDict[stateName] = CountyStats(state).runScrape()
        return self.dataDict
