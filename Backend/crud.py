from sqlalchemy.orm import Session
import models
import schemas


def get_dogs(db: Session):
    return db.query(models.Dog).all()

def create_dog(db: Session, dog: schemas.DogCreate):
    db_dog = models.Dog(**dog.dict())
    db.add(db_dog)
    db.commit()
    db.refresh(db_dog)
    return db_dog
