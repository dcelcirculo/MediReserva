from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.doctor import Doctor
from app.schemas.doctor_schema import CreateDoctor
from app.auth.security import hash_password

# Crear un nuevo doctor
def create_doctor(db: Session, datos: CreateDoctor, user_id: int) -> Doctor:
    new_doctor = Doctor(
        user_id=user_id,
        specialty=datos.specialty
    )

    db.add(new_doctor)
    db.commit()
    db.refresh(new_doctor)

    return new_doctor

# Listar todos los doctores
def list_doctors(db: Session):
    return db.query(Doctor).all()

# Obtener un doctor por su ID
def get_doctor_by_id(db: Session, doctor_id: int) -> Doctor:
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor no encontrado")
    return doctor

# Eliminar un doctor por su ID
def delete_doctor_by_id(db: Session, doctor_id: int):
    doctor = get_doctor_by_id(db, doctor_id)
    db.delete(doctor)
    db.commit()
    return {"detail": "Doctor eliminado correctamente"}

# Actualizar un doctor por su ID
def update_doctor(db: Session, doctor_id: int, datos: CreateDoctor) -> Doctor:
    doctor = get_doctor_by_id(db, doctor_id)
    doctor.specialty = datos.specialty
