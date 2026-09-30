from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.config.database import get_db
from app.models.user import User
from app.schemas.appointment_schema import CreateAppointment, AppointmentResponse, AppointmentUpdate
from app.services import appointment_service

router = APIRouter(prefix="/appointments", tags=["appointments"])

# Obtener todas las citas
@router.get("/", response_model=list[AppointmentResponse])
def list_appointments(db: Session = Depends(get_db)):
    return appointment_service.get_all_appointments(db)

# Obtener una cita por ID
@router.get("/{appointment_id}", response_model=AppointmentResponse)
def get_appointment(appointment_id: int, db: Session = Depends(get_db)):
    return appointment_service.get_appointment_by_id(db, appointment_id)

# Crear una nueva cita
@router.post("/", response_model=AppointmentResponse, status_code=status.HTTP_201_CREATED)
def create_appointment(
    appointment: CreateAppointment,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return appointment_service.create_appointment(db, appointment, current_user.id)

# Actualizar una cita existente
@router.put("/{appointment_id}", response_model=AppointmentResponse)
def update_appointment(appointment_id: int, appointment: AppointmentUpdate, db: Session = Depends(get_db)):
    return appointment_service.update_appointment(db, appointment_id, appointment)

# Eliminar una cita existente
@router.delete("/{appointment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_appointment(appointment_id: int, db: Session = Depends(get_db)   ):
    appointment_service.delete_appointment(db, appointment_id)
    return None 