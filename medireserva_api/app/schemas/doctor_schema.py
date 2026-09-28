from pydantic import BaseModel, ConfigDict

class CreateDoctor(BaseModel):
    specialty: str
    
class DoctorResponse(BaseModel):
    id: int
    specialty: str

    model_config = ConfigDict(from_attributes=True)