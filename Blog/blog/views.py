from django.http import Http404
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import auth
from blog.models import Blogs, Blogs1
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.views.generic import View
from .forms import UserForm
from django.db.models import Q
from itertools import chain
from rest_framework import viewsets
from blog.serializers import bloggerserializer, blogger1serializer, blogger2serializer, blogger3serializer
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class homeview(generic.ListView):
    template_name = 'blog/home.html'
    context_object_name = 'all_blogs'
    queryset = Blogs.objects.all()


class detailview(generic.DetailView):
    model = Blogs
    template_name = 'blog/details.html'


class blogcreate(CreateView):
    model = Blogs
    fields = ['author', 'blog_logo']
    template_name = 'blog/blogs.html'


class blog1create(CreateView):
    model = Blogs1
    fields = ['Author', 'blog_content']
    template_name = 'blog/blogs1.html'

    def get_success_url(self):
        return reverse('blog:home')


class blogupdate(UpdateView):
    model = Blogs
    field = ['author', 'blog_logo']


class blogdelete(DeleteView):
    model = Blogs
    success_url = reverse_lazy('blog:home')


class UserFormview(View):
    form_class = UserForm
    template_name = 'blog/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # display full fill form
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # cleaned (normalized ) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns user onjects if credential are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return redirect('blog:home')
        return render(request, self.template_name, {'form': form})


class bloggerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = bloggerserializer


class SearchResultView(generic.ListView):
    model = Blogs, Blogs1
    template_name = 'blog/search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list1 = Blogs.objects.filter(
            Q(author__username__icontains=query))
        object_list2 = Blogs1.objects.filter(Q(blog_content__icontains=query))
        object_list = sorted(chain
                             (object_list1, object_list2),
                             key=lambda instance: instance.pk, reverse=True)

        return object_list


class BlogsView(APIView):
    def get(self, request):
        blogs = Blogs.objects.all()
        data = bloggerserializer(blogs, many=True).data
        return Response(data)

    def post(self, request):  # for adding blog_content
        # it doesnt matter wht id u provide it store data in id in which it want
        serializer = blogger1serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Blogs1View(APIView):  # detail

    def get_object(self, pk):
        try:
            return Blogs1.objects.filter(Author=pk)  # cant use get bec it only return single value
        except Blogs1.DoesNotExist:
            raise Http404

    def get_object1(self, pk):
        try:
            return Blogs1.objects.get(pk=pk)
        except Blogs1.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = blogger2serializer(snippet, many=True).data  # many =true is neccessary if u
        # r sending multiple data
        return Response(serializer)

    def put(self, request, pk):
        snippet = self.get_object1(pk)
        serializer = blogger2serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):  # give id of blog_content
        snippet = self.get_object1(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
