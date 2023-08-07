# O que o Professor Daniel nomeia como ordem no projeto dele eu chamo aqui de ordem_compra

class OrdemCompra:

    def __init__(self):
        self.atributos = None
        self.id_cliente = None

    def cadastar_ordem(self, cliente):
        self.id_cliente = cliente
