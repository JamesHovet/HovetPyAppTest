# import random

import app.models


def getRandomRecord():
    return app.models.Person.objects.order_by('?').first()
