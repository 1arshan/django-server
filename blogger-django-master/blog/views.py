from django.shortcuts import render
from django.http.response import HttpResponse
from blog.models import Blog
from django.contrib.auth import authenticate, login



def home(request):
    return render(request, 'blog/home.html', {
        'blogs': Blog.objects.all()
    })


def details(request, pk):
    return render(request, 'blog/details.html', {
        'blog': Blog.objects.get(pk=pk)
    })


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

        return HttpResponse('POST')

    return render(request, 'blog/login.html')
