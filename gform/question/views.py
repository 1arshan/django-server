from django.shortcuts import render
from .models import *
from rest_framework import generics
from .serializers import *
from rest_framework.views import APIView
from django import http
from rest_framework.response import Response


# class QuestionSpecificView(APIView):
class QuestionSpecificView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FormInfoSerializers
    queryset = FormInfo.objects.all()


class UserSpecificView(generics.ListCreateAPIView):
    serializer_class = FormInfoSerializers

    def get_queryset(self):
        username = self.kwargs['user_name']
        return FormInfo.objects.filter(username_email=username)


class QuestionView(generics.ListCreateAPIView):
    queryset = FormInfo.objects.all()
    serializer_class = FormInfoSerializers
