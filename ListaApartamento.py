from Apartamento import Apartamento

class ListaApartamento:
    def __init__(self):
        self.inicio = None
        self.fim = None
    
    def adicionarListaApto(self, valor):
        if self.inicio:
            aux = self.inicio

            while(aux.proximo):
                aux = aux.proximo
            aux.proximo = valor

            self.fim = aux.proximo
            no = aux.proximo

        else:
            self.inicio = valor
    
    def imprimirListaApto(self):
        if self.inicio == None:
            print("Lista de apartamentos está vazia!!")
        
        else:
            aux = self.inicio

            while(aux):
                prox = None

                if aux.proximo:
                    prox = aux.proximo

                if(prox == None):
                    print(aux.numero, "-", aux.torre.nome)

                else:
                   print(aux.numero, "-", aux.torre.nome, "-----Próximo:", prox.numero, "-", prox.torre.nome)
                aux = aux.proximo