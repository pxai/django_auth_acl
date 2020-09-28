from django.shortcuts import render
from django.views import generic
from django.template import loader
from django.http import HttpResponse

class AboutView(generic.View):
    def get(self, request, *args, **kwargs):
        template = loader.get_template('notes/about.html')
        return HttpResponse(template.render({}, request))