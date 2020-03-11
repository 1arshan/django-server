from django.urls import path 
from send import views

app_name ='send'
urlpatterns =[

    path('1', views.index1,name ='index1'),
    path('2', views.index2,name ='index2'),
    path('email', views.mailing.as_view(),name ='mailing'),

]
