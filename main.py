from typing import Optional
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import RedirectResponse


app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/learning/{item}")
async def redirect_typer(item):
    learning_pages = ["coursera", "edx", "acloudguru" ]
    for i in learning_pages:
        if i == item:
            result = "https://%s.com" % item
            return RedirectResponse(result)