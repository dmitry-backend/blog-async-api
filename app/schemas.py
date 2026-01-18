from pydantic import BaseModel, ConfigDict

class PostCreate(BaseModel):
    title: str
    content: str

class UserCreate(BaseModel):
    name: str
    age: int

class UserOut(BaseModel):
    id: int
    name: str
    age: int

    # allow build Pydantic model objs based on Declarative model obj attributes
    model_config = ConfigDict(from_attributes=True)
