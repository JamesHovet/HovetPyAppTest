"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Person(models.Model):

    ImgNumber = models.IntegerField()
    UnformattedName = models.CharField(max_length=200, default="UNFORMATTED NAME MISSING")
    FirstName = models.CharField(max_length=200, default="FIRST NAME MISSING")
    LastName = models.CharField(max_length=200, default="LAST NAME MISSING")
    NickName = models.CharField(max_length=200, default="NICK NAME MISSING")
    Form = models.IntegerField(default=0)
    Gender = models.CharField(max_length=10)
    NumCorrect = models.IntegerField(default=0)
    NumIncorrect = models.IntegerField(default=0)
    NumShown = models.IntegerField(default=0)


    def __str__(self):
        return str(self.UnformattedName)

class Player(models.Model):
    UserName = models.CharField(max_length=200, default="USERNAME MISSING")
    QuestionsAnswered = models.IntegerField(default=0)
    AnswersCorrect = models.IntegerField(default=0)
    AnswersIncorrect = models.IntegerField(default=0)
    ImgNumber = models.IntegerField(default=0)
    CorrectPercentage = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.UserName)
