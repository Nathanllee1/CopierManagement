import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
import time
import csv

import pandas

database = pandas.read_csv("database.csv").to_dict('records')

s = requests.Session()

def generateETA(length): #take number of originals * copies
    ETA = str(length * 2) + ' minutes remaining' #1.2375 seconds per page
    print(ETA)
    return ETA

def login(ip):
    payload = 'func=PSL_LP0_TOP&AuthType=None&TrackType=Password&ExtSvType=&Lang=En&Mode=Track&trackpassword=password&ViewMode=Html&ShowDialog=Dialog'
    try:
        s.post('http://' + ip + '/wcd/ulogin.cgi', 'payload', timeout=2)
    except HTTPError as http_err:
        print('HTTP error occurred:' + str(http_err))  # Python 3.6
    except Exception as err:
        print('Other error occurred: ' + str(err))  # Python 3.6
    else:
        return True

length =  0#this won't work with multiple printer

def getData(ip):
    print('Getting data from ' + ip)
    '''
    cookies = {'selno': 'En', 'vm': 'Html','wd': 'y','uatype': 'NN','lang': 'En','ID': 'cbadf4c56bebf949dddc37cd47f838b4',  'usr': 'J_ACT',}
    headers = {'Connection': 'keep-alive','Cache-Control': 'max-age=0','Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36', 'DNT': '1', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3','Referer': 'http://10.99.17.50/wcd/system.xml', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,en;q=0.9',}
    try:
        results = str(s.get('http://' + ip + '/wcd/job.xml', headers=headers, cookies=cookies).text)
    except HTTPError as http_err:
        print('HTTP error occurred:' + str(http_err))  # Python 3.6
    except Exception as err:
        print('Other error occurred: ' + str(err))  # Python 3.6
    '''
    results = open('job.xml', 'r')
    page = BeautifulSoup(results, features='xml')
    prototype = 'Job'
    printObject = page.find_all('Job')
    # check if it exists (currently not working)
    counter = 0

    for jobs in printObject:
        jobID = jobs.find('JobID').text
        jobType = jobs.find('JobType').text

        hour = jobs.find('Hour').text
        minute = jobs.find('Minute').text
        #add the formatting zero
        if len(minute) == 1:
            minute = '0' + minute
        startTime = (hour + ':' + minute)
        print(jobType, jobID, startTime)

        counter += 1
        eta = generateETA(counter)

        queue = {'jobID':jobID, 'jobType':jobType, 'startTime':startTime, 'eta':eta}
        return(queue)

    print(counter)
    length = counter




from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    print('Request received...updating')
    for copierObject in database:
        if copierObject['Type'] == 'Bizhub':
            if login(copierObject['IP']):
                print('Logged in to ' + str(copierObject['Name']))
                copierObject['Queue'] = getData(copierObject['IP'])
                copierObject['Status'] = 'Connected'
                copierObject['JobCount'] = length
            else:
                print('unavaliable')
                copierObject['Status'] = 'unavaliable'
    print(database)
    return render_template('index.html', state=database)


if __name__ == "__main__":
    app.run(port = 5001)
