"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Test(models.Model):
    test_text = models.CharField(max_length=200)

    def __str__(self):
        return self.test_text

class Responces(models.Model):

    op1Numbers = models.IntegerField()
    op2Numbers = models.IntegerField()
    op3Numbers = models.IntegerField()
    op4Numbers = models.IntegerField()

    def __str__(self):
        return str(str(self.op1Numbers) + str(self.op2Numbers) + str(self.op3Numbers) + str(self.op4Numbers))
