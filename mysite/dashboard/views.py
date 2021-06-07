from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from mentor.models import Trainers
from .forms import TrainerForm

def login_required_decorator(f):
    return login_required(f, login_url="login")

@login_required_decorator
def dashboard(request):
    return render(request, 'dashboard/index.html')

def dashboard_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'dashboard/login.html')

@login_required_decorator
def dashboard_logout(request):
    logout(request)
    return redirect('login')

def trainers_list(request):
    trainers = Trainers.objects.all()
    ctx = {
        'trainers':trainers
    }
    return render(request,'dashboard/trainers/list.html',ctx)
def trainer_create(request):
    model = Trainers()
    form = TrainerForm(request.POST,request.FILES, instance=model)
    if request.POST:
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trainer_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/trainers/form.html', ctx)
def trainer_edit(request, pk):
    model = Trainers.objects.get(id=pk)
    form = TrainerForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('trainer_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/trainers/form.html', ctx)
def trainer_delete(request, pk):
    model = Trainers.objects.get(id=pk)
    model.delete()
    return redirect('trainer_list')


def events_list(request):
    return render(request,'dashboard/events/list.html')

def faculty_list(request):
    return render(request,'dashboard/faculties/list.html')

def course_list(request):
    return render(request,'dashboard/course/list.html')