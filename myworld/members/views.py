from logging import exception
from urllib import response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members

findmem = Members()
res = ''

def index(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mymembers': mymembers,
        'findmember': findmem,
        'response': res,
    }
    return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    member = Members(firstname=x, lastname=y)
    member.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    member = Members.objects.get(id = id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    mymember = Members.objects.get(id = id)
    template = loader.get_template('update.html')
    context = {
        'mymember' : mymember,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    first = request.POST['first']
    last = request.POST['last']
    member = Members.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.save()
    return HttpResponseRedirect(reverse('index'))

def find(request):
    first = request.POST['first']
    try:
        findmember = Members.objects.get(firstname=first)
    except:
        global res
        res = 'Not found!'
        return HttpResponseRedirect(reverse('index'))
        
    global findmem 
    findmem = findmember   
    return HttpResponseRedirect(reverse('index'))
