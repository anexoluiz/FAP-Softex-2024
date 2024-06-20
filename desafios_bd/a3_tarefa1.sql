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

/* Alterando o nome do membro 1 */
UPDATE membros
SET
    nome = "Andre Luiz"
WHERE
    membro_id = 1;

/* Removendo o membro 1 */
DELETE FROM membros
WHERE
    membro_id = 1;

/* Alterando o tamanho da coluna cargo para 50 */
ALTER TABLE membros
MODIFY COLUMN cargo VARCHAR(50);

/* Inserindo membros e tarefas */
INSERT INTO
    membros (membro_id, nome, cargo, genero)
VALUES
    (3, "João Silva", "Desenvolvedor Full Stack", "M"),
    (4, "Maria Santos", "Analista de Banco de Dados", "F"),
    (5, "Pedro Oliveira", "Engenheiro de Software", "M"),
    (6, "Ana Costa", "Administrador de Redes", "F"),
    (7, "Carlos Souza", "Especialista em Segurança da Informação", "M");

INSERT INTO
    tarefas (tarefa_id, descricao, membro_id, data_inicio, data_finalizacao)
VALUES
    (2, "Desenvolver novo módulo de login para o sistema", 3, "2024-06-01", "2024-06-15"),
    (3, "Realizar manutenção preventiva nos servidores", 5, "2024-06-01", "2024-06-15"),
    (4, "Criar documentação técnica do projeto XYZ", 6, "2024-06-01", "2024-06-15"),
    (5, "Testar e validar integração com API externa", 4, "2024-06-01", "2024-06-15"),
    (6, "Implementar melhorias na interface do usuário", 7, "2024-06-01", "2024-06-15");

/* Promovendo Ana Costa para Administrador de Rede Senior */
UPDATE membros
SET
    cargo = "Administrador de Rede Senior"
WHERE
    nome = "Ana Costa";

SELECT
    membros.nome,
    membros.cargo,
    tarefas.descricao,
    tarefas.data_inicio,
    tarefas.data_finalizacao
FROM
    membros
    INNER JOIN tarefas ON membros.membro_id = tarefas.membro_id;