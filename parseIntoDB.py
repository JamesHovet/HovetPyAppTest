import django
from app.models import Person

f = open("dataPy.csv", mode='r')

toBeAdded = []

# pTest = Person(ImgNumber=1, Form=18, FirstName="James", LastName="Hovet", NickName="James", NumCorrect=0, NumIncorrect=0, UnformattedName="shown 100",NumShown=100)

# '2988311,"Abby ""Abby"" Hannah Kong  \'17",Abby,Kong,Abby,17,F'

f.readline()

for line in f:

    d = line.strip().split(',')


    tmp = Person(ImgNumber=d[0], Form=d[5], FirstName=d[2], LastName=d[3], NickName=d[4], NumCorrect=0, NumIncorrect=0, UnformattedName=d[1],NumShown=0, Gender=d[6])

    tmp.save()
