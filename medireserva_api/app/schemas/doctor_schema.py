from pydantic import BaseModel, ConfigDict

class CreateDoctor(BaseModel):
    specialty_id: int
    
class DoctorResponse(BaseModel):
    id: int
    specialty_id: int

    model_config = ConfigDict(from_attributes=True)
    
class DoctorUpdate(BaseModel):
    specialty_id: int