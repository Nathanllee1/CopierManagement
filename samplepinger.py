import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError

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
        s.post('http://' + ip + '/wcd/ulogin.cgi', data='payload')
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        return True

def getQueue(ip):
    dataURL = 'http://' + ip + '/wcd/job.xml'
    data = s.get(dataURL)

for copier in state:
    print(copier)
    if copier['type'] == 'bizhub':
        if login(copier['ip']):
            copier['queue'] = getQueue(copier['ip'])
        else:
            copier['status'] = 'unavaliable'

'''
login = s.post('http://10.99.17.50/wcd/ulogin.cgi', data=originalPayload)
#print(login)
print('Logged in')
data = s.get(dataURL).content

soup = BeautifulSoup(data, 'html.parser')
#print(soup.prettify)
rows = soup.find_all("tr")

print(rows)
'''
