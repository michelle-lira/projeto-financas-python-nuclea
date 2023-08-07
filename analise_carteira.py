"""
import matplotlib.pyplot as plt

def realizar_analise_carteira(cliente_id):
    # Implementação para realizar a análise da carteira
    # Aqui você pode implementar as análises que julgar relevantes
    # Exemplo simples: calcular o rendimento total da carteira do cliente
    # e exibir na tela
    pass

def acompanhar_desempenho_ibovespa():
    # Implementação para acompanhar o desempenho da carteira frente ao Ibovespa
    # Vamos criar um exemplo simples usando a biblioteca Matplotlib
    # Essa função deve mostrar um gráfico com os rendimentos da carteira e do Ibovespa
    meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
    rendimentos_carteira = [10, 20, 30, 40, 50, 60]  # Dados de exemplo
    rendimentos_ibovespa = [5, 15, 25, 35, 45, 55]   # Dados de exemplo

    # Plotando o gráfico
    plt.plot(meses, rendimentos_carteira, label='Carteira')
    plt.plot(meses, rendimentos_ibovespa, label='Ibovespa')
    plt.xlabel('Mês')
    plt.ylabel('Rendimento')
    plt.title('Desempenho da Carteira vs Ibovespa')
    plt.legend()
    plt.show()
"""

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


def main():
    # Definir o período de data desejado
    start_date = "2020-01-01"
    end_date = "2023-01-01"

    lista = ['ABCB4.SA', 'AGRO3.SA', 'BBAS3.SA', 'BBSE3.SA', 'CPLE6.SA', 'GOAU4.SA', 'ITSA4.SA', 'RANI3.SA',
             'SAPR11.SA', 'TAEE11.SA', 'VIVT3.SA']

    # Criar um DataFrame vazio
    df = pd.DataFrame()

    # Baixar os dados para cada ação e adicionar ao DataFrame
    for i in lista:
        cotacao = yf.download(i, start=start_date, end=end_date)
        df[i] = cotacao['Adj Close']

    # Plotar as séries de preços do DataFrame
    df.plot(figsize=(15, 10))

    plt.xlabel('Anos')
    plt.ylabel('Valor Ticket')
    plt.title('Variação de valor das ações')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
