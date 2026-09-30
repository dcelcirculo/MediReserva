from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.specialty import Specialty
from app.schemas.specialty_schema import CreateSpecialty, SpecialtyUpdate


def create_specialty(db: Session, datos: CreateSpecialty) -> Specialty:
    specialty = Specialty(name=datos.name)
    db.add(specialty)
    db.commit()
    db.refresh(specialty)
    return specialty


def list_specialties(db: Session) -> list[Specialty]:
    return db.query(Specialty).all()


def get_specialty_by_id(db: Session, specialty_id: int) -> Specialty:
    specialty = db.query(Specialty).filter(Specialty.id == specialty_id).first()
    if not specialty:
        raise HTTPException(status_code=404, detail="Especialidad no encontrada")
    return specialty


def update_specialty(db: Session, specialty_id: int, datos: SpecialtyUpdate) -> Specialty:
    specialty = get_specialty_by_id(db, specialty_id)
    specialty.name = datos.name
    db.commit()
    db.refresh(specialty)
    return specialty


def delete_specialty(db: Session, specialty_id: int) -> None:
    specialty = get_specialty_by_id(db, specialty_id)
    db.delete(specialty)
    db.commit()