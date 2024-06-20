/* Criando a base de dados
para incluir as tabelas */
CREATE DATABASE startup;

/* Selecionando a base de dados */
USE startup;

/* Criando as tabelas de membros e tarefas */
CREATE TABLE
    membros (membro_id INT PRIMARY KEY, nome VARCHAR(20), cargo VARCHAR(20));

CREATE TABLE
    tarefas (
        tarefa_id INT PRIMARY KEY,
        descricao VARCHAR(50),
        membro_id INT,
        FOREIGN KEY (membro_id) REFERENCES membros (membro_id)
    );

/* Inserindo dados nas duas tabelas */
INSERT INTO
    membros (membro_id, nome, cargo)
VALUES
    (1, "Paulo", "Programador 1");

INSERT INTO
    tarefas (tarefa_id, descricao, membro_id)
VALUES
    (1, "Criar a classe produto", 1);

/* Selecionando os dados das tabelas */
SELECT
    nome,
    cargo
FROM
    membros;

SELECT
    descricao
FROM
    tarefas;

/* Selecionando os dados das duas tabelas */
SELECT
    membros.nome,
    tarefas.descricao
FROM
    membros
    INNER JOIN tarefas ON membro.membro_id = tarefas.membro_id