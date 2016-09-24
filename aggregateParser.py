import json

outputFile = open("outputFile.csv", mode='w')
inputFile = open("jsonTmp.txt", mode='r')
numbersFile = open("numbersImgs.txt", mode='r')
unformattedNames = open("unformattedNames.txt", mode='r')

#output format:
# ImgNumber, UnformattedName, FirstName, LastName, NickName, Form, Gender

class item:
    def __init__(self, imgNumber):
        self.ImgNumber = imgNumber

        self.FirstName = "NO_FIRST_NAME"
        self.LastName = "NO_LAST_NAME"
        self.NickName = "NO_NICK_NAME"
        self.UnformattedName = "NO_UNFORMATTED_NAME"
        self.Gender = "NO_GENDER"
        self.Form = "NO_FORM"

    def printAsCSV(self):
        return self.ImgNumber + ',' + self.UnformattedName + ',' + self.FirstName + ',' + self.LastName + ',' + self.NickName + ',' + self.Form + ',' + self.Gender

    def __str__(self):
        return self.printAsCSV()

    def __repr__(self):
        return self.printAsCSV()

# TODO: add more of the json parsing
# TODO: add all of the html parsing code based on numbers
# TODO: basically, this code should fill in the whole spreadsheet of data, from every source possible

numbers = []

personDict = {}

for i in numbersFile.read().split("\n"):
    numbers.append(i)
    personDict[i] = item(i)

l = inputFile.read().split("start,end")



for i in l:

    j = json.loads(i)
    try:
        imgID = j['ProfilePhoto']['LargeFilename'][11:-4]

        FirstName = j['FirstName']
        LastName = j['LastName']

        try:
            NickName = j['NickName']
        except:
            real = None
        try:
            Gender = j['Gender']
        except:
            real = None

    except:
        real = None


    if imgID in numbers:
        personDict[imgID].FirstName = FirstName
        personDict[imgID].LastName = LastName
        personDict[imgID].NickName = NickName
        personDict[imgID].Gender = Gender

for name in unformattedNames.read().split("\n")[:-1]:
    n = name.split(',')
    # print(n[0], n[1])
    # print(n)
    if n[0] in numbers:
        personDict[n[0]].UnformattedName = n[1]
        personDict[n[0]].Form = n[1][-2:]

for key in personDict:
    if key != "":
        print(personDict[key])
