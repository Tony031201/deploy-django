from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from subscribe.models import subscribe
import csv


# Create your views here.
@login_required(login_url='get:login_view')
def get_statistic(request):
    context = {}
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