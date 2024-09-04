from django import forms
from meals.models import Meals
from blog.models import Post

class MealsTableForm(forms.ModelForm):
    class Meta:
        model = Meals
        fields = ['name', 'description', 'image', 'price', 'category']

        image = forms.ImageField(required=False)

class PostTableForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','image','tags','category']

        image = forms.ImageField(required=False)