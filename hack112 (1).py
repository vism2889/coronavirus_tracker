#########################
# Name: Morgan Visnesky, Christina Zhou, Jenna Miller, Emma Parrella
# File: countyCSVDriver.py
# Date: 04/04/2020
#########################

import math, copy, random

from cmu_112_graphics import *
from PIL import Image
import sys
import NationalStatsScraper
import CountyCSVScraper
import OnePointScraper

#helpers

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

def rgbString(red, green, blue):
    # Don't worry about how this code works yet.
    return "#%02x%02x%02x" % (red, green, blue)

# from: https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def runCovidApp():
    width = 1100
    height = 750
    runApp(width = width, height = height)

def appStarted(app):
    app.postalCodes = getPostalCodes(app)
    app.dots = dotData(app)
    updateData(app)
    app.stat, app.countyData = getData2(app)
    app.menu = False
    app.stateList = getListFromDict(app, app.stateData)
    app.countiesList = []
    for state in app.stateList:
        if state in app.countyData:
            countyList = getListFromDict(app, app.countyData[state])
            app.countiesList.append([state] + countyList)
    app.clickables = []
    app.searchResults = []
    app.statesPic = app.loadImage("USA.gif")
    app.alaskaHawaiiPic = app.scaleImage(app.loadImage("AlaskaHawaii.png"), 1.3)
    app.currentPic = app.loadImage("Alabama.gif")
    app.mode = "USA"
    app.searchBar = False
    app.searchResults = []
    app.searchTerm = ""
    app.county = ""
    app.menuTop = 0
    app.timerDelay = 60 * 1000

#backup plan
def getData2(app):
    fileName="Counties.csv"
    data=readFile(fileName)
    data=data.split("\n")
    data.pop(0)
    countyData={} #{state:county:[cases,deaths,"Unknown"]}
    stateData={} #{state:[cases,deaths,"Unknown"]}
    for line in data:
        line=line.split(",")
        line=line[1:3]+line[4:]
        line[2]=int(line[2])
        line[3]=int(line[3])
        if(line[1] in app.dots):
            #[county,state,cases,deaths]
            if(line[1] not in countyData or line[1] not in stateData):
                countyData[line[1]]=dict()
                countyData[line[1]][line[0]]=[line[2],line[3],"Unknown"]
                stateData[line[1]]=[line[2],line[3],"Unknown"]
            elif(line[0] not in countyData[line[1]]):
                countyData[line[1]][line[0]]=[line[2],line[3],"Unknown"]
                stateData[line[1]]=[stateData[line[1]][0]+line[2],stateData[line[1]][1]+line[3],"Unknown"]
            else:
                changeInCases=line[2]-countyData[line[1]][line[0]][0]
                changeInDeaths=line[3]-countyData[line[1]][line[0]][1]
                countyData[line[1]][line[0]]=[line[2],line[3],"Unknown"]
                stateData[line[1]]=[stateData[line[1]][0]+changeInCases,stateData[line[1]][1]+changeInDeaths,"Unknown"]
    return stateData,countyData


def updateData(app):
    updateNationalData(app)
    updateStateData(app)

def updateNationalData(app):
    app.nationalStats = NationalStatsScraper.NationalStatsScraper()
    app.nationalStats.connect()
    app.natStats = app.nationalStats.usNationalStats()
    app.nationalStats.closeBrowser()

def updateStateData(app):
    app.stateObject = OnePointScraper.OnePointScraper()
    app.stateObject.connect()
    app.stateData = app.stateObject.stateStatsTotals()
    app.stateObject.closeBrowser()
    temp = app.stateData
    app.stateData = {}
    for state in temp:
        if state in app.dots:
            app.stateData[state] = temp[state]


def getData(app):
    #This will eventually return the webscraped data
    stateData={}
    countyData={}
    for state in ["New York","Pennsylvania"]:
        stateData[state],countyData[state]=getTotals(app,state)
    '''
    stateData = {
        #"structure":[cases, deaths, recovered]
        "Alabama": [38,1495,50],
        "Alaska": [875,567,98],
        "Arizona": [444,100,89],
        "Arkansas": [644,666,6],
        "California": [425,26,69],
        "New York": getTotals(app,f"{app.postalCodes['New York']}.csv")[0]
    }

    countyData = {
        "Alabama": {"A":[1,3,4], "B":[3,5,6], "C":[9,2,7]},
        "Alaska": {"E": [4,7,89], "K": [2,5,123]},
        "Arizona":{"D":[3,3,3], "J":[7,8,6]},
        "Arkansas":{"L":[45,6, 23]},
        "California":{"R":[2,3,12], "Oakland":[3,4,16]},
        "New York":{"New York City":[1,2,3]}

    }'''
    return stateData, countyData

def getTotals(app,state):
    fileName=app.postalCodes[state]+".csv"
    data=readFile(fileName)
    data=data.split("\n")
    data.pop(0)
    totals=data.pop().split(",")[1:]
    countyData={}
    for line in data:
        line=line.split(",")
        countyData[line[0]]=line[1:]
    return totals, countyData

