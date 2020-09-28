#########################
# Name: Morgan Visnesky
# File: OnePointDriver.py
# Date: 04/04/2020
#########################
# test script to demonstrate function calls to OnePointDriver class

from OnePointScraper import *


test = OnePointScraper()
test.connect()
stateStats = test.stateStatsTotals()
test.closeBrowser()
print(stateStats)
