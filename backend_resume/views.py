from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.http import JsonResponse
from .models import PersonalInfo, Languages, Tools, Comment, Contact
from .forms import MessageForm


# Create your views here.
def index(request):
    info = PersonalInfo.objects.all()
    languages = Languages.objects.all()
    tools = Tools.objects.all()
    contact= Contact.objects.all()


    # receive user message from form
    if request.method != 'POST':
        form = MessageForm()
    else:
        form = MessageForm(request.POST)
        if form.is_valid():
            
            form.save()
            return HttpResponseRedirect(reverse('index'))
    context = {"personal": info,
            "contact": contact,
            "languages": languages,
            "tools": tools,
            'form': form}


    return render(request, "backend_resume/index.html", context)    



























   
