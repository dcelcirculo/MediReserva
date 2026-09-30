from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.user import User
from app.schemas.user_schema import CreateUser
from app.auth.security import hash_password

# Crear un nuevo usuario
def create_user(db: Session, datos: CreateUser) -> User:
    actual_user = db.query(User).filter(User.email == datos.email).first()
    if actual_user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    
    new_user = User(
        name=datos.name,
        email=datos.email,
        password_hash=hash_password(datos.password)
    )
    
    db.add(new_user)
    db.commit() 
    db.refresh(new_user)
    return new_user
        
# Listar todos los usuarios
def list_users(db: Session):
    return db.query(User).all()

# Obtener un usuario por su ID
def get_user_by_id( db: Session, user_id: int) -> User:
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

# Eliminar usuario
def delete_user_by_id(db: Session, user_id: int) -> None:
    user = get_user_by_id(db, user_id)
    db.delete(user)
    db.commit()
    return {"detail": "Usuario eliminado correctamente"}

# Actualizar usuario
def update_user(db: Session, user_id: int, datos: CreateUser) -> User:
    user = get_user_by_id(db, user_id)
    user.name = datos.name
    user.email = datos.email
    user.password_hash = hash_password(datos.password)
    db.commit()
    db.refresh(user)
    return user