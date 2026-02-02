CREATE DATABASE IF NOT EXISTS Frequencia_Inatel;
USE Frequencia_Inatel;

CREATE TABLE IF NOT EXISTS presenca(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    matricula VARCHAR(20),
    sala VARCHAR(50),
    materia VARCHAR(100),
    data_hora DATETIME
    );

SELECT * FROM presenca;