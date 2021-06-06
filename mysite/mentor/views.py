from django.shortcuts import render,redirect
from .services import *
from .models import *
from .forms import *


def home(request):
    course = get_course()
    trainers = get_trainers()
    model = Newsletter()
    form = NewsForm(request.POST, instance=model)
    count_trainers = get_trainers_count()
    count_events = get_events_count()
    count_course = get_courses_count()
    if request.POST:
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    ctx = {
        'home_page': "active",
        'course': course,
        'trainers': trainers,
        'form': form,
        "count_t": count_trainers,
        "count_e": count_events,
        "count_c": count_course,

    }
    return render(request, 'mentor/index.html', ctx)


def about(request):
    model = Newsletter()
    form = NewsForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    ctx = {
        'about_page': "active",
        'form':form
    }
    return render(request, 'mentor/about.html', ctx)


def courses(request):
    model = Newsletter()
    form = NewsForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    course = get_course()

    ctx = {
        'course': course,
        'courses_page': "active",
        'form':form
    }
    return render(request, 'mentor/courses.html', ctx)

def course_details(request,course_id):
    courses = get_course_by_id(course_id)
    ctx = {
        'courses': courses
    }
    return render(request, 'mentor/course-details.html',ctx)


def trainers(request):
    model = Newsletter()
    form = NewsForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    trainers = get_trainers()
    ctx = {
        'trainers': trainers,
        'trainers_page': "active",
        'form': form
    }
    return render(request, 'mentor/trainers.html', ctx)


def events(request):
    model = Newsletter()
    form = NewsForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    events = get_events()
    ctx = {
        'events_page': "active",
        'events': events,
        'form': form
    }
    return render(request, 'mentor/events.html', ctx)


def contact(request):
    a = request.GET
    print(a)
    model = Newsletter()
    form = NewsForm(request.POST, instance=model)
    model_1 = User()
    form_1 = UserForm(request.POST,instance=model_1)
    if request.POST:
        print(request.POST.keys())
        if 'email' in request.POST.keys():
            if form.is_valid():
                form.save()
                return redirect('contact')
        elif 'email_user' in request.POST.keys():
            if form_1.is_valid():
                form_1.save()
                return redirect('contact')
    ctx = {
        'contact_page': "active",
        'form': form,
        'form_1': form_1
    }
    return render(request, 'mentor/contact.html', ctx)

# def newsletter:
