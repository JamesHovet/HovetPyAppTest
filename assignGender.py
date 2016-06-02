"""

This is code that never gets run on the server, but I used to assign a gender to the person based off of their name and my user input. it took about 12 minutes to go through everyone

"""


from app.models import Person

count = Person.objects.filter(isMale=-1).count()

for i in Person.objects.filter(isMale=-1):
    print("====================")
    print("there are ", count ," Left")
    count -=1
    print("male = 1, female = 2")
    print(i.imgNumber)
    print(i.name)
    if input("isMale: ") == '1' :
        i.isMale = 1
        print(i.name, " is now Male")
    else:
        i.isMale = 2
        print(i.name, " is now Female")

    i.save()
    print("===================")


"""

This is code that never gets run on the server, but I used to get all of the permutations of the name that I would need

this code was not perfect, and I had to fix some things by hand

"""

for i in Person.objects.all():
    s = i.name
    #print(s)
    try:
        print('<option value="' + str(i.imgNumber) + '">' + s[s.find('"'):].replace('"','') + '</option.')
    except:
        real = None
    print('<option value="' + str(i.imgNumber) + '">' + s + '</option.')
    print('<option value="' + str(i.imgNumber) + '">' + (s[:-4])[(s[:-4]).rfind(' ')+1:] + ', ' + s[:(s[:-4]).rfind(' ')+1] + '</option.')
