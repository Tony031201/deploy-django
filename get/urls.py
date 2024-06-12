from django.urls import path
from . import views

app_name ='get'
urlpatterns = [
    path('', views.get_statistic,name='get_statistic'),
    path('login/', views.login_view,name='login_view'),
]