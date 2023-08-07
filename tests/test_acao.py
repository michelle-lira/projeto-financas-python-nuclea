import unittest
from models.acao import Acao


class TestAcao(unittest.TestCase):
    def test_cadastro_acao(self):
        # Teste para cadastrar uma ação e verificar se o ID foi atribuído corretamente
        acao = Acao(acao="PETR4", nome="Petrobras", data_compra="2023-01-01", valor_compra=28.50)

        # O ID deve ser None antes de salvar a ação no banco de dados
        self.assertIsNone(acao.id)

        # Salvar a ação no banco de dados
        # Implemente a lógica para salvar a ação no banco usando o SQLAlchemy
        # Exemplo: db.add(acao), db.commit(), etc.

        # Após salvar, o ID deve ser diferente de None
        self.assertIsNotNone(acao.id)

    # Adicione outros testes para as funções da Acao, se houver...
