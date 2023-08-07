from repository.banco_de_dados import BancoDeDados

class OrdemCompraAcao:
    def __init__(self, ordem_compra_id, acao_id):
        self.ordem_compra_id = ordem_compra_id
        self.acao_id = acao_id

# Exemplo de uso
if __name__ == "__main__":
    ordem_compra_acao = OrdemCompraAcao(ordem_compra_id=1, acao_id=2)
    print(f"Ordem de Compra ID: {ordem_compra_acao.ordem_compra_id}, Ação ID: {ordem_compra_acao.acao_id}")
