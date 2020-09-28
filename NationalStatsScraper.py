#########################
# Name: Morgan Visnesky
# File: NationalStatsScraper.py
# Date: 04/03/2020
#########################
# returns this dictionary (values subject to change):
# {
#   'National Coronavirus Cases': '277,161',
#   'National Deaths': '7,392',
#   'National Recovered': '12,283'
# }
from dependencies import *

class NationalStatsScraper(object):

    # connects to site
    def connect(self):
        # select browser, chrome headless
        #version must match current actual chrome version
        self.browser = Browser('chrome', headless=True)
        self.page = "https://www.worldometers.info/coronavirus/country/us/"
        self.browser.visit(self.page)
        time.sleep(1)


    def usNationalStats(self):
        # grab nation wide info for united states
        resultDict = dict()
        self.countTitles = ['National Coronavirus Cases', 'National Deaths', 'National Recovered']
        self.countryCounts = []
        self.xpath= '//*[contains(@class,"maincounter-number")]'
        self.pathSearch = self.browser.find_by_xpath(self.xpath)
        for search in self.pathSearch:
            search = str(search.text.encode('utf8'))[2:-1]
            self.countryCounts.append(search)
        for i in range(len(self.countryCounts)):
            #count = count.text.encode('utf8')
            resultDict[self.countTitles[i]] = self.countryCounts[i]
            #cprint(self.countTitles[i] + ' ' + self.countryCounts[i], 'red', 'on_white')
        return resultDict

    def closeBrowser(self):
        # only call this method if you are done using splinter's Browser
        # be sure to close it otherwise the process will stay open in the
        # background and take up CPU
        self.browser.quit()
