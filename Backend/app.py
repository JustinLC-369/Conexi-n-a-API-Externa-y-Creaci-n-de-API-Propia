from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import requests

import models
import schemas
import crud
from database import SessionLocal, engine, Base


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos los orígenes (solo para desarrollo)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/dogs/", response_model=schemas.DogOut)
def create_dog(dog: schemas.DogCreate, db: Session = Depends(get_db)):
    return crud.create_dog(db, dog)

@app.get("/dogs/", response_model=list[schemas.DogOut])
def read_dogs(db: Session = Depends(get_db)):
    return crud.get_dogs(db)

@app.get("/external/dogs")
def get_external_dogs():
    response = requests.get("https://dog.ceo/api/breeds/image/random/10")
    data = response.json()
    return data["message"]
