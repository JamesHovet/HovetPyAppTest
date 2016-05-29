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
    if n > 89:
        return "green"

    elif n > 79:
        return "orange"

    else:
        return "red"


def test(request):
    """Renders the question page."""


    answer = getOptions.getRandomRecord()

    op = [app.models.Person.objects.filter(form=answer.form, isMale=answer.isMale).order_by('?')[i] for i in range(8)]

    op = list(set(op))

    correctOption = random.randrange(0, 5)

    op[correctOption] = answer

    assert isinstance(request, HttpRequest)

    ##CHECK CORRECT##

    previousCorrect = request.POST.get("correctOption",default=None)
    previousAnswer = request.POST.get("answer",default=None)

    if previousCorrect != None and previousAnswer !=None:
        previousCorrect = "op" + str(int(request.POST.get("correctOption", default=None)) + 1)
        previousAnswer = request.POST.get("answer", default=None)
        if previousCorrect == previousAnswer:
            print("LAST QUESTION WAS CORRECT")
            p = app.models.Person.objects.get(imgNumber=request.POST.get("correctImgId",default=None))
            p.numCorrect += 1
            p.save()
            print(str(p.name) + "Now has " + str(p.numCorrect))
        else:
            print("LAST QUESTION WAS INCORRECT")


    if int(request.GET.get("q", default=1)) < 10:
        return render(
            request,
            'app/question.html',

            context_instance=RequestContext(
                request,
                {
                    'title': 'Quiz',
                    'imgNum': str(answer.imgNumber),
                    'year': datetime.now().year,
                    'op1': op[0].name[:-3],
                    'op2': op[1].name[:-3],
                    'op3': op[2].name[:-3],
                    'op4': op[3].name[:-3],
                    'op5': op[4].name[:-3],

                    'numQuestion': int(request.GET.get("q", default=1)),

                    'correctOption': correctOption,
                    'correctImgId': answer.imgNumber,

                    'previousCorrectDebug':previousCorrect,
                    'previousAnswerDebug':request.POST.get("answer",default=None),
                    'previousPersonId':request.POST.get("correctImgId",default=None),

                    'version': "1.0"

                }))
    else:

        percent = 100

        return render(
            request,
            'app/results.html',

            context_instance=RequestContext(
                request,
                {
                    'title': 'Results',
                    'numCorrect': 23,
                    'numAnswered': 25,
                    'percentColor': getColor(percent),
                    'percentScore': percent,
                    'version': "1.0"

                }))
