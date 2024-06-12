from django.shortcuts import render
from .models import subscribe
from .forms import SubscribeTableForm
    
# Create your views here.

def subscribefunction(request):
    subscribe_form = SubscribeTableForm
    if request.method == 'POST':
        subscribe_form = SubscribeTableForm(request.POST)

        if subscribe_form.is_valid():
            email = request.POST.get('email')
            if subscribe.objects.filter(email=email).exists():
                context = {
                    'form': subscribe_form,
                    'message': "You had already subscribed us."
                }
                return render(request, 'subscribe/subscribe.html', context)
            else:
                subscribe_form.save()
                subscribe_form = SubscribeTableForm
                context = {
                    'form': subscribe_form,
                    'message': "Thanks for your subscription!"
                }
                return render(request, 'subscribe/subscribe.html', context)

    context = {'form':subscribe_form}
    return render(request,'subscribe/subscribe.html',context)
