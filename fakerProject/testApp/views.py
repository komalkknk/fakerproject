from django.shortcuts import render
from testApp.models import *

# Create your views here.

def index(request):
    return render(request,'testAppTemplates/index.html')

def hydjobsinfo(request):
    hydjobs_list=hydjobs.objects.order_by('date')
    my_dict={'hydjobs_list':hydjobs_list}
    return render(request,'testAppTemplates/hydjobs.html',context=my_dict)

def punejobsinfo(request):
    return render(request,'testAppTemplates/punejobs.html')

def banglorejobsinfo(request):
    return render(request,'testAppTemplates/banglorejobs.html')

def chennaijobsinfo(request):
    return render(request,'testAppTemplates/chennaijobs.html')
