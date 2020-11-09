from django.shortcuts import render
from django.views import generic
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def index(request):
    template=  loader.get_template('notes/index.html')
    return HttpResponse(template.render({}, request))