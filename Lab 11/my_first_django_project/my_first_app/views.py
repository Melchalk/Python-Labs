from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

# Create your views here.
def hello_world(request):
    return HttpResponse("<h1>Hello, World!</h1>")

def list_by_temp(request):
    names = ["Mel", "Max", "Katy"]
    data = {"names": names}
    return render(request, "base.html", context=data)

def extended_temp(request):
    return render(request, "extended.html")