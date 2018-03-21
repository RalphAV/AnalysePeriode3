from django.shortcuts import render, redirect
from django.http import HttpResponse
from header.headertype import headertype, cleanhtml
from .forms import *



# Create your views here.
from header.models import saveHeader


def ex1(request):
   a = request.META['HTTP_USER_AGENT']
   return HttpResponse(a)

def ex2(request):
   a = request.META['HTTP_USER_AGENT']
   a += '<script>alert("Hi!")</script>'
   return render(request, 'index.html', {'head1': a})


def ex3(request):
   a = request.META
   return render(request, 'index.html', {'head2' : a})

def ex4(request):
    allobjects = saveHeader.objects.all()
    a = request.META['HTTP_USER_AGENT']
    a += '<script>alert("Hi!")</script>'
    headertype(a)
    return render(request, 'index.html', {'head3' : allobjects})

def ex5(request):

    return render(request, 'index2.html')

def colorExercise(request):
    modelform = nameForm(request.POST)
    colorform = colorForm(request.POST)
    if request.method == 'POST':
        if 'nameButton' in request.POST:
            if modelform.is_valid():
                request.session['name'] = modelform.cleaned_data['name']
                request.session['address'] = modelform.cleaned_data['address']
                return render(request, 'index3-2.html', {'colorform': colorform})
            else:
                modelform = nameForm()
        elif 'colorButton' in request.POST:
            if colorform.is_valid():
                request.session['color'] = colorform.cleaned_data['color']
                name = request.session['name']
                test = '\033[1m' + name
                address = request.session['address']
                color = request.session['color']
                object = colorOutput(name=test, color=color, address=address)
                object.save()
                return render(request, 'index3-3.html', {'name': test, 'color': color})
            else:
                colorform = colorForm()
    else:
        return render(request, 'index3-1.html', {'modelform' : modelform})



def formexercise(request):
    form = messageForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            text = form.cleaned_data['text']
            message = cleanhtml(text)
            object = MessageText(text=message)
            object.save()
            messages = MessageText.objects.all().order_by('-id')[:10]
            return render(request, 'message.html', {'form' : form, 'messages' : messages})
        else:
            form = messageForm()
    else:

        return render(request, 'message.html', {'form' : form})
