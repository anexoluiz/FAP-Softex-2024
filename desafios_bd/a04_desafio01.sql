/* Criando e selecionando a nova database */
DROP TABLE demo;

-- CREATE DATABASE clinica;

-- USE clinica;

CREATE TABLE
    enderecos (
        endereco_id INT PRIMARY KEY,
        rua VARCHAR(100),
        numero INT,
        bairro VARCHAR(50),
        cep INT,
        cidade VARCHAR(50),
        estado CHAR(2)
    );

CREATE TABLE
    medicos (
        crm INT PRIMARY KEY,
        nome VARCHAR(60),
        genero CHAR(1),
        telefone_fixo INT,
        telefone_movel INT,
        endereco_id INT,
        especialidade VARCHAR(50),
        FOREIGN KEY (endereco_id) REFERENCES enderecos (endereco_id)
    );

CREATE TABLE
    pacientes (
        cpf INT PRIMARY KEY,
        nome VARCHAR(60),
        genero CHAR(1),
        telefone_fixo INT,
        telefone_movel INT,
        nascimento DATE
    );

CREATE TABLE
    consultas (
        consulta_id INT PRIMARY KEY,
        datahora DATETIME,
        diagnóstico VARCHAR(100),
        crm INT,
        cpf INT,
        FOREIGN KEY (crm) REFERENCES medicos (crm),
        FOREIGN KEY (cpf) REFERENCES pacientes (cpf)
    );

/* Inserindo dados aleatórios */
INSERT INTO
    enderecos
VALUES
    (1, 'Rua A', 100, 'Bairro A', 12345678, 'Cidade A', 'SP'),
    (2, 'Rua B', 200, 'Bairro B', 87654321, 'Cidade B', 'RJ'),
    (3, 'Rua C', 300, 'Bairro C', 45678912, 'Cidade C', 'MG');

INSERT INTO
    medicos
VALUES
    (123456, 'Médico A', 'M', 11111111, 22222222, 1, 'Cardiologista'),
    (234567, 'Médico B', 'F', 33333333, 44444444, 2, 'Pediatra'),
    (345678, 'Médico C', 'M', 55555555, 66666666, 3, 'Ortopedista');

INSERT INTO
    pacientes
VALUES
    (11111111111, 'Paciente A', 'M', 77777777, 88888888, '1990-01-01'),
    (22222222222, 'Paciente B', 'F', 99999999, 10101010, '1995-02-02'),
    (33333333333, 'Paciente C', 'M', 12121212, 13131313, '2000-03-03');

INSERT INTO
    consultas
VALUES
    (1, '2021-01-01 08:00:00', 'Consulta A', 123456, 11111111111),
    (2, '2021-02-02 09:00:00', 'Consulta B', 234567, 22222222222),
    (3, '2021-03-03 10:00:00', 'Consulta C', 345678, 33333333333);