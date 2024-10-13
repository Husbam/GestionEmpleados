from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base

class Person(Base):
    __tablename__ = "Empleados"
    
    ID = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(255))
    Primer_Apellido = Column(String(255))
    Segundo_Apellido = Column(String(255))
    Curp = Column(String(18)) 
    Puesto = Column(String(100))
    Jefe_ID = Column(Integer, ForeignKey('Empleados.ID'), nullable=True)
    Direccion = Column(String(255))
    Empleado_id = Column(String(12))
    Estatus = Column(Boolean, default=False)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)

    #Autoreferencia al jefe
    jefe = relationship('Person', remote_side=[ID], backref='subordinados')