import requests
import xml.etree.ElementTree as ET
ip = "http://10.99.17.50"

s = requests.Session()
payload = 'func=PSL_LP0_TOP&AuthType=None&TrackType=Password&ExtSvType=&Lang=En&Mode=Track&trackpassword=password&ViewMode=Html&ShowDialog=Dialog'

post = s.post(ip + '/wcd/ulogin.cgi', data=payload)


get = ip + '/wcd/job.xml'
results = s.get('http://10.99.17.50/wcd/job.xml').text

import xml.etree.ElementTree as ET
tree = ET.ElementTree(ET.fromstring(results))
root = tree.getroot()
#print(results)
for printobject in root.findall('JobHistory'):
    print('yes')
    print(printobject.text)
