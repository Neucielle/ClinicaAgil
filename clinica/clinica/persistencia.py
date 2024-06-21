from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

DATABASE_URI = 'mssql+pyodbc://Nancy:Wender1995#@LAPTOP-LO53ELLE/Clinica?driver=ODBC+Driver+17+for+SQL+Server'

engine = create_engine(DATABASE_URI)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

def inicializar_banco():
    Base.metadata.create_all(engine)

def salvar_paciente(session, nome, telefone):
    from .paciente import Paciente
    try:
        paciente = Paciente(nome=nome, telefone=telefone)
        session.add(paciente)
        session.commit()
        print("Paciente cadastrado com sucesso!")
    except IntegrityError:
        session.rollback()
        print(f"Número de telefone '{telefone}' já cadastrado. Não foi possível cadastrar o paciente. Tente cadastrar outro paciente.")

def salvar_consulta(session, paciente_id, data, hora, especialidade):
    from .consulta import Consulta
    consulta = Consulta(paciente_id=paciente_id, data=data, hora=hora, especialidade=especialidade)
    session.add(consulta)
    session.commit()

def carregar_pacientes(session):
    from .paciente import Paciente
    return session.query(Paciente).all()

def carregar_consultas(session):
    from .consulta import Consulta
    return session.query(Consulta).all()

def deletar_consulta(session, consulta_id):
    from .consulta import Consulta
    consulta = session.query(Consulta).filter_by(id=consulta_id).first()
    if consulta:
        session.delete(consulta)
        session.commit()
