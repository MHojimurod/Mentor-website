from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from mentor.models import Trainers,Events,Faculty,Course,User
from .forms import TrainerForm,EventsForm,FacultyForm,CourseForm
import datetime

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
        'trainers':trainers,
        "t_active": 'active'
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
    events = Events.objects.all()
    ctx ={
        'events':events,
        "e_active": 'active'
    }
    return render(request,'dashboard/events/list.html',ctx)
def events_create(request):
    model = Events()
    form = EventsForm(request.POST,request.FILES, instance=model)
    if request.POST:
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/events/form.html', ctx)
def events_edit(request, pk):
    model = Events.objects.get(id=pk)
    form = EventsForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('events_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/events/form.html', ctx)
def events_delete(request, pk):
    model = Events.objects.get(id=pk)
    model.delete()
    return redirect('events_list')


def faculty_list(request):
    faculty = Faculty.objects.all()
    ctx = {
        'faculty':faculty,
        "f_active": 'active'
    }
    return render(request,'dashboard/faculty/list.html',ctx)
def faculty_create(request):
    model = Faculty()
    form = FacultyForm(request.POST,request.FILES, instance=model)
    if request.POST:
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faculty_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/faculty/form.html', ctx)
def faculty_edit(request, pk):
    model = Faculty.objects.get(id=pk)
    form = FacultyForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('faculty_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/faculty/form.html', ctx)
def faculty_delete(request, pk):
    model = Faculty.objects.get(id=pk)
    model.delete()
    return redirect('faculty_list')

def course_list(request):
    course = Course.objects.all()
    print(course)
    ctx = {
        'course':course,
        "c_active": 'active'
    }
    return render(request,'dashboard/course/list.html',ctx)
def course_create(request):
    model = Course()
    form = CourseForm(request.POST,request.FILES, instance=model)
    if request.POST:
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/course/form.html', ctx)
def course_edit(request, pk):
    model = Course.objects.get(id=pk)
    form = CourseForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('course_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/course/form.html', ctx)
def course_delete(request, pk):
    model = Course.objects.get(id=pk)
    model.delete()
    return redirect('course_list')

def users_list(request):
    users = User.objects.all()
    now = datetime.datetime.now()
    ctx = {
        'users':users,
        'now':now
    }
    return render(request,'dashboard/user_messages/message.html',ctx)

def read(request,pk):
    user = User.objects.filter(pk=pk)
    print('a',user)
    ctx = {
    'user': user
    }
    return render(request,'dashboard/user_messages/read.html',ctx)

