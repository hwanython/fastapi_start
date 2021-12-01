from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
# add helper each page context
from .library.helpers import *
#How to Add Routers to FastAPI
from app.routers import unsplash, twoforms, accordion



app = FastAPI()
# Import Jinja2Templates and set the template directory templates
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(unsplash.router)
app.include_router(twoforms.router)
app.include_router(accordion.router)
# app.include_router(unsplash.router)
# @app.get('/')
# async def home():
#     data = {
#         "text" : "hi"
#     }
#     return {"data" : data}

#Specifiy th response_class to HTMLResponse
@app.get("/", response_class=HTMLResponse)
#Add request as a parameter
async def home(request: Request):
    # define data shape
    # data = {
    #     "page" : "Home page",
    #     "Author": "Hwanython"
    # }
    # use the openfile in helper.py
    data = openfile("home.md")
    # Return templates.TemplateResponse() with the page HTML adn data
    return templates.TemplateResponse("page.html", {"request": request, "data": data})

@app.get("/page/{page_name}", response_class=HTMLResponse)
async def page(request: Request, page_name : str):
    # data = {
    #     "page" : page_name
    # }

    # use the openfile in helper.py
    data = openfile(page_name+".md")
    return templates.TemplateResponse("page.html", {"request": request, "data": data})



