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
from django.template import loader


from .models import CoinFlip


logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse("Toss dice")


def coin(request):
    template = loader.get_template("coin.html")
    head_or_tails = ("Heads", "Tails")
    side = choice(head_or_tails)
    CoinFlip(side=side).save()
    logger.info(side)
    context = {
        'side': side,
        'last_results': CoinFlip.get_last_flip(10)
    }
    return HttpResponse(template.render(context=context))


def dice(request):
    result = random.randint(1,6)
    logger.info(f"Dice was tossed and gave number {result}")
    return HttpResponse(f"The result of toss a dice is {result}")


def random_num(request):
    result = random.randint(0, 100)
    logger.info(f"The random number from 0 to 100 is {result}")
    return HttpResponse(f"The random number from 0 to 100 is {result}")
