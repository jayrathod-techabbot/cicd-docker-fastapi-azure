from fastapi import FastAPI
from app.model import model


app = FastAPI()


@app.get("/")
def root():
    return {"status": "server is running"}


@app.get("/new")
def root():
    return {"status": "new server is running"}


@app.post("/predict")
def classify(text: str):
    result = model.predict(text)
    return {"label": result}