/* Criando e selecionando a nova database */
CREATE DATABASE clinica;

USE clinica;

CREATE TABLE
    medicos (
        crm INT PRIMARY KEY,
        nome VARCHAR(60),
        genero CHAR(1),
        telefone_fixo INT,
        telefone_movel INT,
        rua VARCHAR(100),
        numero INT,
        bairro VARCHAR(50),
        cep INT,
        cidade VARCHAR(50),
        estado CHAR(2),
        especialidade VARCHAR(50)
    );

CREATE TABLE
    pacientes (cpf INT PRIMARY KEY, nome VARCHAR(60), genero CHAR(1), telefone_fixo INT, telefone_movel INT, nascimento DATE);

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