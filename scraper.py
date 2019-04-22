    #indexer
def GenerateIndex(response):
    lines = {}
    index = 0
    for line in response:
      line = line.split()
      dictionary = {index : line}
      lines.update(dictionary)
      index += 1

    return lines

#Get lists
def getListData():
    listpage = open('sampleresponse.txt', 'r')
    listpage = GenerateIndex(listpage)
    #print(listpage)
    IDList = []

    #Iterate over lines
    for index, line in listpage.items():

      #the indexing breaks when it's blank
      if line != []:
        if line[0] == 'Index':
          print(line)
          #Move along the index
          indexnum = int(line[2][:-1])
          id = listpage[indexnum + 2]
          IDList.append(id)
          time = listpage[indexnum + 12]

          #Replace with database commits
          #print(indexnum)
          #print(id)
          #print(time)
        else:
          pass
'''
    for IDs in IDList:
        detailpage = GenerateIndex(open('sampledetail.txt', 'r'))

        for index, line in detailpage.items():
          line = line.split()
          if line != []:

            index = 0

            while index < 7:
                if line[0] == 'JobDetail[' + index + ']':
                    pass
                else:
                    pass
'''
getListData()
