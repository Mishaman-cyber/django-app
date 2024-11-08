from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
# Create your views here.

def home(request):
    mem = Member.objects.all().values()
    # x = {'name':'aman', 'age':20}
    context = {
        'mem': mem
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))
