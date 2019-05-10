import requests
import xml.etree.ElementTree as ET
from requests_xml import XMLSession


ip = "http://10.99.17.50"

s = requests.Session()
xml = XMLSession()
payload = 'func=PSL_LP0_TOP&AuthType=None&TrackType=Password&ExtSvType=&Lang=En&Mode=Track&trackpassword=password&ViewMode=Html&ShowDialog=Dialog'

post = s.post(ip + '/wcd/ulogin.cgi', data=payload)
#cookies = post.cookies

cookies = {
    'selno': 'En',
    'vm': 'Html',
    'wd': 'y',
    'uatype': 'NN',
    'lang': 'En',
    'ID': 'cbadf4c56bebf949dddc37cd47f838b4',
    'usr': 'J_ACT',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'DNT': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Referer': 'http://10.99.17.50/wcd/system.xml',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
}

results = s.get('http://10.99.17.50/wcd/job.xml', headers=headers, cookies=cookies).text



import xml.etree.ElementTree as ET
tree = ET.ElementTree(ET.fromstring(results))
root = tree.getroot()

#print(results)

#for child in root:
#    print(child.tag, child.attrib)
for printobject in root.findall('JobHistoryList/Print/JobHistory'):
    print(printobject.attrib)