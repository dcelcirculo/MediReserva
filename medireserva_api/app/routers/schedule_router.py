from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.schemas.schedule_schema import CreateSchedule, ScheduleResponse, ScheduleUpdate
from app.services import schedule_service

router = APIRouter(prefix="/schedules", tags=["schedules"])

# Obtener todos los horarios
@router.get("/", response_model=list[ScheduleResponse])
def list_schedules(db: Session = Depends(get_db)):
	return schedule_service.get_all_schedules(db)

# Obtener los horarios de un doctor
@router.get("/doctor/{doctor_id}", response_model=list[ScheduleResponse])
def list_doctor_schedules(doctor_id: int, db: Session = Depends(get_db)):
	return schedule_service.get_schedules_by_doctor(db, doctor_id)

# Obtener un horario por ID
@router.get("/{schedule_id}", response_model=ScheduleResponse)
def get_schedule(schedule_id: int, db: Session = Depends(get_db)):
	return schedule_service.get_schedule_by_id(db, schedule_id)

# Crear un nuevo horario
@router.post("/", response_model=ScheduleResponse, status_code=status.HTTP_201_CREATED)
def create_schedule(schedule: CreateSchedule, db: Session = Depends(get_db)):
	return schedule_service.create_schedule(db, schedule)

# Actualizar un horario existente
@router.put("/{schedule_id}", response_model=ScheduleResponse)
def update_schedule(schedule_id: int, schedule: ScheduleUpdate, db: Session = Depends(get_db)):
	return schedule_service.update_schedule_details(db, schedule_id, schedule)

# Eliminar un horario existente
@router.delete("/{schedule_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_schedule(schedule_id: int, db: Session = Depends(get_db)):
	schedule_service.delete_schedule(db, schedule_id)
	return None
