# 📊 Finanças - Python - Bootcamp Ser+Tech | Ada & Núclea

Projeto final da disciplina de Python do bootcamp Ser+Tech, uma parceria da Ada com a Nuclea, ministrada pelo Professor Daniel Vieira (github.com/danielgundim)

## 🗒️Descrição do projeto:

1. Construiremos uma aplicação em __Python__ que cadastre clientes e colete dados das ações do mercado financeiro da carteira desse cliente e as armazene num banco de dados.     
2. Será utilizado o banco de dados __PostgreSQL__ para conexão com a aplicação.     
3. Com os dados armazenados realizaremos análises para avaliar o desempenho de uma carteira durante um período definido.      
4. A aplicação deve permitir interação com o usuário através do prompt de comando num menu interativo, onde ele escolherá quais ações irão compor sua carteira, atualizar seus dados de cadastro e acompanhar os rendimentos dos seus ativos.      
5. Devemos cadastrar estes dados do cliente:      
     * Nome, CPF, data de nascimento, celular, CEP e número de residência, estado civil e valor do patrimônio.
6. Para as informações de CPF consumiremos a  [API ViaCep](https://viacep.com.br/).    
7. Devemos cadastrar estes dados da carteira do cliente:
     * Ação, nome da ação, data e valor de compra. 
8. Como regras de negócios da aplicação devemos checar se o CPF do cliente é válido e buscar de forma automática o endereço completo do cliente através do CEP.
9. A aplicação deverá exibir à pessoa usuária a opção de acompanhar o desempenho da carteira frente ao índice __Ibovespa__ através da biblioteca __Matplotlib__.
10. O código deverá ser construído com a utilização de testes unitários.
11. Essa aplicação utilizará boas práticas em Python e todo o conteúdo aprendido durante o módulo e o coding tank. O código da aplicação deverá ser armazenado no __Github__ do aluno que será criado durante o módulo.

## 🌳 Estrutura dos diretórios:




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

