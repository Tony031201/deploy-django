from django.shortcuts import render
from .models import *
from taggit.models import Tag
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import PostTableForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import smtplib
import os
from dotenv import load_dotenv


# Create your views here.
def post_list(request):
    post_list = Post.objects.all().order_by('-id')

    ##search
    search_query = request.GET.get('q')
    if search_query:
        post_list = post_list.filter(
            Q(title__icontains=search_query)|
            Q(content__icontains=search_query)|
            Q(tags__name__icontains=search_query)
        ).distinct()
    paginator = Paginator(post_list, 5)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    post_list = paginator.get_page(page_number)
    context = {
        'post_list':post_list
    }
    return render(request,'Post/post_list.html',context)
def post_detail(request,id):
    post_detail = Post.objects.get(id=id)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {
        'post_detail':post_detail,
        'categories':categories,
        'tags':tags
    }
    return render(request,'Post/post_detail.html',context)

def post_by_tag(request,tag):
    post_by_tag = Post.objects.filter(tags__name__in=[tag])
    context = {
        'post_list':post_by_tag,
    }
    return render(request, 'Post/post_list.html', context)

def post_by_category(request,category):
    post_by_category = Post.objects.filter(category__category_name=category)
    context = {
        'post_list': post_by_category,
    }
    return render(request, 'Post/post_list.html', context)

@login_required(login_url='get:login_view')
def post_new(request):
    form = PostTableForm
    message = ''
    context = {
        'form':form,
    }
    if request.method == 'POST':
        form = PostTableForm(request.POST,request.FILES)
        author = request.user
        title = request.POST.get('title')
        content = request.POST.get('content')
        tags = request.POST.get('tags')
        image = request.FILES.get('image')
        category = request.POST.get('category')
        try:
            get_category = Category.objects.get(category_name=category)
        except Category.DoesNotExist:
            Category.objects.create(category_name=category)
            get_category = Category.objects.get(category_name=category)

        get_author = User.objects.get()
        post = Post.objects.create(
            author=author,
            title=title,
            content=content,
            image=image,
            category=get_category
        )
        tag_list = [tag.strip() for tag in tags.split(',')]

        for tag_name in tag_list:
            try:
                get = Tag.objects.get(name=tag_name)
            except Tag.DoesNotExist:
                Tag.objects.create(name=tag_name)
                get = Tag.objects.get(name=tag_name)
            post.tags.add(get)
        post.save()


        return render(request,'Post/post_new.html',context={'form':form,'message':'Post successfully'})

    return render(request,'Post/post_new.html',context)
