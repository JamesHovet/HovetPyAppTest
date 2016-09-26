"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
import app.models
# import random

from django.http import HttpResponse
# import getOptions


def home(request):
    """Renders the home page."""

    assert isinstance(request, HttpRequest)



    homeResponce = render(
        request,
        'app/index.html',
        context_instance=RequestContext(
            request,
            {
                'title': 'Home Page',
                'year': datetime.now().year,
                'version': "1.0"
            })
    )

    if 'playerID' in request.COOKIES:
        homeResponce.delete_cookie('playerID')

    return homeResponce



def playerLogin(request):
    assert isinstance(request, HttpRequest)

    """PREPARE REQUEST"""




    context = RequestContext(
        request,
        {
            'title': 'Player Login:',

        }
    )



    return render(
        request,
        'app/playerLogin.html',
        context_instance=context
    )


def leaderboard(request):
    assert isinstance(request, HttpRequest)

    print(app.models.Player.objects.all())

    list = app.models.Player.objects.all().filter(QuestionsAnswered__gte=49).order_by('CorrectPercentage').reverse()

    # list = ["one", "two", "three", "four"]

    for i in range(len(list)):
        list[i].Position = i + 1
        list[i].ImgNumber = str(list[i].ImgNumber)
        list[i].CorrectPercentage = str(list[i].CorrectPercentage*100)[:4] + "%"

    context = RequestContext(
        request,
        {
            'title': 'Leaderboard',
            'list': list,
        }
    )

    leaderboardRender = render(
        request,
        'app/leaderboard.html',
        context_instance=context
    )

    return leaderboardRender

# THIS IS MY FUNCTION##

def getColor(n):
    if n > 80:
        return "green"

    elif n > 70:
        return "orange"

    else:
        return "red"


