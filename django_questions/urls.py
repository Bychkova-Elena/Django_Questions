from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/v1/', include("questionsAnswers.urls")),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += doc_urls
