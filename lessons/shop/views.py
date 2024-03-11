from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import logging

logger = logging.getLogger(__name__)

def index(request):
    template = loader.get_template("index.html")
    logger.info('Shop page accessed')
    return HttpResponse(template.render())
