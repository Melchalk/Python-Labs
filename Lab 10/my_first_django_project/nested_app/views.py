from django.http import HttpResponse

# Create your views here.
def greet_world(request):
    return HttpResponse("<h1>Hello, World! I am nested app</h1>")

def greet_by_name(request, name):
    return HttpResponse(f"<h1>Hello, {name}! I am nested app</h1>")

def greet_with_name_and_age(request, name):
    age = request.GET.get("age", None)
    if age is None:
        return greet_by_name(request, name)
    else:
        return HttpResponse(
            f"<h1>Hello, {name}! I am nested app and you are {age} years old.</h1>")