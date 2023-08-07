# 📊 Finanças - Python - Bootcamp Ser+Tech | Ada & Núclea

Projeto final da disciplina de Python do bootcamp Ser+Tech, uma parceria da Ada com a Nuclea, ministrada pelo Professor Daniel Vieira (github.com/danielgundim)

## 🗒️Descrição do projeto:

1. Construiremos uma aplicação em __Python__ que cadastre clientes e colete dados das ações do mercado financeiro da carteira desse cliente e as armazene num banco de dados.     
2. Será utilizado o banco de dados __PostgreSQL__ para conexão com a aplicação.     
3. Com os dados armazenados realizaremos análises para avaliar o desempenho de uma carteira durante um período definido.      
4. A aplicação deve permitir interação com o usuário através do prompt de comando num menu interativo, onde ele escolherá quais ações irão compor sua carteira, atualizar seus dados de cadastro e acompanhar os rendimentos dos seus ativos.      
5. Devemos cadastrar estes dados do cliente:      
     * Nome, CPF, data de nascimento, celular, CEP, logradouro, número da residência, complemento, bairro, cidade e estado. __Obs: Adicionei telefone, email e valor do patrimônio aos atributos do cliente, fora do escopo do projeto.__
6. Para as informações de CPF consumiremos a  [API ViaCep](https://viacep.com.br/).    
7. Devemos cadastrar estes dados da carteira do cliente:
     * Ação, nome da ação, data e valor de compra. 
8. Como regras de negócios da aplicação devemos checar se o CPF do cliente é válido e buscar de forma automática o endereço completo do cliente através do CEP.
9. A aplicação deverá exibir à pessoa usuária a opção de acompanhar o desempenho da carteira frente ao índice __Ibovespa__ através da biblioteca __Matplotlib__.
10. O código deverá ser construído com a utilização de testes unitários.
11. Essa aplicação utilizará boas práticas em Python e todo o conteúdo aprendido durante o módulo e o coding tank. O código da aplicação deverá ser armazenado no __Github__ do aluno que será criado durante o módulo.

## 🌳 Estrutura dos diretórios:

├───projeto-financas-python-nuclea     
│     
├───models     
│   └───acao.py    
│   └───cliente.py     
│   └───endereco.py     
│   └───ordem_compra.py     
│   └───tabelas_intermediarias.py      
│       
├───repository       
│   └───banco_de_dados.py     
│    
├───scripts    
│   └───CRUD-banco-de-dados-nuclea.sql     
|   └───insert-tabela-endereco.sql     
|     
├───tests      
|     
└───utils     
│    └───cep.py     
|    └───data.py     
|    └───funcoes_auxiliares.py    
|    └───valida_cpf.py    
|    └───valida_rg.py    
|     
└───.env     
└───analise_carteira.py      
└───main.py      
└───README.md      
└───relatorio.py     
└───requirements


## Relacionamento entre as tabelas:

### Tabela Cliente:
A tabela **`Cliente`** tem um relacionamento com a tabela **`Endereco`**. O relacionamento é do tipo **muitos-para-um**. 
Isso significa que alguns clientes podem ter o mesmo endereço. O relacionamento é estabelecido pela coluna **`endereco_id`** na tabela **`Cliente`**, que é uma chave estrangeira que faz referência à coluna **`id`** na tabela **`Endereco`**. A tabela **`Endereco`** não tem uma coluna que faça referência à tabela **`Cliente`**. 

### Tabela Endereço:
A tabela **`Endereco`** tem uma relação bidirecional com a tabela **`Cliente`**. Isso significa que a tabela **`Cliente`** tem uma relação com a tabela **`Endereco`**, e a tabela **`Endereco`** tem uma relação com a tabela **`Cliente`**. A relação bidirecional é estabelecida pela propriedade **`endereco`** na classe **`Cliente`**, que é definida como um relacionamento com a classe **`Endereco`**, e pela propriedade **`clientes`** na classe **`Endereco`**, que é definida como um relacionamento com a classe **`Cliente`**.

### Tabela Ordem Compra:
A tabela **`OrdemCompra`** tem um relacionamento com a tabela **`Cliente`**. O relacionamento é do tipo **muitos-para-um**. Isso significa que muitas ordens de compra podem ser feitas por um único cliente. O relacionamento é estabelecido pela coluna **`cliente_id`** na tabela **`OrdemCompra`**, que é uma chave estrangeira que faz referência à coluna **`id`** na tabela **`Cliente`**. 

A tabela **`Cliente`** tem uma relação bidirecional com a tabela **`OrdemCompra`**. Isso significa que a tabela **`OrdemCompra`** tem uma relação com a tabela **`Cliente`**, e a tabela **`Cliente`** tem uma relação com a tabela **`OrdemCompra`**. A relação bidirecional é estabelecida pela propriedade **`ordens_compra`** na classe **`Cliente`**, que é definida como um relacionamento com a classe **`OrdemCompra`**, e pela propriedade **`cliente`** na classe **`OrdemCompra`**, que é definida como um relacionamento com a classe **`Cliente`**.

### Tabela Ação:
A tabela **`Acao`** tem um relacionamento com a tabela **`OrdemCompra`**. O relacionamento é do tipo **muitos-para-muitos**. Isso significa que muitas ordens de compra podem ter muitas ações, e muitas ações podem estar em muitas ordens de compra. O relacionamento é estabelecido pela tabela intermediária **`ordem_compra_acao`**, que contém as colunas **`ordem_compra_id`** e **`acao_id`**. Essas colunas são chaves estrangeiras que fazem referência às colunas **`id`** nas tabelas **`OrdemCompra`** e **`Acao`**, respectivamente. 

### Tabela Intermediária (Ordem-Compra-Ação):
**A tabela intermediária é definida como uma instância da classe Table do SQLAlchemy.** A propriedade **`ordens_compra`** na classe **`Acao`** é definida como um relacionamento secundário com a tabela intermediária, e a propriedade **`acoes`** na classe **`OrdemCompra`** é definida como um relacionamento secundário com a tabela intermediária.


## 🐍 Bibliotecas utilizadas:

Package            | Version
------------------ | ---------
certifi            | 2023.7.22
charset-normalizer | 3.2.0
Faker              | 0.7.4
idna               | 3.4
pip                | 23.2.1
psycopg2           | 2.9.6
python-dateutil    | 2.8.2
python-dotenv      | 1.0.0
python-utils       | 3.7.0
requests           | 2.31.0
setuptools         | 68.0.0
six                | 1.16.0
sqlalchemy         |
typing_extensions  | 4.7.1
urllib3            | 2.0.4
validate-docbr     | 1.10.0
wheel              | 0.40.0

