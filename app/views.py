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
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )


def test(request):
    """Renders the about page."""

    imgNum = getOptions.n()

    op = [app.models.Person.objects.get(imgNumber=getOptions.n()),app.models.Person.objects.get(imgNumber=getOptions.n()),app.models.Person.objects.get(imgNumber=getOptions.n()),app.models.Person.objects.get(imgNumber=getOptions.n())]

    op[random.randrange(0,4)] = app.models.Person.objects.get(imgNumber=imgNum)

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/question.html',


        context_instance = RequestContext(request,
        {
            'title':'Test2',
            'imgNum': imgNum,
            'year':datetime.now().year,
            'op1': op[0],
            'op2': op[1],
            'op3': op[2],
            'op4': op[3]
        }))
