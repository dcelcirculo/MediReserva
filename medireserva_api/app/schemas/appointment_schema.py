from datetime import date, time

from pydantic import BaseModel, ConfigDict

class CreateAppointment(BaseModel):
    doctor_id:int
    schedule_id: int
    appointment_date: date
    appointment_time: time
    
class AppointmentResponse(BaseModel):
    id: int
    doctor_id: int
    user_id: int
    schedule_id: int
    appointment_date: date
    appointment_time: time
    status: str

    model_config = ConfigDict(from_attributes=True)