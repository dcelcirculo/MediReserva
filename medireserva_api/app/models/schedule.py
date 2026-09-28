from sqlalchemy import Column, ForeignKey, Integer, String, Time
from sqlalchemy.orm import relationship
from app.database import Base

class Schedule(Base):
    __tablename__ = "schedule"
    
    id = Column(Integer, primary_key=True)
    
    # ID del doctor al que pertenece el horario
    doctor_id = Column(
        Integer,
        ForeignKey("doctor.id"),
        nullable=False,
        index=True
    )
    day = Column(String, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    
    # Relación con el doctor al que pertenece el horario
    doctor = relationship(
        "Doctor",
        back_populates="schedules"
    )
    
    # Relación con las citas asociadas a este horario
    appointments = relationship(
        "Appointment",
        back_populates="schedule"
    )