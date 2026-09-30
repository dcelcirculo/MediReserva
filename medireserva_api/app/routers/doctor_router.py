from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.schemas.doctor_schema import CreateDoctor, DoctorUpdate, DoctorResponse
from app.services import doctor_service

router = APIRouter(prefix="/doctors", tags=["doctors"])

# Obtener todos los doctores
@router.get("/", response_model=list[DoctorResponse])
def list_doctors(db: Session = Depends(get_db)):
    return doctor_service.list_doctors(db)

# Obtener un doctor por ID
@router.get("/{doctor_id}", response_model=DoctorResponse)
def get_doctor(doctor_id: int, db: Session = Depends(get_db)):
    return doctor_service.get_doctor_by_id(db, doctor_id)

# Crear un nuevo doctor
@router.post("/", response_model=DoctorResponse, status_code=status.HTTP_201_CREATED)
def create_doctor(doctor: CreateDoctor, user_id: int, db: Session = Depends(get_db)):
    return doctor_service.create_doctor(db, doctor, user_id)

# Actualizar un doctor existente
@router.put("/{doctor_id}", response_model=DoctorResponse)
def update_doctor(doctor_id: int, doctor: DoctorUpdate, db: Session = Depends(get_db)):
    return doctor_service.update_doctor(db, doctor_id, doctor)

# Eliminar un doctor existente
@router.delete("/{doctor_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_doctor(doctor_id: int, db: Session = Depends(get_db)):
    doctor_service.delete_doctor_by_id(db, doctor_id)
    return None