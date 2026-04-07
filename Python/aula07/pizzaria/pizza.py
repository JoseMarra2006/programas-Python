class Pizza:
    def __init__(self, sabor, tamanho, massa):
        self.sabor = sabor
        self.tamanho = tamanho
        self.massa = massa

    def to_dict(self):
        return {
           'sabor': self.sabor,
           'tamanho': self.tamanho,
           'massa': self.massa
        }

    @staticmethod
    def from_dict(dados):
        return Pizza(
            dados['sabor'],
            dados['tamanho'],
            dados['massa']
        )