import logging

from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(response):
    page = """
    <!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Главная</title>
</head>
<body>
    <div id="menu">
        <div class="menu-item"><a href="#">Главная</a></div>
        <div class="menu-item"><a href="about/">О нас</a></div>
    </div>
    <h1>Главная</h1>
    <p>Главная страница сайта.</p>
</body>
</html>"""
    logger.info('Index page accessed')
    return HttpResponse(page)


def about(request):
    page = """
        <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>О нас</title>
    </head>
    <body>
        <div id="menu">
        <div class="menu-item"><a href="/">Главная</a></div>
        <div class="menu-item"><a href="#">О нас</a></div>
    </div>
        <h1>О нас</h1>
        <p>Страница описания "О нас". Чего-то тут должно быть написано.</p>
    </body>
    </html>"""
    logger.info('About page accessed')
    return HttpResponse(page)
