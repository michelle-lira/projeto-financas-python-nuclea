-- -- Cria tabela 'endereco'
-- CREATE TABLE endereco (
--     id SERIAL PRIMARY KEY,
--     cep VARCHAR(12) NOT NULL,
--     logradouro VARCHAR(12) NOT NULL,
--     bairro VARCHAR(12) NOT NULL,
--     cidade VARCHAR(12) NOT NULL,
--     estado VARCHAR(2) NOT NULL,
--     pais VARCHAR(30) NOT NULL
-- );

-- -- Cria tabela 'cliente'
-- CREATE TABLE cliente (
--     id SERIAL PRIMARY KEY,
--     nome VARCHAR(200) NOT NULL,
--     cpf VARCHAR(15) NOT NULL,
--     data_nascimento VARCHAR(10) NOT NULL,
--     telefone VARCHAR(15) NOT NULL,
--     email VARCHAR(50) NOT NULL,
--     endereco_id INTEGER NOT NULL REFERENCES endereco(id),
--     complemento_residencia VARCHAR(40),
--     numero_residencia VARCHAR(10) NOT NULL,
--     patrimonio_liquido NUMERIC(20, 2) NOT NULL,
--     data_cadastro VARCHAR(10) NOT NULL,
--     cliente_id INTEGER NOT NULL REFERENCES public.cliente (id) ON DELETE CASCADE, 
--     FOREIGN KEY (endereco_id) REFERENCES endereco(id)
-- );

-- -- Cria tabela 'acao'
-- CREATE TABLE acao (
--     id SERIAL PRIMARY KEY,
--     codigo_acao VARCHAR(10) NOT NULL,
--     nome_empresa VARCHAR(30) NOT NULL,
--     preco FLOAT(10) NOT NULL
-- );

-- -- Cria tabela 'ordem_compra'
-- CREATE TABLE ordem_compra (
--     id SERIAL PRIMARY KEY,
--     ticket SERIAL NOT NULL,
--     cliente_id INTEGER NOT NULL REFERENCES cliente(id),
--     quantidade INTEGER NOT NULL,
--     valor_total FLOAT(20) NOT NULL
-- );

-- -- Cria tabela 'ordem_compra_acao'
-- CREATE TABLE ordem_compra_acao (
--     ordem_compra_id INTEGER REFERENCES ordem_compra(id),
--     acao_id INTEGER REFERENCES acao(id)
-- );

-- ALTER TABLE endereco ALTER COLUMN bairro TYPE VARCHAR(30);

-- ALTER TABLE endereco ALTER COLUMN cidade TYPE VARCHAR(30);
-- ALTER TABLE endereco ALTER COLUMN logradouro TYPE VARCHAR(50);