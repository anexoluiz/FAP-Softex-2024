/* Criando e selecionando a nova database */
DROP DATABASE clinica;

CREATE DATABASE clinica;

USE clinica;

CREATE TABLE
    enderecos (
        endereco_id INT PRIMARY KEY NOT NULL,
        rua VARCHAR(100) NOT NULL,
        numero INT NOT NULL,
        complemento VARCHAR(100),
        bairro VARCHAR(100) NOT NULL,
        cep INT NOT NULL,
        cidade VARCHAR(100) NOT NULL,
        estado CHAR(2) NOT NULL
    );

CREATE TABLE
    medicos (
        crm INT PRIMARY KEY NOT NULL,
        nome VARCHAR(100) NOT NULL,
        genero CHAR(1) NOT NULL,
        telefone_fixo INT,
        telefone_movel INT NOT NULL,
        especialidade VARCHAR(100) NOT NULL,
        endereco_id INT NOT NULL,
        FOREIGN KEY (endereco_id) REFERENCES enderecos (endereco_id)
    );

CREATE TABLE
    pacientes (
        cpf BIGINT PRIMARY KEY NOT NULL,
        nome VARCHAR(100) NOT NULL,
        genero CHAR(1) NOT NULL,
        telefone_fixo INT,
        telefone_movel INT NOT NULL,
        nascimento DATE NOT NULL
    );

CREATE TABLE
    consultas (
        consulta_id INT PRIMARY KEY NOT NULL,
        datahora DATETIME NOT NULL,
        diagnostico VARCHAR(100) NOT NULL,
        observacoes VARCHAR(100),
        crm INT NOT NULL,
        cpf BIGINT NOT NULL,
        FOREIGN KEY (crm) REFERENCES medicos (crm),
        FOREIGN KEY (cpf) REFERENCES pacientes (cpf)
    );

/* Inserindo dados aleatórios */
INSERT INTO
    enderecos
VALUES
    (1, 'Rua A', 100, 'Apartamento 101','Bairro A', 12345678, 'Cidade A', 'SP'),
    (2, 'Rua B', 200, 'Apartamento 102','Bairro B', 87654321, 'Cidade B', 'RJ'),
    (3, 'Rua C', 300, 'Apartamento 103','Bairro C', 45678912, 'Cidade C', 'MG');

INSERT INTO
    medicos
VALUES
    (123456, 'Médico A', 'M', 11111111, 22222222, 'Cardiologista', 1),
    (234567, 'Médico B', 'F', 33333333, 44444444, 'Pediatra', 2),
    (345678, 'Médico C', 'M', 55555555, 66666666, 'Ortopedista', 3);

INSERT INTO
    pacientes
VALUES
    (11111111111, 'Paciente A', 'M', 77777777, 88888888, '1990-01-01'),
    (22222222222, 'Paciente B', 'F', 99999999, 10101010, '1995-02-02'),
    (33333333333, 'Paciente C', 'M', 12121212, 13131313, '2000-03-03');

INSERT INTO
    consultas
VALUES
    (1, '2021-01-01 08:00:00', 'Diagnóstico A', 'Observações A', 123456, 11111111111),
    (2, '2021-02-02 09:00:00', 'Diagnóstico B', 'Observações B', 234567, 22222222222),
    (3, '2021-03-03 10:00:00', 'Diagnóstico C', 'Observações C', 345678, 33333333333);