import requests
import xml.etree.ElementTree as ET
#from requests_xml import XMLSession


ip = "http://10.99.17.50"

s = requests.Session()
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

results = str(s.get('http://10.99.17.50/wcd/job.xml', headers=headers, cookies=cookies).text)
#results = open('job.xml', 'r')
from bs4 import BeautifulSoup

#print(results)
#print(page)

#print(joblist)

def getData(ip):
    page = BeautifulSoup(results, features='xml')
    prototype = 'JobList'
    printObject = page.find_all(prototype)
    counter = 0
    # check if it exists
    if printObject:

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
        return(length, jobID, jobType, startTime)
    else:
        print('No Jobs')
    length = counter


getData('')
'''
from xmljson import badgerfish as bf
from lxml.html import Element, fromstring

results.decode('utf-8').encode('ascii')


import xmljson
def removebadXML(xml):
    lines = xml.readLines()
    print(lines[58])


with open('job.xml') as job:
    results = xmltodict.parse(job.read())

print(results)

#print(results)
#removebadXML(results)
print(bf.data(fromstring(results)))

newresult = map(lambda x: x.replace('<WithPrint><Enprint(get)', '').replace('<?xml version="1.0" encoding="UTF-8"?><?xml-stylesheet href="job.xsl" type="text/xsl"?>', '') for x in results)
removebadXML(newresult)
'''
