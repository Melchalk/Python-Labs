import uvicorn
from user import users
from fastapi import FastAPI, Header, Response, Cookie, Form, Body
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse, RedirectResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get("/")
def say_hello():
    return "Hello, World!"

@app.get("/greet/{name}")
def greet_by_name(name):
    return f"Hello, {name}!"

@app.get("/search")
def use_query(query):
    return f"You searched for: {query}"

@app.get("/json")
def get_my_info():
    return {"name": "Mel", "age": 19, "hobby": "drawing"}

@app.get("/file")
def get_file():
    return FileResponse("file.txt", media_type="application/octet-stream")

@app.get("/redirect")
def redirect():
    return RedirectResponse("/")

@app.get("/headers")
def get_headers(header: str = Header()):
    return {"header": header}

@app.get("/set-cookie")
def set_cookie(your_name, response: Response):
    response.set_cookie(key="username", value=your_name)

@app.get("/get-cookie")
def get_cookie(username = Cookie()):
    return username

@app.get("/login")
def login_form():
    return FileResponse("login.html")

@app.post("/auth")
def auth(username = Form(), password=Form()):
    return f"Welcome, {username}!"

@app.post("/register")
def register(data = Body()):
    username = data["username"]
    return f"User {username} registered successfully!"

@app.get("/users")
def get_users():
    return users

@app.get("/users/{id}")
def get_users(id:int):
    for user in users:
        if user.id == id:
            return user
    return None

uvicorn.run(app, host="127.0.0.1", port=8000)
