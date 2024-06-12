from django.urls import path
from . import views

app_name ='subscribe'
urlpatterns = [
    path('sub/', views.subscribefunction,name='subscribe'),
]