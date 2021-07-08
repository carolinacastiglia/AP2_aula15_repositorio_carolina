from Torre import Torre

class Apartamento:

    def __init__(self):
        self.id = None
        self.numero = None
        self.torre = None
        self.vaga = int()
        self.proximo = None

    
    def cadastrar(self, id, numero, torre):
        self.id = id
        self.numero = numero
        self.torre = torre

    def imprimir(self):
        if self.vaga:
            if self.proximo:
                print("ID APTO:", self.id, " - APTO", self.numero, " - está na torre", 
                    self.torre.nome, " - vaga", self.vaga, 
                    " - próximo apto é o ", self.proximo.numero, "-", self.proximo.torre.nome)
            else:
                print("ID APTO:", self.id, " - APTO", self.numero, " - está na torre", 
                    self.torre.nome, " - vaga", self.vaga)
        else:
            if self.proximo:
                print("ID APTO:", self.id, " - APTO", self.numero, " - está na torre", self.torre.nome,
                        " - próximo apto é o ", self.proximo.numero, "-", self.proximo.torre.nome)
            else:
                print("ID APTO:", self.id, " - APTO", self.numero, " - está na torre", self.torre.nome)
