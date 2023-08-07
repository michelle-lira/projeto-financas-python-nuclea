import psycopg2
from dotenv import load_dotenv
import os


class BancoDeDados:
    def __init__(self):
        # Carrega as variáveis de ambiente do arquivo .env
        load_dotenv()

        # Obtém as variáveis de ambiente
        self.db_host = os.getenv("DB_HOST")
        self.db_port = os.getenv("DB_PORT")
        self.db_name = os.getenv("DB_NAME")
        self.db_user = os.getenv("DB_USER")
        self.db_password = os.getenv("DB_PASSWORD")

        self.conn = None

    def conectar(self):
        # Cria a conexão com o banco de dados PostgreSQL
        self.conn = psycopg2.connect(
            host=self.db_host,
            port=self.db_port,
            database=self.db_name,
            user=self.db_user,
            password=self.db_password
        )

    def executar_query(self, query):
        if self.conn is None:
            raise ValueError("Conexão não estabelecida. Chame o método 'conectar' primeiro.")

        # Crie um cursor para executar consultas SQL
        cur = self.conn.cursor()

        # Execute a consulta
        cur.execute(query)

        # Faça o commit das alterações (se necessário)
        self.conn.commit()

        # Feche o cursor
        cur.close()

    def testar_conexao(self):
        try:
            # Tente se conectar
            self.conectar()

            # Se chegou até aqui, a conexão foi bem-sucedida
            print("Conexão bem-sucedida ao banco de dados!")

        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {str(e)}")

        finally:
            # Certifique-se de fechar a conexão, mesmo se ocorrer um erro
            self.fechar_conexao()

    def fechar_conexao(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None


# Exemplo de uso
if __name__ == "__main__":
    banco = BancoDeDados()
    # banco.conectar()
    banco.testar_conexao()

    # query = "INSERT INTO sua_tabela (coluna1, coluna2) VALUES (%s, %s);"
    # values = ("Valor1", "Valor2")
    # banco.executar_query(query, values)
    #
    #
    # banco.fechar_conexao()
