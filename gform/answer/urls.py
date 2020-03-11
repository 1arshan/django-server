from django.urls import path
from .views import *

app_name = 'answer12'

urlpatterns = [
    path('general/', AnswerView.as_view(), name='answer11'),
    path('<str:user_name>/', UserSpecificView.as_view(), name='userspecific'),
    path('abc/<int:pk>/', SpecificQuestionAnswerView.as_view(), name='specificquestionanswer'),

]

