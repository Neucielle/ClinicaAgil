from sqlalchemy import Column, Integer, String
from .persistencia import Base

class Paciente(Base):
    __tablename__ = 'pacientes'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    telefone = Column(String(20), nullable=False)
