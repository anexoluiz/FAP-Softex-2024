/* Criando e selecionando a nova database */
CREATE DATABASE clinica;

USE clinica;

CREATE TABLE
    medicos (
        crm INT PRIMARY KEY,
        nome VARCHAR(60),
        genero CHAR(1),
        telefone INT,
        endereco VARCHAR(150),
        especialidade VARCHAR(50)
    );

CREATE TABLE
    pacientes (cpf INT PRIMARY KEY, nome VARCHAR(60), genero CHAR(1), telefone INT, nascimento DATE);

CREATE TABLE
    consultas (
        consulta_id INT PRIMARY KEY,
        datahora DATETIME,
        diagnóstico VARCHAR(100),
        crm INT,
        cpf INT,
        FOREIGN KEY (crm) REFERENCES medicos (crm),
        FOREIGN KEY (cpf) REFERENCES pacientes (cpf)
    )