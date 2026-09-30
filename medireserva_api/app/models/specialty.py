from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.config.database import Base

class Specialty(Base):
    __tablename__ = "specialty"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    doctors = relationship(
        "Doctor",
        back_populates="specialty"
    )