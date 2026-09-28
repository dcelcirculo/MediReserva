from sqlalchemy import Column, Date, ForeignKey, Integer, String, Time
from sqlalchemy.orm import relationship
from app.database import Base

class Appointment(Base):
    __tablename__ = "appointment"
    
    id = Column(Integer, primary_key=True)
    
    # ID del doctor al que pertenece la cita
    doctor_id = Column(
        Integer,
        ForeignKey("doctor.id"),
        nullable=False,
        index=True
    )
    
    # ID del usuario (paciente) al que pertenece la cita
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )
    
    # ID del horario al que pertenece la cita
    schedule_id = Column(
        Integer, 
        ForeignKey("schedule.id"),
        nullable=False
    )
    appointment_date = Column(Date, nullable=False)
    appointment_time = Column(Time, nullable=False)
    status = Column(String, nullable=False)

    # Relación con el doctor al que pertenece la cita
    doctor = relationship(
        "Doctor",
        back_populates="appointments"
    )
    
    # Relación con el usuario (paciente) al que pertenece la cita
    patient = relationship(
        "User",
        back_populates="appointments"
    )
    
    # Relación con el horario al que pertenece la cita
    schedule = relationship(
        "Schedule",
        back_populates="appointments"
    )