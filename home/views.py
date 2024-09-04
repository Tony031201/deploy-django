from django.shortcuts import render
from meals.models import Meals
from meals.models import Category
from blog.models import Post
from django.contrib import messages

# Create your views here.
def home(request):
    specials = Meals.objects.filter(category__name='SPECIAL')[:6]
    special1 = specials[0]
    special2 = specials[1]
    special3 = specials[2]
    special4 = specials[3]
    special5 = specials[4]
    special6 = specials[5]
    meal_list = Meals.objects.all()
    categories = Category.objects.all()
    post = Post.objects.last()

    context = {
        'special1':special1,
        'special2': special2,
        'special3': special3,
        'special4': special4,
        'special5': special5,
        'special6': special6,
        'meal_list':meal_list,
        'categories':categories,
        'post':post,

    }


    return render(request,'home/index.html',context)
