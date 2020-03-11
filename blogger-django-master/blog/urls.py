from django.urls import path
from blog.views import home, details, login_page

urlpatterns = [
    path('', home),
    path('<int:pk>/', details, name='blog-details'),
    path('login/', login_page, name='login-page')
]
# <int:pk> details(request, pk)
