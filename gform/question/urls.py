from django.urls import path
from .views import *

app_name = 'question11'

urlpatterns = [
    path('general/', QuestionView.as_view(), name='question12'),
    path('<str:user_name>/', UserSpecificView.as_view(), name='userspecific'),
    path('abc/<int:pk>/', QuestionSpecificView.as_view()),

]

