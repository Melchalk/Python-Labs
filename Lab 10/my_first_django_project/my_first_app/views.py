from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

# Create your views here.
def hello_world(request):
    return HttpResponse("<h1>Hello, World!</h1>")

def hello_by_name(request, name):
    return HttpResponse(f"<h1>Hello, {name}!</h1>")

def hello_with_name_and_age(request, name):
    age = request.GET.get("age", None)
    if age is None:
        return HttpResponse(f"<h1>Hello, {name}!</h1>")
    else:
        return HttpResponse(f"<h1>Hello, {name}! You are {age} years old.</h1>")

def redirect(request):
    return HttpResponseRedirect("/hello")

def json_example(request):
    return JsonResponse({"name": "Mel", "age": 20})

def hello_world_with_cookie(request):
    name = request.GET.get("name", None)
    if name is None:
        return HttpResponse("<h1>Hello, World!</h1>")
    else:
        response = HttpResponse("<h1>Hello, World!</h1>")
        response.set_cookie("username", name)
        return response

def show_cookies(request):
    response = ""
    for cookie in request.COOKIES:
        response += f"{cookie} {request.COOKIES[cookie]}"
    return HttpResponse(response)