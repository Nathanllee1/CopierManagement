import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
import time

state = {
    '106A Copier 1' : {
        'ip' : '10.99.17.50',
        'status' : '',
        'queue' : [],
        'type' : 'bizhub'
    },
}

s = requests.Session()

def login(ip):
    payload = 'func=PSL_LP0_TOP&AuthType=None&TrackType=Password&ExtSvType=&Lang=En&Mode=Track&trackpassword=password&ViewMode=Html&ShowDialog=Dialog'
    try:
        s.post('http://' + ip + '/wcd/ulogin.cgi', data='payload', timeout=2)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        return True

def getQueue(ip):
    dataURL = 'http://' + ip + '/wcd/job.xml'
    data = s.get(dataURL)
    soup = BeautifulSoup(data, 'html.parser')
    #print(soup.prettify)
    rows = soup.find_all("tr").text

    print(rows)

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
                copier['queue'] = getQueue(copier['ip'])
            else:
                copier['status'] = 'unavaliable'
                print(state)


    return render_template('index.html', state=state, len=len(state))


if __name__ == "__main__":
    app.run(port = 5001)
