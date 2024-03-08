import logging

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

logger = logging.getLogger(__name__)


def index(response):
    template = loader.get_template("index.html")
    logger.info('Index page accessed')
    return HttpResponse(template.render())


def about(request):
    template = loader.get_template("about.html")
    logger.info('About page accessed')
    return HttpResponse(template.render())
