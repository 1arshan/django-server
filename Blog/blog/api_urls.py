from django.urls import path,include
from blog.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('',bloggerViewSet)

urlpatterns =[
    path('',include(router.urls)),
]

