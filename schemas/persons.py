from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class PersonBase(BaseModel):
    Nombre: str
    Primer_Apellido: str
    Segundo_Apellido: str
    Curp: str
    Puesto: Optional[str] = None 
    Jefe_ID: Optional[int] = None
    Direccion: Optional[str] = "Calle: ,No.Exteriror: ,No.Interior: ,Clonia: ,Municipio: , Estado: ,Pais:"
    Empleado_id: Optional[str] = None
    Estatus: bool
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime

class PersonCreate(PersonBase):
    pass

class PersonUpdate(PersonBase):
    pass

class Person(PersonBase):
    ID: int

    class Config:
        orm_mode = True
