"""
URL configuration for my_first_django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from my_first_app import views
from my_first_app import custom_views

urlpatterns = [
    path('hello', views.hello_world),
    path("temp", views.list_by_temp),
    path("home", custom_views.HomeView.as_view(extra_context={"names": ["Mel", "Max", "Katy"]})),

    path("temp/extended", views.extended_temp),
]