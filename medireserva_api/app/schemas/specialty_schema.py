from pydantic import BaseModel, ConfigDict

class CreateSpecialty(BaseModel):
    name: str

class SpecialtyUpdate(BaseModel):
    name: str

class SpecialtyResponse(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)