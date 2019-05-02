import requests

baseURL = 'http://10.99.17.50'

s = requests.Session()
payload = {'func':'PSL_LP0_TOP', 'AuthType':'None', 'TrackType':'Password', 'ExtSvType&Lang':'Auto', 'Mode':'Track', 'trackpassword':'password', 'ViewMode':'html', 'ShowDialog':'Dialog'}
shortenedPayload = {'trackpassword' : 'password'}
originalPayload = 'func=PSL_LP0_TOP&AuthType=None&TrackType=Password&ExtSvType=&Lang=En&Mode=Track&trackpassword=password&ViewMode=Html&ShowDialog=Dialog'
login = s.post('http://10.99.17.50/wcd/top.xml', data=originalPayload)
#print(login)
print(login.text)
dataURL = 'http://10.99.17.50/wcd/flash_donejob.xml?cnt=11933021'
data = s.get(dataURL)
print(data.headers)
