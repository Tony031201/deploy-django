from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from subscribe.models import subscribe
from meals.models import Meals
from meals.models import Category
from blog.models import Post
from .forms import MealsTableForm
from .forms import PostTableForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import csv


# Create your views here.
@login_required(login_url='get:login_view')
def get_statistic(request):
    content = 'this is what I  wanna send'
    context = {'email_body':content}
    if request.method == 'POST':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="subscribes.csv"'

        writer = csv.writer(response)

        writer.writerow(['Name', 'Email'])

        all_subscribes = subscribe.objects.all()

        for sub in all_subscribes:
            writer.writerow([sub.name, sub.email])

        return response

    return render(request,'get/get_statistic.html',context)

@login_required(login_url='get:login_view')
def menu_panel(request):
    meals = Meals.objects.all()
    categories = Category.objects.all()
    context = {
        'meals':meals,
        'categories':categories
    }
    return render(request,'get/menu_control.html',context)

@login_required(login_url='get:login_view')
def post_new_meal(request):
    if request.method == 'POST':
        form = MealsTableForm(request.POST,request.FILES or None)
        print("FILES:", request.FILES)
        if form.is_valid():
            # 使用 update_or_create 来创建或更新对象
            if request.FILES:
                meal, created = Meals.objects.update_or_create(
                    name=form.cleaned_data['name'],
                    defaults={
                        'description': form.cleaned_data['description'],
                        'price': form.cleaned_data['price'],
                        'image': form.cleaned_data['image'] ,
                        'category': form.cleaned_data['category']
                    }
                )
            else:
                meal, created = Meals.objects.update_or_create(
                    name=form.cleaned_data['name'],
                    defaults={
                        'description': form.cleaned_data['description'],
                        'price': form.cleaned_data['price'],

                        'category': form.cleaned_data['category']
                    }
                )
            return redirect('get:menu_panel')

        else:
            # 如果表单无效，可以返回错误信息
            return render(request, 'get/post_new_meal.html', {'form': form})
    else:
        form = MealsTableForm()
        context = {'form': form}
        return render(request,'get/post_new_meal.html',context)

@login_required(login_url='get:login_view')
def delete_meal(request,slug):
    meal = get_object_or_404(Meals, slug=slug)
    meal.delete()
    return redirect('get:menu_panel')

@login_required(login_url='get:login_view')
def modify_meal(request,slug):
    meal = get_object_or_404(Meals,slug=slug)
    form = MealsTableForm(instance=meal)
    context = {'form':form}
    return render(request,'get/post_new_meal.html',context)

@login_required(login_url='get:login_view')
def send_email(request):
    context={}
    if request.method == 'POST':
        title = request.POST.get('subject')
        content = request.POST.get('message')
        all_subscribes = subscribe.objects.all()
        all_email = [subscriber.email for subscriber in all_subscribes]
        context={
            'title':title,
            'content':content,
            'email':all_email
        }
        return render(request, 'get/send_email.html', context)
    return render(request,'get/send_email.html',context)

@login_required(login_url='get:login_view')
def blog_panel(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'get/blog_control.html', context)

@login_required(login_url='get:login_view')
def post_new_blog(request):

    if request.method == 'POST':
        form = PostTableForm(request.POST,request.FILES or None)
        print("FILES:", request.FILES)
        if form.is_valid():
            # 使用 update_or_create 来创建或更新对象
            if request.FILES:
                author = User.objects.get(username='tony')
                post, created = Post.objects.update_or_create(
                    title=form.cleaned_data['title'],
                    defaults={
                        'author':author,
                        'content': form.cleaned_data['content'],
                        'tags': form.cleaned_data['tags'],
                        'image': form.cleaned_data['image'] ,
                        'category': form.cleaned_data['category']
                    }
                )
            else:
                author = User.objects.get(username='tony')
                post, created = Post.objects.update_or_create(
                    title=form.cleaned_data['title'],
                    defaults={
                        'author':author,
                        'content': form.cleaned_data['content'],
                        'tags': form.cleaned_data['tags'],

                        'category': form.cleaned_data['category']
                    }
                )
            return redirect('get:blog_panel')

        else:
            # 如果表单无效，可以返回错误信息
            return render(request, 'get/post_new_blog.html', {'form': form})
    else:
        form = PostTableForm()
        context = {'form': form}
        return render(request,'get/post_new_blog.html',context)

@login_required(login_url='get:login_view')
def delete_blog(request,id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('get:blog_panel')

@login_required(login_url='get:login_view')
def modify_blog(request,id):
    post = get_object_or_404(Post,id=id)
    form = PostTableForm(instance=post)
    context = {'form':form}
    return render(request,'get/post_new_blog.html',context)

def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('get:get_statistic')
        else:
            context = {
                'name':username,
                'password':password
            }
            return render(request,'get/login.html',context)

    return render(request,'get/login.html',context)