def getListFromDict(app, dictionary):
    newList = []
    for key in dictionary:
        newList.append(key)
    newList = sorted(newList)
    return newList

def dotData(app):
    dotData = {
        "Alabama":[788, 470],
        "Alaska":[172, 612],
        "Arizona":[306, 424],
        "Arkansas":[676, 431],
        "California":[172, 336],
        "Colorado":[437, 326],
        "Connecticut":[1012, 226],
        "Delaware":[978, 298],
        "Florida":[902, 562],
        "Georgia":[853, 467],
        "Hawaii":[363, 659],
        "Idaho":[297, 189],
        "Illinois":[729, 306],
        "Indiana":[786, 302],
        "Iowa":[651, 262],
        "Kansas":[564, 349],
        "Kentucky":[807, 360],
        "Louisiana":[679, 524],
        "Maine":[1044, 122],
        "Maryland":[951, 295],
        "Massachusetts":[1022,206],
        "Michigan":[797,222],
        "Minnesota":[631,168],
        "Mississippi":[730,483],
        "Missouri":[671,355],
        "Montana":[391,134],
        "Nebraska":[545,272],
        "Nevada":[235,282],
        "New Hampshire":[1018,177],
        "New Jersey":[990,267],
        "New Mexico":[414,433],
        "New York":[953,203],
        "North Carolina":[920,390],
        "North Dakota":[538,134],
        "Ohio":[842,294],
        "Oklahoma":[583,414],
        "Oregon":[194,165],
        "Pennsylvania":[925,261],
        "Rhode Island":[1032,221],
        "South Carolina":[900,437],
        "South Dakota":[537,204],
        "Tennessee":[793,400],
        "Texas":[536,503],
        "Utah":[328,306],
        "Vermont":[996,168],
        "Virginia":[925, 340],
        "Washington":[230, 87],
        "West Virginia":[882, 327],
        "Wisconsin":[707,198],
        "Wyoming":[412, 230],
    }
    return dotData

def getPostalCodes(app):
    postalCodes = {
        "Alabama": "AL",
        "Alaska":"AK",
        "Arizona":"AZ",
        "Arkansas":"AR",
        "California":"CA",
        "Colorado":"CO",
        "Connecticut":"CT",
        "Delaware": "DE",
        "Florida":"FL",
        "Georgia":"GA",
        "Hawaii":"HI",
        "Idaho":"ID",
        "Illinois":"IL",
        "Indiana":"IN",
        "Iowa":"IA",
        "Kansas":"KS",
        "Kentucky":"KY",
        "Louisiana":"LA",
        "Maine":"ME",
        "Maryland":"MD",
        "Massachusetts":"MA",
        "Michigan":"MI",
        "Minnesota":"MN",
        "Mississippi":"MS",
        "Missouri":"MO",
        "Montana":"MT",
        "Nebraska":"NE",
        "Nevada":"NV",
        "New Hampshire":"NH",
        "New Jersey":"NJ",
        "New Mexico":"NM",
        "New York":"NY",
        "North Carolina":"NC",
        "North Dakota":"ND",
        "Ohio":"OH",
        "Oklahoma":"OK",
        "Oregon":"OR",
        "Pennsylvania":"PA",
        "Rhode Island":"RI",
        "South Carolina":"SC",
        "South Dakota":"SD",
        "Tennessee":"TN",
        "Texas":"TX",
        "Utah":"UT",
        "Vermont":"VT",
        "Virginia":"VA",
        "Washington":"WA",
        "West Virginia":"WV",
        "Wisconsin":"WI",
        "Wyoming":"WY",
    }
    return postalCodes

