from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from mentor.models import Trainers,Events,Faculty,Course,User
from .forms import CategoryForm,ProductForm
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


@login_required_decorator
def category_list(request):
    categories = Categories.objects.all()
    ctx = {
        'categories':categories,
        "t_active": 'active'
    }
    return render(request,'dashboard/categories/list.html',ctx)

@login_required_decorator
def category_create(request):
    model = Category()
    form = CategoryForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('category_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/categories/form.html', ctx)

@login_required_decorator
def category_edit(request, pk):
    model = Category.objects.get(id=pk)
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('category_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/categories/form.html', ctx)

@login_required_decorator
def category_delete(request, pk):
    model = Category.objects.get(id=pk)
    model.delete()
    return redirect('category_list')


@login_required_decorator
def product_list(request):
    products = Product.objects.all()
    ctx = {
        'products':products,
        "t_active": 'active'
    }
    return render(request,'dashboard/products/list.html',ctx)

@login_required_decorator
def product_create(request):
    model = Product()
    form = ProductForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('product_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/products/form.html', ctx)

@login_required_decorator
def product_edit(request, pk):
    model = Product.objects.get(id=pk)
    form = ProductForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('product_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/products/form.html', ctx)

@login_required_decorator
def product_delete(request, pk):
    model = Product.objects.get(id=pk)
    model.delete()
    return redirect('product_list')


