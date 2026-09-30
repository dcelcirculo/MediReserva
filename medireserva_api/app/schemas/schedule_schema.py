from datetime import time

from pydantic import BaseModel, ConfigDict

class CreateSchedule(BaseModel):
    doctor_id: int
    day: str
    start_time: time
    end_time: time

class ScheduleResponse(BaseModel):
    id: int
    doctor_id: int
    day: str
    start_time: time
    end_time: time

    model_config = ConfigDict(from_attributes=True)
    
class ScheduleUpdate(BaseModel):
    doctor_id: int | None = None
    day: str | None = None
    start_time: time | None = None
    end_time: time | None = None

    model_config = ConfigDict(from_attributes=True)