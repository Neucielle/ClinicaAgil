CREATE DATABASE Clinica;

USE Clinica;

CREATE TABLE Pacientes (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nome NVARCHAR(255) NOT NULL,
    telefone NVARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE Consultas (
    id INT IDENTITY(1,1) PRIMARY KEY,
    paciente_id INT,
    data DATE,
    hora TIME,
    especialidade NVARCHAR(255),
    FOREIGN KEY (paciente_id) REFERENCES Pacientes(id)
);
