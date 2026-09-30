from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.config.database import Base

class Doctor(Base):
    __tablename__ = "doctor"
    
    id = Column(Integer, primary_key=True)
    
    # ID del usuario al que pertenece el doctor
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        unique=True, #Evitamos crear 2 perfiles medicos para el mismo usuario
        index=True # Creamos un índice para mejorar la búsqueda por user_id
    )
    specialty = Column(String, nullable=False)
    
    # Relación con el usuario al que pertenece el doctor
    user = relationship(
        "User",
        back_populates="doctor"
    )
    
    # Relación con las citas del doctor
    appointments = relationship(
        "Appointment",
        back_populates="doctor"
    )
    
    # Relación con los horarios del doctor
    schedules = relationship(
        "Schedule",
        back_populates="doctor"
    )