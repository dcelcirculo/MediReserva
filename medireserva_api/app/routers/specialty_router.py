from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.schemas.specialty_schema import CreateSpecialty, SpecialtyResponse, SpecialtyUpdate
from app.services import specialty_service

router = APIRouter(prefix="/specialties", tags=["specialties"])


@router.get("/", response_model=list[SpecialtyResponse])
def list_specialties(db: Session = Depends(get_db)):
    return specialty_service.list_specialties(db)


@router.get("/{specialty_id}", response_model=SpecialtyResponse)
def get_specialty(specialty_id: int, db: Session = Depends(get_db)):
    return specialty_service.get_specialty_by_id(db, specialty_id)


@router.post("/", response_model=SpecialtyResponse, status_code=status.HTTP_201_CREATED)
def create_specialty(specialty: CreateSpecialty, db: Session = Depends(get_db)):
    return specialty_service.create_specialty(db, specialty)


@router.put("/{specialty_id}", response_model=SpecialtyResponse)
def update_specialty(specialty_id: int, specialty: SpecialtyUpdate, db: Session = Depends(get_db)):
    return specialty_service.update_specialty(db, specialty_id, specialty)


@router.delete("/{specialty_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_specialty(specialty_id: int, db: Session = Depends(get_db)):
    specialty_service.delete_specialty(db, specialty_id)
    return None