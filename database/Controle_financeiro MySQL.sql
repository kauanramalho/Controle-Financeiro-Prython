CREATE DATABASE controle_financeiro;
USE controle_financeiro;
SHOW TABLES;

CREATE TABLE movimentacoes (
	id INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(20) NOT NULL,
    descricao VARCHAR(100) NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    data_movimentacao DATE NOT NULL
    );

