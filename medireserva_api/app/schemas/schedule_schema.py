from datetime import time

from pydantic import BaseModel, ConfigDict

class CreateSchedule(BaseModel):
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