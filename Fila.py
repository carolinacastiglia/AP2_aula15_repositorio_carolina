from Apartamento import Apartamento

class Fila:

    def __init__(self):
        self.inicio = None
        self.fim = None
    
    def adicionarAptoFilaEspera(self, apartamento):
        apto = apartamento

        if self.inicio == None:
            self.inicio = apto
        
        else:
            self.fim.proximo = apto
            
        self.fim = apto

    def removerAptoFilaEspera(self, vaga):
        if self.inicio == None:
            print("A fila de espera está vazia")
        
        elif self.inicio == self.fim:
            self.inicio.vaga = vaga
            self.inicio = None
            self.fim = None

        else:
            self.inicio.vaga = vaga
            self.inicio = self.inicio.proximo


    def imprimirFilaEspera(self):
        txt = ""
        if self.inicio == None:
            txt = "Fila de espera vazia"
        else:
            aux = self.inicio
            while(aux):
                txt += str(aux.numero)
                aux = aux.proximo
                if aux:
                    txt += "\n"
        
        print(txt)