import pathlib
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

BASE_DIR = pathlib.Path(__file__).parent
templates = Jinja2Templates(directory=BASE_DIR / "templates")

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home_view(request: Request):
    return templates.TemplateResponse(request, "home.html", {"abc": "123"})  # ✅ Fixed

@app.post("/")
def home_detail_view():
    return {"message": "You posted to the homepage. Thanks!"}