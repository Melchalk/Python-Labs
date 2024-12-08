from django.db.models import Avg
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseNotFound
from django.shortcuts import render
from django.db import connection

from my_first_app.models import Author, Book

# Create your views here.
def hello_world(request):
    return HttpResponse("<h1>Hello, World!</h1>")

#region Author Crud

def index_author(request):
    authors = Author.objects.all()
    return render(request, "index.html", {"authors": authors})

def create_author(request):
    if request.method == "POST":
        author = Author()
        author.name = request.POST.get("name")
        author.birth_date = request.POST.get("birth_date")
        author.bio = request.POST.get("bio")
        author.save()
    return HttpResponseRedirect("/")

def edit_author(request, id):
    try:
        author = Author.objects.get(id=id)

        if request.method == "POST":
            author.name = request.POST.get("name")
            author.birth_date = request.POST.get("birth_date")
            author.bio = request.POST.get("bio")
            author.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"author": author})
    except Author.DoesNotExist:
        return HttpResponseNotFound("<h2>Author not found</h2>")

def delete_author(request, id):
    try:
        author = Author.objects.get(id=id)
        author.delete()
        return HttpResponseRedirect("/")
    except Author.DoesNotExist:
        return HttpResponseNotFound("<h2>Author not found</h2>")

#endregion

#region Book Crud

def index_book(request):
    books = Book.objects.all()
    return render(request, "index_book.html", {"books": books})

def edit_book(request, id):
    try:
        return Book.objects.get(id=id)
    except Book.DoesNotExist:
        return HttpResponseNotFound("<h2>Book not found</h2>")

def create_book(request):
    if request.method == "POST":
        book = Book()
        book.title = request.POST.get("title")
        book.publication_date = request.POST.get("publication_date")
        book.save()
    return HttpResponseRedirect("/")

def edit_book(request, id):
    try:
        book = Book.objects.get(id=id)

        if request.method == "POST":
            book.title = request.POST.get("title")
            book.publication_date = request.POST.get("publication_date")
            book.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit_book.html", {"book": book})
    except Book.DoesNotExist:
        return HttpResponseNotFound("<h2>Book not found</h2>")

def delete_book(request, id):
    try:
        book = Book.objects.get(id=id)
        book.delete()
        return HttpResponseRedirect("/")
    except Book.DoesNotExist:
        return HttpResponseNotFound("<h2>Book not found</h2>")

#endregion

#region Filter

def filter_book(request, author_id):
    return Book.objects.all().filter(author_id=author_id)

def sort_book(request):
    return (Book.objects.all().order_by("publication_date")
            .values_list("title", flat=True))

#endregion

#region Set

def distinct_books_names(request):
    return Book.objects.values_list("name", flat=True).distinct()

#endregion

#region Aggregate

def get_avg_publication_date(request):
    author_id = request.GET.get("author_id")
    books = filter_book(request, author_id)
    return books.aggregate(Avg("publication_date"))

#endregion

#region SQL

def execute_custom_sql(request):
    sql = request.POST.get("sql")
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows


#endregion