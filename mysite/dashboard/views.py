from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


def login_required_decorator(f):
    return login_required(f, login_url="login")

@login_required_decorator
def dashboard(request):
    return render(request, 'dashboard/index.html')

def trainers_list(request):
    return render(request,'dhasboard/trainers.html')

def events_list(request):
    return render(request,'dhasboard/events.html')

def faculty_list(request):
    return render(request,'dhasboard/faculties.html')