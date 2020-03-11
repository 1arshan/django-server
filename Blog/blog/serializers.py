from rest_framework import serializers

from django.contrib.auth.models import User
from blog.models import Blogs,Blogs1


class blogger1serializer(serializers.ModelSerializer):
    #author =bloggerserializer(many =True)
    class Meta:
        model =Blogs1
        fields =['blog_content','id','Author']
        

class bloggerserializer(serializers.ModelSerializer):
    blog_detail =blogger1serializer(many =True) # x is here foreign key
    class Meta:
        model =Blogs
        fields = ['id','author','blog_detail']

class blogger3serializer(serializers.ModelSerializer):
    class Meta:
        model =Blogs
        fields = ['id','author','blog_logo']
        

class blogger2serializer(serializers.ModelSerializer):
    #Author =blogger3serializer(many =True)
    class Meta:
        model =Blogs1
        fields = ['blog_content','id','Author']

        