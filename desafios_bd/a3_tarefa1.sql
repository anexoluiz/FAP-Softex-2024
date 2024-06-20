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

/* Incluindo coluna genero na tabela membros */
ALTER TABLE membros
ADD genero CHAR(1);

/* Incluindo colunas data_inicio e data_fim na tabela tarefas */
ALTER TABLE tarefas
ADD data_inicio DATE,
ADD data_finalizacao DATE;

/* Alterando o genero do membro Paulo */
UPDATE membros
SET
    genero = "M"
WHERE
    membro_id = 1;

UPDATE tarefas
SET
    data_inicio = "2024-06-01",
    data_finalizacao = "2024-06-15"
WHERE
    tarefa_id = 1;

/* Inserindo Maria na tabela membros */
INSERT INTO
    membros (membro_id, nome, cargo, genero)
VALUES
    (2, "Maria", "Programador 2", "F");

/* Buscando todos os membros do sexo feminino */
SELECT
    *
FROM
    membros
WHERE
    genero = "F";

