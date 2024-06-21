from sqlalchemy import Column, Integer, Date, Time, ForeignKey, String
from sqlalchemy.orm import relationship
from .persistencia import Base

class Consulta(Base):
    __tablename__ = 'consultas'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    paciente_id = Column(Integer, ForeignKey('pacientes.id'), nullable=False)
    data = Column(Date, nullable=False)
    hora = Column(Time, nullable=False)
    especialidade = Column(String(255), nullable=False)
    paciente = relationship("Paciente")
