from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
import crud

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='crud.html')),
    path('home/', TemplateView.as_view(template_name='home.html')),
    path('', include('crud.urls')),
]
