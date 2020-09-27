from django.shortcuts import render
from django.views import generic
from django.template import loader
from django.http import HttpResponse

# Create your views here.
class IndexView(generic.View):
    def get(self, request, *args, **kwargs):
        template = loader.get_template('notes/index.html')
        return HttpResponse(template.render({}, request))