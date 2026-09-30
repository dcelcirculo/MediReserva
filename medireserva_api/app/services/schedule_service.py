from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.schedule import Schedule
from app.schemas.schedule_schema import CreateSchedule, ScheduleUpdate

# Crear un nuevo horario
def create_schedule(db: Session, datos: CreateSchedule) -> Schedule:
    new_schedule = Schedule(
        doctor_id=datos.doctor_id,
        day=datos.day,
        start_time=datos.start_time,
        end_time=datos.end_time
    )
    
    db.add(new_schedule)
    db.commit()
    db.refresh(new_schedule)
    
    return new_schedule

# Obtener un horario por su ID
def get_schedule_by_id(db: Session, schedule_id: int) -> Schedule:
    schedule = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    if not schedule:
        raise HTTPException(status_code=404, detail="Horario no encontrado")
    return schedule

# Obtener todos los horarios de un doctor
def get_schedules_by_doctor(db: Session, doctor_id: int) -> list[Schedule]:
    schedules = db.query(Schedule).filter(Schedule.doctor_id == doctor_id).all()
    return schedules

# Obtener todos los horarios
def get_all_schedules(db: Session) -> list[Schedule]:
    schedules = db.query(Schedule).all()
    return schedules

# Eliminar un horario por su ID
def delete_schedule(db: Session, schedule_id: int) -> None:
    schedule = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    if not schedule:
        raise HTTPException(status_code=404, detail="Horario no encontrado")
    db.delete(schedule)
    db.commit()
    return None

# Actualizar los detalles de un horario
def update_schedule_details(db: Session, schedule_id: int, datos: ScheduleUpdate) -> Schedule:
    schedule = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    if not schedule:
        raise HTTPException(status_code=404, detail="Horario no encontrado")
    if datos.doctor_id is not None:
        schedule.doctor_id = datos.doctor_id
    if datos.day is not None:
        schedule.day = datos.day
    if datos.start_time is not None:
        schedule.start_time = datos.start_time
    if datos.end_time is not None:
        schedule.end_time = datos.end_time
    db.commit()
    db.refresh(schedule)
    return schedule