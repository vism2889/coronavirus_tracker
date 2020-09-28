#########################
# Name: Morgan Visnesky
# File: OnePointScraper.py
# Date: 04/04/2020
#########################
# grabs state totals
# select browser, chrome headless version must match current actual chrome version
from dependencies import *

'''
returns formatted data like so:
stateData = {
        #"structure":[confirmed, deaths, fatality rate, recovered]
        "Alabama": ['38','10','10%','50'],
        "Alaska": ['875','297','25%','98'],
        "Arizona": ['444','100','20%','89']
    }
'''


class OnePointScraper(object):
    def connect(self):
        #print('Loading Coronavirus Data Source......')
        self.browser = Browser('chrome', headless=True)
        self.page = "https://coronavirus.1point3acres.com/"
        self.browser.visit(self.page)
        time.sleep(1)

    def stateStatsTotals(self):
        # grab nation wide info and last update time
        #print('Grabbing state stats......')
        self.stateCounts = []
        self.xpath= '//*[@class="jsx-1703765630"]'
        self.pathSearch = self.browser.find_by_xpath(self.xpath)

        for search in self.pathSearch:
            search = str(search.text.encode('utf8'))[2:-1]
            self.stateCounts.append(search)

        stats = self.stateCounts[12:-6]
        formattedStats = [stats[x:x+8] for x in range(0, len(stats),8)]
        formattedList = []

        for i in range(len(formattedStats)-6):
            temp = formattedStats[i][2:]
            temp[0] = temp[0].strip()
            for i in range(len(temp)):
                if temp[i].startswith('+'):
                    temp[i] = temp[i].split('n')[1]
            temp.pop(1)
            formattedList.append(temp)

        returnDict = dict()
        for stat in formattedList:
            returnDict[stat[0]] = stat[1:]

        return (returnDict)

    def closeBrowser(self):
        self.browser.quit()

    '''
    def countyStats(self):
        # broken right now, doesnt grab correct data
        # grab nation wide info and last update time
        self.countTitles = ['Coronavirus Cases', 'Deaths', 'Recovered']
        self.countryCounts = []
        self.xpath= '//*[@class="jsx-1703765630 row"]'
        self.pathSearch = self.browser.find_by_xpath(self.xpath)
        print(self.pathSearch)
        for search in self.pathSearch:

            search = str(search.text.encode('utf8'))#[2:-1]
            print(search)
            self.countryCounts.append(search)
        for i in range(len(self.countryCounts)):
            #count = count.text.encode('utf8')
            cprint(self.countryCounts[i], 'red', 'on_white')

    '''
