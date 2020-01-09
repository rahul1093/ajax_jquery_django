from .models import *
from .forms import *
from django.shortcuts import render, redirect
from django.http import HttpResponse


def Student_view(request):

        sform = StudentForm()
        return render(request, 'index.html', {'sform': sform})

def Student_views(request):

        Firstname = request.POST.get('Firstname')
        # Middlename = request.POST.get('Middlename')
        # Lastname = request.POST.get('Lastname')
        # SSC_marks = request.POST.get('SSC_marks')
        # Diploma_marks = request.POST.get('Diploma_marks')
        # BE_marks = request.POST.get('BE_marks')
        # Email = request.POST.get('Email')
        # contact = request.POST.get('contact')
        data = StudentData(
            Firstname=Firstname,
            Middlename="asd",
            Lastname="asd",
            SSC_marks=55,
            Diploma_marks=55,
            BE_marks=55,
            Email="asd",
            contact=458
        )
        data.save()
