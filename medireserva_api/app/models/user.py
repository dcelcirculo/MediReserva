from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)
    rol = Column(String, nullable=False, default="patient")

    # Relación con el doctor asociado al usuario (si existe)
    doctor = relationship(
        "Doctor",
        back_populates="user",
        uselist=False
    )

    # Relación con las citas del usuario (paciente)
    appointments = relationship(
        "Appointment",
        back_populates="patient"
    )