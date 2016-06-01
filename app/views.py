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


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance=RequestContext(
            request,
            {
                'title': 'Contact',
                'message': 'Your contact page.',
                'year': datetime.now().year,
                'version': "1.0"
            })
    )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance=RequestContext(
            request,
            {
                'title': 'About',
                'message': 'Your application description page.',
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

    answer = getOptions.getRandomRecord()

    if "alreadyUsed" in request.COOKIES:
        alreadyUsedList = request.COOKIES["alreadyUsed"].split(',')
        print(alreadyUsedList)
        print(answer.imgNumber)
        while str(answer.imgNumber) in alreadyUsedList:
            answer = getOptions.getRandomRecord()


    """CHECK CORRECT"""

    previousAnswer = request.POST.get("answer", default=None)
    previousCorrect = request.POST.get("correctImgId", default=None)


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

    ## if the cookie does not exist, create one
    if not "playerNumCorrect" in request.COOKIES or request.GET.get("q",default=0) == 0:
        serverResponce.set_cookie("playerNumCorrect",value=0)

    if not "alreadyUsed" in request.COOKIES or request.GET.get("q", default=0) == 0:
        serverResponce.set_cookie("alreadyUsed", value="")




    """MAIN STUFF"""
    #print("HIDDEN VALUE IS:")
    #print(request.POST.get("answer"))
    print(previousCorrect, previousAnswer)
    if previousCorrect != None and previousAnswer !=None:
        #previousCorrect = "op" + str(int(request.POST.get("correctOption", default=None)) + 1)
        #previousAnswer = request.POST.get("answer", default=None)

        previousAnswer = request.POST.get("answer",default=None)
        previousCorrect = request.POST.get("correctImgId",default=None)
        print(type(previousCorrect), type(previousAnswer))

        print(previousCorrect, previousAnswer, str(previousAnswer) == str(previousCorrect))

        p = app.models.Person.objects.get(imgNumber=request.POST.get("correctImgId", default=None))

        if previousCorrect == previousAnswer:
            print("LAST QUESTION WAS CORRECT")
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

        serverResponce.set_cookie("alreadyUsed", value=request.COOKIES["alreadyUsed"] + str(answer.imgNumber) + ',')



    if int(request.GET.get("q", default=1)) < 25+1:
        return serverResponce

    else:

        """CALCULATE PERCENT CORRECT"""

        totalPlayed = 25
        percent = (float(currentPlayerNumCorrect)/float(totalPlayed))*100.0

        """DEFINE SERVER RESPONCE"""

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
                    'version': "1.0"

                }))

        """DELETE COOKIES"""
        serverResultsResponce.delete_cookie("playerNumCorrect")

        return serverResultsResponce
