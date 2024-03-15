import random
from random import choice

from django.shortcuts import render
import logging
from django.http import HttpResponse
from django.template import loader
from .forms import GameForm

from .models import CoinFlip, DieToss, RandomNum

logger = logging.getLogger(__name__)


def index_task5(request):
    logger.info('Index page accessed')
    return HttpResponse("Toss dice")


def game(request):
    func = {"C": coin, "D": dice, "R": random_num}
    if request.method == 'POST':
        form = GameForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            choice_ = form.cleaned_data['choice']
            tries = form.cleaned_data['tries']
            logger.info(f'{choice_} -- {tries}')
            return func[choice_](request, tries)
    else:
        form = GameForm()
        message = 'Выберите игру'

    context = {
        'title': 'Выберите игру',
        'form': form,
        'message': message,
    }
    template_name = 'task05/game.html'

    return render(
        request,
        template_name,
        context
    )


def coin(request, amount_of_flips=3):
    template_name = "task05/result.html"
    head_or_tails = ("Heads", "Tails")
    side = choice(head_or_tails)
    CoinFlip(side=side).save()
    last_results = CoinFlip.get_last_flip(amount_of_flips)
    logger.info(side)
    context = {
        'title': "Бросаем монету",
        'result': side,
        'last_results': last_results
    }
    return render(request, template_name, context=context)


def dice(request, amount_of_toss=3):
    template_name = "task05/result.html"
    result = random.randint(1, 6)
    DieToss(result=result).save()
    last_results = DieToss.get_last_toss(amount_of_toss)
    logger.info(f"Dice was tossed and gave number {result}")
    context = {
        'title': "Бросаем кости",
        'result': result,
        'last_results': last_results
    }
    return render(request, template_name, context=context)


def random_num(request, amount_of_rand=3):
    template_name = "task05/result.html"
    result = random.randint(0, 100)
    RandomNum(result=result).save()
    last_results = RandomNum.get_last_num(amount_of_rand)
    logger.info(f"The random number from 0 to 100 is {result}")
    context = {
        'title': "Случайное число от 0 до 100",
        'result': result,
        'last_results': last_results
    }
    return render(request, template_name, context=context)
