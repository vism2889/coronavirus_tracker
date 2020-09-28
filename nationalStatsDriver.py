#########################
# Name: Morgan Visnesky
# File: NationalStatsDriver.py
# Date: 04/03/2020
#########################
# Driver script to test classes associated with coronavirus project

from dependencies import *
from NationalStatsScraper import *



# test national stats
test = NationalStatsScraper()
test.connect()
dictionary = test.usNationalStats()
test.closeBrowser()
#
# cprint(dictionary, 'red', 'on_white')
print(dictionary)
