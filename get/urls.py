from django.urls import path
from . import views

app_name ='get'
urlpatterns = [
    path('', views.get_statistic,name='get_statistic'),
    path('login/', views.login_view,name='login_view'),
    path('menu_panel/',views.menu_panel,name='menu_panel'),
    path('post_new_meal/',views.post_new_meal,name='post_new_meal'),
    path('delete_meal/<slug:slug>',views.delete_meal,name='delete_meal'),
    path('modify_meal/<slug:slug>',views.modify_meal,name='modify_meal'),
    path('send_email/',views.send_email,name='send_email'),
    path('blog_panel/',views.blog_panel,name='blog_panel'),
    path('post_new_blog/',views.post_new_blog,name='post_new_blog'),
    path('delete_blog/<int:id>',views.delete_blog,name='delete_blog'),
    path('modify_blog/<int:id>',views.modify_blog,name='modify_blog'),
    path('show_email/',views.show_email,name='show_email'),
]