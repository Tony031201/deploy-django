from django.shortcuts import render
from .models import *
from taggit.models import Tag
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.
def post_list(request):
    post_list = Post.objects.all()

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