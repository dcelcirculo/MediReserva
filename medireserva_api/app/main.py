from fastapi import FastAPI
from app.database import Base, engine

from app.models import appointment, schedule, doctor, user

from app.routers import appointment_router, schedule_router, doctor_router, auth_router

Base.metadata.create_all(bind=engine) # Create all tables in the database based on the models

app = FastAPI(title="Medical Booking API", description="Backend API for managing medical appointments.")

@app.get("/")
def root():
    return {"message": "Welcome to the Medical Booking API"}