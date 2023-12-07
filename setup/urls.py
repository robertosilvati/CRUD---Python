from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crud/', TemplateView.as_view(template_name='crud.html')),
    path('home/', TemplateView.as_view(template_name='home.html')),

]
