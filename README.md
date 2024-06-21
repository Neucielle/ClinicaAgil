##  📘ClinicaAgil


# ⏰Sistema de Gerenciamento de Consultas Médicas

Este sistema de backend foi desenvolvido em Python para facilitar o gerenciamento de pacientes e consultas médicas, utilizando um banco de dados SQL Server para armazenamento persistente dos dados. As principais funcionalidades incluem:

* Cadastro de Pacientes: Permite registrar novos pacientes no sistema, armazenando informações como nome e informação de contato (telefone).

* Marcação de Consultas: Funcionalidade que permite agendar consultas para os pacientes cadastrados. Cada consulta é associada a um paciente específico, data e hora marcadas, e especialidade.

* Cancelamento de Consultas: Oferece a capacidade de cancelar consultas previamente agendadas. O sistema garante a remoção adequada da consulta do banco de dados.

* Sair do Sistema: Opção para encerrar a sessão de uso do sistema de maneira segura, garantindo a integridade dos dados e fechamento adequado das conexões com o banco de dados.

Tecnologias Utilizadas:

![Python](https://img.shields.io/badge/python-3670A0?style=flat-square&logo=python&logoColor=ffdd54)
: Utilizado para desenvolvimento do backend, manipulação lógica e interação com o banco de dados.

![MicrosoftSQLServer](https://img.shields.io/badge/Microsoft%20SQL%20Server-CC2927?style=flat-square&logo=microsoft%20sql%20server&logoColor=white)
: Banco de dados relacional escolhido para armazenamento seguro e eficiente das informações dos pacientes e consultas.
