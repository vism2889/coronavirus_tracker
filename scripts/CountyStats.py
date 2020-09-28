#########################
# Name: Morgan Visnesky
# File: CountyStats.py
# Date: 04/04/2020
#########################
# Classes with methods to format data from .csv files filled with county
# information for each state.
# See stateScraperDriver.py for example of how to call classes together

# TODO: if value is initial .csv is empty, change to 'unknown'

import csv

class CountyStats(object):
    def __init__(self, stateName):
        self.stateName = stateName
        self.stateStats = []

    def grabData(self, stateName):
        # formatted for csv that has title row at beginning
        # and total row at last entry, must be formatted in that fashion
        # cols are: No Cases, No Deaths, No Recovered
        with open(stateName, newline='') as state:
            self.readCSV = csv.reader(state, delimiter=',')
            for row in self.readCSV:
                self.stateStats.append(row)

    def statsToDict(self, statList):
        self.countyDict= dict()
        stats = self.stateStats[1:-1]
        for row in stats:
            self.countyDict[row[0]] = (row[1],row[2],row[3])
        return self.countyDict

    def runScrape(self):
        self.grabData(self.stateName)
        return (self.statsToDict(self.stateStats))
