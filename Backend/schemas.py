from pydantic import BaseModel

class DogBase(BaseModel):
    title: str
    description: str
    image_url: str

class DogCreate(DogBase):
    pass

class DogOut(DogBase):
    id: int

    class Config:
        orm_mode = True
