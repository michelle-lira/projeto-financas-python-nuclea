"""
# REFERÊNCIAS - REMOVER NO FINAL

import os
from dotenv import load_dotenv
from utils import cep, data, funcoes_auxiliares, valida_cpf, valida_rg
from models.clientes import Cliente
from models.acoes import Acao
from models.analise_carteira import realizar_analise_carteira, acompanhar_desempenho_ibovespa

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Agora você pode acessar as variáveis de ambiente usando os.getenv("NOME_DA_VARIAVEL")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")


def cadastrar_cliente():
    # Implementação para cadastrar um cliente
    pass


def cadastrar_acao():
    # Implementação para cadastrar uma ação
    pass


def atualizar_dados_cadastro_cliente():
    # Implementação para atualizar os dados de cadastro do cliente
    pass


def realizar_analise_carteira():
    # Implementação para realizar a análise da carteira
    cliente_id = input("Digite o ID do cliente: ")
    realizar_analise_carteira(cliente_id)


def acompanhar_rendimentos():
    # Implementação para acompanhar os rendimentos
    pass


def imprimir_relatorio_carteira():
    # Implementação para imprimir o relatório da carteira
    pass


def acompanhar_desempenho_ibovespa():
    # Implementação para acompanhar o desempenho da carteira frente ao Ibovespa
    # Vamos criar um exemplo simples usando a biblioteca Matplotlib
    # Essa função deve mostrar um gráfico com os rendimentos da carteira e do Ibovespa
    import matplotlib.pyplot as plt

    # Dados de exemplo
    meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
    rendimentos_carteira = [10, 20, 30, 40, 50, 60]
    rendimentos_ibovespa = [5, 15, 25, 35, 45, 55]

    # Plotando o gráfico
    plt.plot(meses, rendimentos_carteira, label='Carteira')
    plt.plot(meses, rendimentos_ibovespa, label='Ibovespa')
    plt.xlabel('Mês')
    plt.ylabel('Rendimento')
    plt.title('Desempenho da Carteira vs Ibovespa')
    plt.legend()
    plt.show()


def sair():
    # Implementação para sair da aplicação
    pass


def menu_principal():
    while True:
        print("=" * 31)
        print("======= Menu Principal =======")
        print("=" * 31)
        print("1 - Cadastrar Cliente")
        print("2 - Cadastrar Ação")
        print("3 - Atualizar Dados de Cadastro do Cliente")
        print("4 - Realizar Análise da Carteira")
        print("5 - Acompanhar Rendimentos")
        print("6 - Imprimir Relatório da Carteira")
        print("7 - Acompanhar Desempenho frente ao Ibovespa")
        print("8 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            cadastrar_acao()
        elif opcao == "3":
            atualizar_dados_cadastro_cliente()
        elif opcao == "4":
            realizar_analise_carteira()
        elif opcao == "5":
            acompanhar_rendimentos()
        elif opcao == "6":
            imprimir_relatorio_carteira()
        elif opcao == "7":
            acompanhar_desempenho_ibovespa()
        elif opcao == "8":
            sair()
            break
        else:
            print("Opção inválida. Tente novamente.")
"""

from utils.cep import valida_cep
from utils.data import valida_data_nascimento
from utils.funcoes_auxiliares import formata_texto, retorna_menu_principal
from utils.valida_cpf import valida_cpf
from utils.valida_rg import valida_rg


# A variável com a lista de clientes está fora do ‘loop’ para não ser resetada a cada iteração
clientes = []


def main():

    # O validador é a variável que vai controlar o loop do menu principal
    validador = True

    while validador:
        print(
            "Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea. Selecione uma das opções abaixo:")
        print("1 - Cliente")
        # Deve alterar o "Cadastrar cliente" por "Cliente" e exibir submenu com as devidas opções do CRUD.
        print("2 - Cadastrar ação")
        print("3 - Realizar análise da carteira")
        print("4 - Imprimir relatório da carteira")
        print("5 - Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            pass
            # cliente = Cliente()
            # print("1 - Cadastrar Cliente")
            #     cliente.cadastrar_cliente()
            # print("2 - Consultar Cliente")
            # print("3 - Alterar Cliente")
            # print("4 - Deletar Cliente")
            # print("Informe os dados do cliente: ")
            # cliente = {
            #     "nome": formata_texto(input("Nome: ")),
            #     "cpf": valida_cpf(),
            #     "rg": valida_rg(),
            #     "data_nascimento": valida_data_nascimento(),
            #     "endereco": valida_cep(),
            #     "numero_casa": input("Número casa: ")
            # }
            # O append adiciona o cliente na lista de clientes
            # clientes.append(cliente)
            # print(clientes)
            # #Corrigir o validador para evitar duplicidade do retorna_menu_principal
            # validador = retorna_menu_principal()

        elif opcao == "2":
            pass
            # Preencher a função da ordem.
        elif opcao == "3":
            pass
        elif opcao == "4":
            pass
        elif opcao == "5":
            print("Obrigado por utilizar o sistema de gerenciamento de carteira de ações da Nuclea. Até a próxima!")
            validador = False
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
