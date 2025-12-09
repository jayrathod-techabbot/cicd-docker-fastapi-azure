from fastapi import FastAPI
from app.model import model


app = FastAPI()


@app.get("/")
def root():
    return {"status": "server is running"}


@app.post("/predict")
def classify(text: str):
    result = model.predict(text)
    return {"label": result}