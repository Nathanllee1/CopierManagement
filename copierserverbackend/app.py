import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
import time

state = {
    '106A Copier 1' : {
        'name': '106A Copier 1',
        'ip' : '10.99.17.50',
        'status' : '',
        'queue' : {
            'a' : {
                'number': 68,
                'time': '5:00 PM'
            },
            'b' : {
                'number': 69,
                'time': '4:20 AM'
            },
            'c' : {
                'number': 693,
                'time': 'yeet'
            }
        },
        'jobcount': 1,
        'type' : 'bizhub',
    },
    '106A Copier 2' : {
        'name': '106A Copier 2',
        'ip': '1234',
        'status' : '',
        'queue' : {},
        'jobcount': 0,
        'type' : 'bizhub'
    }
}



s = requests.Session()

def generateETA(jobNumber):
    ETA = str(jobNumber * 2) + ' minutes remaining'
    return ETA

def login(ip):
    payload = 'func=PSL_LP0_TOP&AuthType=None&TrackType=Password&ExtSvType=&Lang=En&Mode=Track&trackpassword=password&ViewMode=Html&ShowDialog=Dialog'
    try:
        s.post('http://' + ip + '/wcd/ulogin.cgi', 'payload', timeout=2)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        return True
'''
queuetemplate = 'jobnumber' = {
    'Status': ''
}
'''
def getQueue(ip):
    dataURL = 'http://' + ip + '/wcd/job.xml'
    data = s.get(dataURL)
    #soup = BeautifulSoup(data, 'html.parser')
    print(data.text)
    #print(soup.prettify)
    #rows = soup.find_all("tr").text
    '''
    for data in table
    put it in queutemplate and replace everything in
    '''

    print(data)

print(state)
'''
while True:
    for copier in state.values():
        if copier['type'] == 'bizhub':
            if login(copier['ip']):
                copier['queue'] = getQueue(copier['ip'])
            else:
                copier['status'] = 'unavaliable'
                print(state)
    time.sleep(100)
'''
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():

    for copier in state.values():
        if copier['type'] == 'bizhub':
            if login(copier['ip']):
                print('Logged in to ' + str(copier))
                copier['queue'] = getQueue(copier['ip'])
                copier['status'] = 'connected'
            else:
                copier['status'] = 'unavaliable'
                print(state)


    return render_template('index.html', state=state)


if __name__ == "__main__":
    app.run(port = 5001)
