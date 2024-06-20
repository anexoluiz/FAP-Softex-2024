CREATE TABLE
    membros (membro_id INT PRIMARY KEY, nome VARCHAR(20), cargo VARCHAR(20), genero char(1));

CREATE TABLE
    tarefas (
        tarefa_id INT PRIMARY KEY,
        descricao VARCHAR(50),
        data_ini date,
        data_fim date,
        membro_id INT,
        FOREIGN KEY (membro_id) REFERENCES membros (membro_id)
    );

INSERT into
    membros (membro_id, nome, cargo, genero)
VALUES
    (3, 'Luiz', 'Analista', 'F');

/* change cargo from varchar20 to varchar60
pois alguns dos cargos abaixo possuem mais
de 20 caracteres */
ALTER TABLE membros MODIFY cargo VARCHAR(60);

INSERT into
    membros (membro_id, nome, cargo, genero)
VALUES
    (4, 'João Silva', 'Desenvolvedor', 'M'),
    (5, ' Maria Santos ', 'Analista de Banco de Dados', 'F'),
    (6, 'Pedro Oliveira', ' Engenheiro de Software', 'M'),
    (7, 'Luiz Carlos', 'Engenheiro de Software', 'F'),
    (8, 'Ana Costas', 'Administrador de Redes', 'F');

/* Inserindo algumas tarefas */
INSERT INTO
    tarefas (tarefa_id, descricao, data_ini, data_fim, membro_id)
VALUES
    (1, 'Analisar requisitos novo projeto', '2024-06-19', '2024-06-30', 3),
    (2, 'Desenvolver funcionalidades sistema', '2024-06-20', '2024-07-01', 4),
    (3, 'Otimizar consultas SQL desempenho', '2024-06-21', '2024-07-02', 5),
    (4, 'Arquitetar estrutura novo módulo', '2024-06-22', '2024-07-03', 6),
    (5, 'Revisão código padrões qualidade', '2024-06-23', '2024-07-04', 7),
    (6, 'Configurar switches expansão rede', '2024-06-24', '2024-07-05', 8);

/* Corrigindo o sexo dos membros 3 e 7 */
UPDATE membros
SET
    genero = 'M'
WHERE
    membro_id = 7
    OR membro_id = 3;

/* Listando os nomes e tarefas atribuidas */
SELECT
    membros.nome,
    tarefas.descricao
FROM
    membros
    INNER JOIN tarefas ON membros.membro_id = tarefas.membro_id