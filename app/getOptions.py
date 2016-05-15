import random

numbers = [i for i in range(100)]

alpha = 'abcdefghijklmnopqrstuvwxyz'

chars = [i for i in alpha]

def returnRandomInNumbers():
    return numbers[random.randrange(0,100)]

def returnRandomInChars():
    return chars[random.randrange(0,26)]

