import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
import time
import csv
import datetime
import pandas

#forms

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired



database = pandas.read_csv("database.csv").to_dict('records')

s = requests.Session()

def generateETA(length): #take number of originals * copies
    ETA = str(length * 2) + ' minutes remaining' #1.2375 seconds per page
    print(ETA)
    return ETA

def login(ip):
    payload = 'func=PSL_LP0_TOP&AuthType=None&TrackType=Password&ExtSvType=&Lang=En&Mode=Track&trackpassword=password&ViewMode=Html&ShowDialog=Dialog'
    try:
        s.post('http://' + str(ip) + '/wcd/ulogin.cgi', 'payload', timeout=2)
    except HTTPError as http_err:
        print('HTTP error occurred:' + str(http_err))  # Python 3.6
    except Exception as err:
        print('Other error occurred: ' + str(err))  # Python 3.6
    else:
        return True

def getData(results):
    print('Getting data')
    page = BeautifulSoup(results, features='xml')
    printObject = page.find_all('Job')
    queue = {}
    for jobs in printObject:
        jobID = jobs.find('JobID').text
        jobType = jobs.find('JobType').text

        hour = jobs.find('Hour').text
        minute = jobs.find('Minute').text
        #add the formatting zero
        if len(minute) == 1:
            minute = '0' + minute
        startTime = (str(hour) + ':' + str(minute))
        print(jobType, jobID, startTime)

        status = jobs.find('Status').text
        documentNumber = int(jobs.find('DocumentNumber').text)
        copyNumber = int(jobs.find('CopyNumber').text)

        totalpages = documentNumber * copyNumber

        eta = str(totalpages * 1.24)

        queue = {'jobID':jobID, 'jobType':jobType, 'startTime':startTime, 'eta':eta, 'status':status, 'totalpages':str(totalpages)}
    return(queue)



from flask import Flask, render_template
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


class reportForm(FlaskForm):
    notes = StringField('Notes')
    submit = SubmitField('Submit')



@app.route("/")
def main():
    print('Request received...updating')
    fulltime = 0
    for copierObject in database:
        copierObject['Queue'] = []
        if copierObject['Type'] == 'Bizhub':
            if login(copierObject['IP']):
                print('actual ip')
                print('Logged in to ' + str(copierObject['Name']))
                results = ''
                cookies = {'selno': 'En', 'vm': 'Html','wd': 'y','uatype': 'NN','lang': 'En','ID': 'cbadf4c56bebf949dddc37cd47f838b4',  'usr': 'J_ACT',}
                headers = {'Connection': 'keep-alive','Cache-Control': 'max-age=0','Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36', 'DNT': '1', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3','Referer': 'http://10.99.17.50/wcd/system.xml', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,en;q=0.9',}
                try:
                    results = str(s.get('http://' + str(copierObject['IP']) + '/wcd/job.xml', headers=headers, cookies=cookies, timeout=3).text)
                except Exception as err:
                    print('Other error occurred: ' + str(err))  # Python 3.6

                queueData = getData(results)
                copierObject['Queue'].append(queueData)
                copierObject['Status'] = 'connected'
                copierObject['JobCount'] = len(copierObject['Queue'])
                copierObject['ETA'] = '0'
                print(queueData)
                if len(queueData) != 0:
                    #fulltime = fulltime + float(queueData['eta'])
                    print('Yes')
            else:
                copierObject['Queue'] = ''
                copierObject['JobCount'] = '0'
                copierObject['Status'] = 'unavaliable'
                copierObject['ETA'] = '0'

        elif copierObject['Type'] == 'Test':
            print('Recieved Test')
            results = open('job.xml')
            queueData = getData(results)
            copierObject['Queue'].append(queueData)
            copierObject['Status'] = 'connected'
            copierObject['JobCount'] = len(copierObject['Queue'])
            print(queueData)


            rawTime = '24 Seconds'
            copierObject['ETA'] = rawTime


    print(database)
    form = reportForm()

    if form.validate_on_submit():
        copierObject['Status'] = 'Broken'
        copierObject['brokenNotes'] = form.Notes.data
        return redirect('/')
    return render_template('index.html', state=database, form=form)


if __name__ == "__main__":
    app.debug = True
    app.run(host = '10.99.116.132', port=5000)
