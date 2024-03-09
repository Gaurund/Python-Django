'''
� Орёл или решка
� Значение одной из шести граней игрального кубика
� Случайное число от 0 до 100
'''
import random
from random import choice

from django.shortcuts import render
import logging
from django.http import HttpResponse


logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse("Toss dice")


def coin(request):
    head_or_tails = ("It's heads!", "It's tails!")
    coin_ = choice(head_or_tails)
    logger.info(coin_)
    return HttpResponse(coin_)


def dice(request):
    result = random.randint(1,6)
    logger.info(f"Dice was tossed and gave number {result}")
    return HttpResponse(f"The result of toss a dice is {result}")


def random_num(request):
    result = random.randint(0, 100)
    logger.info(f"The random number from 0 to 100 is {result}")
    return HttpResponse(f"The random number from 0 to 100 is {result}")
