"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
import app.models
import random

from django.http import HttpResponse
import getOptions


def home(request):
    """Renders the home page."""

    assert isinstance(request, HttpRequest)
    return render(
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


##THIS IS MY FUNCTION##

def getColor(n):
    if n > 80:
        return "green"

    elif n > 70:
        return "orange"

    else:
        return "red"


def test(request):
    """Renders the question page"""

    # gets the img to be used from the database by getting the first in a random arrangemet of all items in the db

    answer = app.models.Person.objects.order_by('?').first()

    # this is not perfect for a few reasons, but I tried to remove duplicates, and it works almost always

    if "alreadyUsed" in request.COOKIES:
        alreadyUsedList = request.COOKIES["alreadyUsed"].split(',')
        print(alreadyUsedList)
        print(answer.imgNumber)
        while str(answer.imgNumber) in alreadyUsedList:
            answer = app.models.Person.objects.order_by('?').first()


    """CHECK CORRECT"""

    # this assigns the last answer and the last correct value to a variable. this is done here because I am lazy and did not do this properly

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
                'imgNum': str(answer.imgNumber),



                'numQuestion': int(request.GET.get("q", default=1)),
                'correctOption':answer.name,


                'correctImgId': answer.imgNumber,

                'previousCorrectDebug': previousCorrect,
                'previousAnswerDebug': request.POST.get("answer", default=None),
                'previousPersonId': request.POST.get("correctImgId", default=None),

                'version': "1.0",




            }))


    """COOKIE STUFF"""

    ## if the cookie does not exist, create one, for all of the three cookies that I used
    ## it also wipes the cookies if you are starting a new quiz, even if you do not finish the last one
    if not "playerNumCorrect" in request.COOKIES or request.GET.get("q",default=0) == 0:
        serverResponce.set_cookie("playerNumCorrect",value=0)

    if not "alreadyUsed" in request.COOKIES or request.GET.get("q", default=0) == 0:
        serverResponce.set_cookie("alreadyUsed", value="")

    if not "incorrectAnswers" in request.COOKIES or request.GET.get("q",default=0) == 0:
        serverResponce.set_cookie("incorrectAnswers", value="")




    """MAIN STUFF"""

    print(previousCorrect, previousAnswer)
    if previousCorrect != None and previousAnswer !=None:

        # debug print to server console:
        #print(previousCorrect, previousAnswer, str(previousAnswer) == str(previousCorrect))


        # assign the person variable that we will use for the responce just submitted, this is based off of the hidden input slot in the previous HTML page
        p = app.models.Person.objects.get(imgNumber=request.POST.get("correctImgId", default=None))

        if previousCorrect == previousAnswer:
            #print("LAST QUESTION WAS CORRECT")
            p.numCorrect += 1
            p.save()
            print(str(p.name) + "Now has " + str(p.numCorrect))
            currentPlayerNumCorrect = int(request.COOKIES["playerNumCorrect"])
            serverResponce.set_cookie("playerNumCorrect", value=currentPlayerNumCorrect+1)
            currentPlayerNumCorrect +=1
        else:
            print("LAST QUESTION WAS INCORRECT")
            p.numIncorrect +=1
            print(str(p.name) + "Now has " + str(p.numIncorrect) + " Incorrect")
            p.save()
            currentPlayerNumCorrect = request.COOKIES["playerNumCorrect"]
            serverResponce.set_cookie("incorrectAnswers", value=request.COOKIES["incorrectAnswers"] + str(p.imgNumber) + ',')

        # add that person to the list of already used
        serverResponce.set_cookie("alreadyUsed", value=request.COOKIES["alreadyUsed"] + str(answer.imgNumber) + ',')



    # if this is less than the 26th question, return the main question page
    # else: return the results page

    if int(request.GET.get("q", default=1)) < 25+1:
        return serverResponce

    else:

        """CALCULATE PERCENT CORRECT"""

        totalPlayed = 25
        percent = (float(currentPlayerNumCorrect)/float(totalPlayed))*100.0

        """DEFINE SERVER RESPONCE"""

        list = [app.models.Person.objects.get(imgNumber=request.COOKIES['incorrectAnswers'].split(',')[i]) for i in
         range(len(request.COOKIES['incorrectAnswers'].split(',')) - 1)]
        for i in list:
            i.imgNumber = str(i.imgNumber)

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
                    'list': list


                }))

        """DELETE COOKIES"""
        serverResultsResponce.delete_cookie("playerNumCorrect")

        return serverResultsResponce