def test(request):
    """Renders the question page"""

    # gets the img to be used from the database by getting the first in a
    # random arrangemet of all items in the db

    lowestNumber = app.models.Person.objects.order_by('NumShown').first().NumShown
    # print("lowest:", lowestNumber)

    answer = app.models.Person.objects.order_by('?').filter(NumShown=lowestNumber).first()
    answer.NumShown += 1
    answer.save()

    # this is not perfect for a few reasons, but I tried to remove duplicates,
    # and it works almost always

    # if "alreadyUsed" in request.COOKIES:
    #     alreadyUsedList = request.COOKIES["alreadyUsed"].split(',')
    #     print(alreadyUsedList)
    #     print(answer.ImgNumber)
    #     while str(answer.ImgNumber) in alreadyUsedList:
    #         answer = app.models.Person.objects.order_by('?').first()

    """CHECK CORRECT"""

    # this assigns the last answer and the last correct value to a variable.
    # this is done here because I am lazy and did not do this properly

    previousAnswer = request.POST.get("answer", default=None)
    previousCorrect = request.POST.get("correctImgId", default=None)




    # this is defining the responce that the server will send to the user

    """
    The values that I send to the user:

    title: the title that appears in the browser
    imgNum: the location of the file of the image on the server's disk

    numQuestion: question x out of 25
    correctOption: this is a debug bit that says what the actual answer is

    correctImgId: redundant, but I used it for debug

    the rest are debug things


    """

    assert isinstance(request, HttpRequest)
    """SERVER RESPONCE CREATION"""

    serverResponce = render(
        request,
        'app/question.html',

        context_instance=RequestContext(
            request,
            {

                'title': 'Quiz',
                'imgNum': str(answer.ImgNumber),

                'numQuestion': int(request.GET.get("q", default=1)),

                'correctImgId': answer.ImgNumber,

                'previousPersonId': request.POST.get("correctImgId", default=None),

                'version': "1.0",

            }))

    """COOKIE STUFF"""

    # if the cookie does not exist, create one, for all of the three cookies that I used
    # it also wipes the cookies if you are starting a new quiz, even if you do
    # not finish the last one
    if "playerNumCorrect" not in request.COOKIES or request.GET.get("q", default=0) == 0:
        serverResponce.set_cookie("playerNumCorrect", value=0)

    if "alreadyUsed" not in request.COOKIES or request.GET.get("q", default=0) == 0:
        serverResponce.set_cookie("alreadyUsed", value="")

    if "incorrectAnswers" not in request.COOKIES or request.GET.get("q", default=0) == 0:
        serverResponce.set_cookie("incorrectAnswers", value="")

    if "playerID" not in request.COOKIES:
        serverResponce.set_cookie("playerID", value=str(request.POST.get("PlayerName")))

        """CREATE PLAYERID FOR NEW PLAYERS"""

        try:
            currentPlayer = app.models.Player.objects.get(ImgNumber=request.POST.get("PlayerName"))

        except:
            newPlayer = app.models.Player(ImgNumber=request.POST.get("PlayerName"),UserName=app.models.Person.objects.get(ImgNumber=request.POST.get("PlayerName")).UnformattedName)
            print(newPlayer)
            print(newPlayer.ImgNumber)

            newPlayer.save()

            currentPlayer = newPlayer
    else:

        """ACTIVATE PLAYER"""

        currentPlayer = app.models.Player.objects.get(ImgNumber=request.COOKIES['playerID'])

    # if app.models.Player.get(playerID=str(request.POST.get("PlayerName"))) == None:


    print('currentPlayer', currentPlayer)

    """MAIN STUFF"""

    print("peviousCorrect, previousAnswer: ", previousCorrect, previousAnswer)

    print("POST:" , request.POST)
    print("GET:" , request.GET)
    print("COOKIES:", request.COOKIES)

    if previousCorrect is not None and previousAnswer is not None:

        # debug print to server console:
        # print(previousCorrect, previousAnswer, str(previousAnswer) == str(previousCorrect))

        # assign the person variable that we will use for the responce just
        # submitted, this is based off of the hidden input slot in the previous
        # HTML page
        p = app.models.Person.objects.get(
            ImgNumber=request.POST.get("correctImgId", default=None))

        # add one to number of times shown:


        if previousCorrect == previousAnswer:
            # print("LAST QUESTION WAS CORRECT")
            p.NumCorrect += 1
            p.save()
            print(str(p.UnformattedName) + "Now has " + str(p.NumCorrect))
            currentPlayerNumCorrect = int(request.COOKIES["playerNumCorrect"])
            serverResponce.set_cookie(
                "playerNumCorrect", value=currentPlayerNumCorrect + 1)
            currentPlayerNumCorrect += 1

            currentPlayer.AnswersCorrect += 1

        else:
            # print("LAST QUESTION WAS INCORRECT")
            p.NumIncorrect += 1
            print(str(p.UnformattedName) + "Now has " + str(p.NumIncorrect) + " Incorrect")
            p.save()
            currentPlayerNumCorrect = request.COOKIES["playerNumCorrect"]
            serverResponce.set_cookie("incorrectAnswers", value=request.COOKIES[
                                      "incorrectAnswers"] + str(p.ImgNumber) + ',')

            currentPlayer.AnswersIncorrect += 1

        # add that person to the list of already used
        serverResponce.set_cookie("alreadyUsed", value=request.COOKIES[
                                  "alreadyUsed"] + str(answer.ImgNumber) + ',')



        currentPlayer.QuestionsAnswered += 1

        currentPlayer.CorrectPercentage = (currentPlayer.AnswersCorrect/currentPlayer.QuestionsAnswered)

        currentPlayer.save()

    # if this is less than the 26th question, return the main question page
    # else: return the results page

    if int(request.GET.get("q", default=1)) < 25 + 1:
        return serverResponce

    else:

        """CALCULATE PERCENT CORRECT"""

        totalPlayed = 25
        percent = (float(currentPlayerNumCorrect) / float(totalPlayed)) * 100.0

        """DEFINE SERVER RESPONCE"""

        list = [app.models.Person.objects.get(ImgNumber=request.COOKIES['incorrectAnswers'].split(',')[i]) for i in
                range(len(request.COOKIES['incorrectAnswers'].split(',')) - 1)]

        print(list)

        for i in list:
            i.ImgNumber = str(i.ImgNumber)
            i.UnformattedName = i.UnformattedName.replace("\"", "")

        print(list)

        serverResultsResponce = render(
            request,
            'app/results.html',

            context_instance=RequestContext(
                request,
                {
                    'title': 'Results',
                    'numCorrect': currentPlayerNumCorrect,
                    'numAnswered': totalPlayed,
                    'percentColor': getColor(percent),
                    'percentScore': percent,
                    'version': "1.0",
                    'list': list,



                }))

        """DELETE COOKIES"""
        serverResultsResponce.delete_cookie("playerNumCorrect")

        return serverResultsResponce
