import urllib2
import json
import datetime
import time


dateStart = datetime.datetime(2013, 1,1)
#timeDelay = 178
timekeeper = 0
#I needed it till the end of the year,
#you can do it for a selection of days with minor changes to this script
for timeDelay in range(178,366):    
    if (timekeeper == 9):
        time.sleep(60)
        timekeeper = 0

    timekeeper += 1
    
    datevar = dateStart + datetime.timedelta(timeDelay)
    writeFile = open(str(datevar)[0:4] + "_" + str(datevar)[5:7]+ "_" + str(datevar)[8:10]+ "_" + "output.json", 'w')

    response = urllib2.urlopen(
        'http://api.wunderground.com/api/{Your API key}/history_'
        + str(datevar)[0:4] +str(datevar)[5:7]+str(datevar)[8:10]+
        '/q/IL/Chicago.json')

    data = json.load(response)   
    writeFile.write(str(data))
    writeFile.close()
