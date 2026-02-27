class Trabalhador:
    
    def __init__(self, cargo, id, senha, nome):
        self.cargo = cargo
        self.id = id
        self.senha = senha
        self.nome = nome
class Produto:

    def __init__(self, preco, quantidade, nome, id):
        self.preco = preco
        self.quantidade = quantidade
        self.nome = nome
        self.id = id

    def __str__(self):
        text =f'Nome: {self.nome} | Preco: {self.preco} | Quantidade: {self.quantidade}'
        return text