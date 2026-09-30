from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.appointment import Appointment
from app.schemas.appointment_schema import CreateAppointment
from app.auth.security import hash_password

# Crear una nueva cita
def create_appointment(db: Session, datos: CreateAppointment, user_id: int) -> Appointment:
    new_appointment = Appointment(
        user_id=user_id,
        doctor_id=datos.doctor_id,
        schedule_id=datos.schedule_id,
        appointment_date=datos.appointment_date,
        appointment_time=datos.appointment_time,
        status="scheduled"
    )
    
    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)
    
    return new_appointment

# Obtener una cita por su ID
def get_appointment_by_id(db: Session, appointment_id: int) -> Appointment:
    appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()
    if not appointment:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return appointment

# Obtener todas las citas de un usuario
def get_appointments_by_user(db: Session, user_id: int) -> list[Appointment]:
    appointments = db.query(Appointment).filter(Appointment.user_id == user_id).all()
    return appointments

# Obtener todas las citas de un doctor
def get_appointments_by_doctor(db: Session, doctor_id: int) -> list[Appointment]:
    appointments = db.query(Appointment).filter(Appointment.doctor_id == doctor_id).all()
    return appointments

# Obtener todas las citas
def get_all_appointments(db: Session) -> list[Appointment]:
    appointments = db.query(Appointment).all()
    return appointments

# Eliminar una cita por su ID
def delete_appointment(db: Session, appointment_id: int) -> None:
    appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()
    if not appointment:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    db.delete(appointment)
    db.commit()
    return None

# Actualizar el estado de una cita
def update_appointment_status(db: Session, appointment_id: int, new_status: str) -> Appointment:
    appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()
    if not appointment:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    appointment.status = new_status
    db.commit()
    db.refresh(appointment)
    return appointment

# Actualizar los detalles de una cita
def update_appointment_details(db: Session, appointment_id: int, datos: CreateAppointment) -> Appointment:
    appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()
    if not appointment:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    appointment.doctor_id = datos.doctor_id
    appointment.schedule_id = datos.schedule_id
    appointment.appointment_date = datos.appointment_date
    appointment.appointment_time = datos.appointment_time
    db.commit()
    db.refresh(appointment)
    return appointment

