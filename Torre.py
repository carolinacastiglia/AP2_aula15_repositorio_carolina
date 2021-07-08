class Torre:

    def __init__(self):
        self.id = int()
        self.nome = str()
        self.endereco = str()
    
    def cadastrar(self, id, nome, endereco):
        self.id = id
        self.nome = nome
        self.endereco = endereco

    def imprimir(self):
        print("ID TORRE:", self.id, " - TORRE", self.nome, " -", self.endereco)
