from django.shortcuts import render
from .utils import fetch_and_save
from django.http import JsonResponse
from .models import Post


# Create your views here.

def home(request):
    # fetch_and_save()
    # groups = fetch_groups()
    # return JsonResponse(posts, safe=False)
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'home.html', context)
