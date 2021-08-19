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





















































    # personal_info = {
    #     "phone": "0900000000", 
    #     "linkedIn": "",
    #     "twitter": ""

    # }
    # education = {
    #     "university": "University of Ilorin",
    #     "degree": "B.sc Microbiology",
    #     "web_programming": "",
    # }

    # projects = {
    #     "project1": "Django Chatapp",
    #     "project2": "E-commerce Website", 
    #     "project3": "Mail"
    # }

    # skills_tools = {
    #     'skills': ['Python', "Javascript",
    #      "HTML", "CSS", "Git/Github",
    #      "Bootstrap", "Postgresql", "ReactJs" ]
    # }

    # experience = {
    #     "zuri": [{"":"Zuri x I4G internship", 
    #     "duration": "August 2021 - Present"}]
        
    # }
    # my_data.append([{'personal':personal_info},
    #  {"education": education}, {"projects": projects}, 
    #  {"skills": skills_tools}, {"experience": experience}])

   