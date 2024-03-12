import logging

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

logger = logging.getLogger(__name__)


def index(request):
    template_name = "myapp/index.html"
    logger.info('Index page accessed')
    return render(request, template_name)


def about(request):
    template_name = "myapp/about.html"
    logger.info('About page accessed')
    return render(request, template_name)
