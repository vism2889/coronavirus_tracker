# coronavirus_tracker

Coronavirus_tracker took first place in the 15-112 hackathon during the spring semester of 2020!  

The app was developed in collaboration with my partners Christina Zhou, Jenna Miller, and Emma Parrella over the span of 24 hours. All collaboration was done remotely via Discord, as it took place during the beginning of the pandemic. The 'Hack 112' event was an activity put together by the staff and TA's of CMU's 15-112: Fundamentals of Programming and Computer Science course.  The guidelines were basically to design and implement something interesting in the alotted time frame.  Submissions were judged based on correct use of the python langage, interactivity, difficulty of concepts implemented, and originality.  

![Demo from hack-112, spring 2020](https://github.com/vism2889/coronavirus_tracker/blob/master/hackathon_demo.gif)


### Overview of the application:

 - Scrapes coronavirus statistics for every county in the United States.
 - Custom interactive GUI made with the cmu-graphics library.


 ## README for scrapers:


 1. Install splinter driver '$ sudo pip install splinter'
 2. Install chromedriver.
 - Version of chromedriver must match current version of Chrome.
 - check if chromedriver is already installed by entering:
 - `cd /usr/local/bin` then `ls`, which should print all files and directories in that location. See if chromedriver is in there.
 - If not already installed Download ChromeDriver here: https://chromedriver.chromium.org/downloads
 - ChromeDriver must live in this directory: '/usr/local/bin'
 - After downloading in a terminal window enter the following commands:
 **On Mac OS:**
 -`cd Downloads`
 -`mv -chromedriver /usr/local/bin`

 ## Included files
 dependencies.py - All required modules
 NationalStatsScraper.py - Grabs national totals
 OnePointScraper.py - Grabs state totals
 CountyCSVScraper.py - Grabs county totals from csv files


 ## Citations
 - https://stackoverflow.com/questions/49788257/what-is-default-location-of-chromedriver-and-for-installing-chrome-on-windows
 - https://splinter.readthedocs.io/en/latest/index.html
 - https://chromedriver.chromium.org/downloads
 - https://stackedit.io - for README.md

 ## README for graphics:
 Files needed: download all the files in the drive. This should include:
 1. All state pictures which are formatted as [State Name].gif
 2. USA.gif
 3. AlaskaHawaii.png
 4. cmu_112_graphics.py
 5. Counties.csv

 Instructions on how to operate:
 It starts at the United States screen. This will show the national data. The circles are sized in representation of the number of cases in the state with larger circles meaning more cases. The color represents the death rate where green is  a lower rate and red is higher.
 Click on the blue States button to reveal a dropdown menu of the states in alphabetical order. Use up and down arrow keys to scroll the list. Click on the state you would like to view.
 Once on a state, it will show the state's overall data and a picture of the state with its counties. There is a search bar where you can click on it and then type letters and a dropdown will appear with county names beginning with the letter or letters typed in. Clicking on one of these counties will give the county's data. If a county does not show up, then there is no data for that county.
 Note: It may take a moment to update. Thank you for your patience.
