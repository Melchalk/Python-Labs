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
from nested_app import views as nested_views

greet_patterns = [
    path("", nested_views.greet_world),
    path("name/<str:name>", nested_views.greet_by_name),
    path("age/<str:name>", nested_views.greet_with_name_and_age),
]

urlpatterns = [
    path('hello', views.hello_world_with_cookie),
    path('hello', views.hello_world),
    path('redirect', views.redirect),
    path('hello/<str:name>', views.hello_with_name_and_age),
    path('json', views.json_example),
    path('show/cookies', views.show_cookies),

    path("greet/", include(greet_patterns)),
]
