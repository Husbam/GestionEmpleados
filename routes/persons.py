from fastapi import APIRouter,HTTPException,Depends,Request
from sqlalchemy.orm import Session
import crud.persons,config.db,schemas.persons,models.persons
from typing import List
from sqlalchemy import func


person = APIRouter()

models.persons.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@person.get("/persons/", response_model=List[schemas.persons.Person], tags=["Empleados"])
def read_persons(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_persons= crud.persons.get_persons(db=db, skip=skip, limit=limit)
    return db_persons

@person.post("/person/{ID}", response_model=schemas.persons.Person, tags=["Empleados"])
def read_person(ID: int, db: Session = Depends(get_db)):
    db_person= crud.persons.get_person(db=db, ID=ID)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return db_person

@person.post("/persons/", response_model=schemas.persons.Person, tags=["Empleados"])
def create_person(person: schemas.persons.PersonCreate, db: Session = Depends(get_db)):
    db_person = crud.persons.get_person_by_Nombre(db, Nombre=person.Nombre)
    if db_person:
        raise HTTPException(status_code=400, detail="Empleado existente, intenta nuevamente")
    return crud.persons.create_person(db=db, person=person)

@person.put("/person/{ID}", response_model=schemas.persons.Person, tags=["Empleados"])
def update_person(ID: int, person: schemas.persons.PersonUpdate, db: Session = Depends(get_db)):
    db_person = crud.persons.update_person(db = db, ID = ID, person = person)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Empleados no existente, no esta actualizado")
    return db_person

