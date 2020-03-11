
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('blog/',include('blog.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/',include('blog.api_urls')),
    path('email/',include('send.urls'))


   # path('/<int:>/',include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root =settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)