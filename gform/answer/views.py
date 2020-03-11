from django.shortcuts import render
from .models import *
from rest_framework import generics
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response


class SpecificQuestionAnswerView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnsInfoSerializers
    queryset = AnswerInfo.objects.all()


class UserSpecificView(generics.ListCreateAPIView):
    serializer_class = AnsInfoSerializers

    def get_queryset(self):
        username = self.kwargs['user_name']
        return AnswerInfo.objects.filter(username_email=username)


class AnswerView(APIView):
    # class AnswerView(generics.ListCreateAPIView):
    def get(self, request):
        x = AnswerInfo.objects.all()
        serializer = AnsInfoSerializers(x, many=True)
        print(serializer.data)
        return Response(serializer.data)
