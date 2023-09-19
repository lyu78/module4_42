from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.db.models import Count, Q

from .models import Advertisement
from .forms import AdvertisementForm


User = get_user_model()


def index(request):
    adv = Advertisement.objects.all()
    context = {'advertisements': adv}
    return render(request, 'app_advertisements/index.html', context)


def top_sellers(request):
    users = User.objects.annotate(
        count=Count('advertisement')
    ).filter(~Q(count=0)).order_by('-count')

    context = {'users': users}
    return render(request, 'app_advertisements/top-sellers.html', context)


def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            adv = Advertisement(**form.cleaned_data)
            adv.user = request.user
            adv.save()
            url = reverse('main-page')
            return redirect(url)

    else:
        form = AdvertisementForm()

    context = {'form': form}
    return render(request, 'app_advertisements/advertisement-post.html', context)
