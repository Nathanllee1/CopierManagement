import xmltodict

with open('job.xml') as job:
    results = xmltodict.parse(job.read())

tree = ET.ElementTree(ET.fromstring(results))
root = tree.getroot()