def mousePressed(app, event):
    x = event.x
    y = event.y
    if 5 <= x and 95 >= x and 5 <= y and 25>=y:
        if app.menu:
            app.menu = False
        else:
            app.menu = True
            menuList = ["USA"]+app.stateList
            makeMenuClickables(app, menuList[app.menuTop:app.menuTop+21])
    if 100 <= x and 190 >= x and 5<= y and 25>= y and app.mode != "USA":
        if app.searchBar == False:
            app.searchBar = True
    if app.menu:
        for elem in app.clickables:
            x1 = elem[1]
            y1 = elem[2]
            x2 = elem[3]
            y2 = elem[4]
            if x1 <= x and x2 >= x and y1 <= y and y2 >= y:
                app.mode = elem[0]
                #app.currentPic=app.loadImage(f"{app.mode}.gif")
                #these next three lines are my attempt at resizing but it fucks up the image quality
                app.currentPic =Image.open(f"{app.mode}.gif")
                app.currentPic=app.currentPic.resize((app.currentPic.width*600//app.currentPic.height,600),Image.ANTIALIAS)
                app.currentPic=ImageTk.PhotoImage(app.currentPic)
                app.menu = False
                app.clickables = []
                app.county=""
    if app.searchBar:
        for elem in app.clickables:
            x1 = elem[1]
            y1 = elem[2]
            x2 = elem[3]
            y2 = elem[4]
            if x1 <= x and x2 >= x and y1 <= y and y2 >= y:
                app.county = elem[0]
                app.searchBar = False
                app.searchTerm = ""
                app.clickables = []

def keyPressed(app, event):
    if (app.searchBar):
        if(event.key.isalpha() and len(event.key)==1):
            app.searchTerm+=event.key
        elif(event.key=="Space"):
            app.searchTerm += " "
        elif(event.key=="Delete"):
            app.searchTerm=app.searchTerm[:-1]
        app.searchResults = []
        stateCounties = getListFromDict(app, app.countyData[app.mode])
        for elem in stateCounties:
            if elem.lower().startswith(app.searchTerm.lower()):
                app.searchResults.append(elem)
        app.searchResults = sorted(app.searchResults)
        makeSearchClickables(app, app.searchResults)
        if app.searchTerm == "":
            app.searchResults = []
    if app.menu:
        if event.key == "Up" and app.menuTop > 0:
            app.menuTop -= 1
            menuList = ["USA"]+app.stateList
            makeMenuClickables(app, menuList[app.menuTop:app.menuTop+21])
        elif event.key == "Down" and app.menuTop < 30:
            app.menuTop += 1
            menuList = ["USA"]+app.stateList
            makeMenuClickables(app, menuList[app.menuTop:app.menuTop+21])


def timerFired(app):
    #updateData(app)
    return 42

def clean(num):
    newNum = ""
    for char in num:
        if char in "123456789.0":
            newNum += char
    return newNum

def makeMenuClickables(app, placeList):
    y1 = 5
    for place in placeList:
        y1+=20
        app.clickables.append([place, 5, y1, 135, y1 + 20])

def makeSearchClickables(app, placeList):
    y1=5
    for place in placeList:
        y1 += 20
        app.clickables.append([place, 140, y1, 330, y1 + 20])

def drawDropDown(app, canvas, placeList):
    y1 = 5
    canvas.create_rectangle(5, 5, 135, 25, fill = "light blue")
    canvas.create_text(7, 15, text = "States", fill = "blue",
        anchor = "w")

    if app.menu == True:
        for place in placeList:
            y1+=20
            canvas.create_rectangle(5,y1,135,y1+20, fill="blue")
            canvas.create_text(7,y1+10,text=place,fill="white",
            anchor = "w")

def drawSearchBarDropDown(app, canvas):
    y1 = 5
    for place in app.searchResults:
        y1+=20
        canvas.create_rectangle(140,y1,330,y1+20, fill="light grey")
        canvas.create_text(142,y1+10,text=place,fill="black",
            anchor = "w")

def drawDots(app, canvas):
    for key in app.dots:
        cx = app.dots[key][0]
        cy = app.dots[key][1]
        r = math.pow(int(clean(app.stateData[key][0])),.35)//2
        fraction = 17 * int(clean(app.stateData[key][1]))/int(clean(app.stateData[key][0]))
        color = rgbString((roundHalfUp(255 * fraction))
                        ,roundHalfUp(255 * (1-fraction)),0)
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = color)

def drawSearchBar(app,canvas):
    canvas.create_rectangle(140,5,330,25,fill="light gray")
    if(app.searchTerm == ""):
        if not app.searchBar:
            canvas.create_text(142,15,text=f"Search Counties in {app.mode}",fill="gray",anchor="w")
    else:
        canvas.create_text(142,15,text=app.searchTerm,fill="black",anchor="w")

def redrawAll(app, canvas):
    #drop down menu
    if app.mode == "USA":

        canvas.create_image(45, 535, image = ImageTk.PhotoImage(app.alaskaHawaiiPic),\
            anchor = "nw")
        canvas.create_image(100, 30, image = ImageTk.PhotoImage(app.statesPic),\
            anchor = "nw")
        drawDots(app, canvas)
        i = 0
        for key in app.natStats:
            i += 20
            canvas.create_text(450, 5 + i, text = f"{key}: {app.natStats[key]}", anchor = "w")
    else:
        canvas.create_image(100,85, image = app.currentPic,
         anchor = "nw")
    if(app.mode!="USA"):
        drawSearchBar(app, canvas)
        if app.searchBar == True:
            drawSearchBarDropDown(app, canvas)
    if app.county != "":
        canvas.create_text(550, 15, text = f"{app.county}, {app.mode}")
        canvas.create_text(550, 35, text = f"Cases: {app.countyData[app.mode][app.county][0]}")
        canvas.create_text(550, 55, text = f"Deaths: {app.countyData[app.mode][app.county][1]}")
        canvas.create_text(550, 75, text = f"Recovered: {app.countyData[app.mode][app.county][2]}")
    elif app.mode != "USA":
        canvas.create_text(550,15, text = f"{app.mode}")
        canvas.create_text(550,35, text = f"Cases: {app.stateData[app.mode][0]}")
        canvas.create_text(550,55, text = f"Deaths: {app.stateData[app.mode][1]}")
        canvas.create_text(550, 75, text = f"Death rate: {app.stateData[app.mode][2]}")
        canvas.create_text(550,95, text = f"Recovered: {app.stateData[app.mode][3]}")
    menuList = ["USA"]+app.stateList
    drawDropDown(app, canvas, menuList[app.menuTop:app.menuTop + 21])

def main():
    runCovidApp()

if __name__ == '__main__':
    main()
