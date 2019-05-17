import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
import time
import csv
#real database
import pandas

database = pandas.read_csv("database.csv")
print(database)

s = requests.Session()

def generateETA(length):
    ETA = str(length * 2) + ' minutes remaining'
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

def getData(ip):
    cookies = {'selno': 'En', 'vm': 'Html','wd': 'y','uatype': 'NN','lang': 'En','ID': 'cbadf4c56bebf949dddc37cd47f838b4',  'usr': 'J_ACT',}
    headers = {'Connection': 'keep-alive','Cache-Control': 'max-age=0','Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36', 'DNT': '1', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3','Referer': 'http://10.99.17.50/wcd/system.xml', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,en;q=0.9',}

    results = str(s.get('http://' + ip + '/wcd/job.xml', headers=headers, cookies=cookies).text)

    page = BeautifulSoup(results, features='xml')
    prototype = 'JobList'
    printObject = page.find_all(prototype)

    # check if it exists (currently not working)
    if printObject:
        counter = 0
        for jobs in printObject:
            jobID = jobs.find('JobID').text
            jobType = jobs.find('JobType').text
            #starttimeObject = jobs.find('CreateTime')
            hour = jobs.find('Hour').text
            minute = jobs.find('Minute').text
            if len(minute) == 1:
                minute = str(0) + minute
            startTime = (hour + ':' + minute)
            print(jobType, jobID, startTime)
            #print(type(printObject))
            counter += 1
        print(counter)
    else:
        print('No Jobs')
    length = counter

    #dataframe it
    queue = [length, jobID, jobType, startTime]
    #queue = pandas.DataFrame([data])
    #print(queue)
    return(queue)


from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    rowcounter = 0
    print(database.shape[0])
    for index, row in database.iterrows():
        if row['Type'] == 'bizhub':
            print('uyes')
            if login(copier['IP']):
                print('Logged in to ' + str(copier['Name']))
                row['Queue'] = getData(row['IP'])
                row['Status'] = 'connected'
            else:
                row['Status'] = 'unavaliable'

        rowcounter += 1
    print(database.to_dict())
    return render_template('index.html', state=database.to_dict())


if __name__ == "__main__":
    app.run(port = 5001)
