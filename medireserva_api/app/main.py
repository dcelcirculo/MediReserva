from fastapi import FastAPI
from app.config.database import Base, engine

from app.models import appointment, schedule, doctor, user

from app.routers import appointment_router, schedule_router, doctor_router, auth_router

Base.metadata.create_all(bind=engine) # crea todas las tablas en la base de datos según los modelos

app = FastAPI(title="Medical Booking API", description="Backend API for managing medical appointments.")

@app.get("/")
def root():
    return {"message": "Welcome to the Medical Booking API"}

app.include_router(appointment_router.router)
app.include_router(schedule_router.router)
app.include_router(doctor_router.router)
app.include_router(auth_router.router)