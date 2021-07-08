from Apartamento import Apartamento
from Torre import Torre
from ListaApartamento import ListaApartamento
from Fila import Fila

class main:

    t1 = Torre()
    t1.cadastrar(1, "A", "Acesso 123")

    t2 = Torre()
    t2.cadastrar(2, "B", "Acesso 456")

    t3 = Torre()
    t3.cadastrar(3, "C", "Acesso 789")

    print("------ TORRE ------")
    t1.imprimir()
    t2.imprimir()
    t3.imprimir()
    
    ap1 = Apartamento()
    ap1.cadastrar(1, 304, t1)

    ap2 = Apartamento()
    ap2.cadastrar(2, 305, t1)

    ap3 = Apartamento()
    ap3.cadastrar(3, 108, t2)

    ap4 = Apartamento()
    ap4.cadastrar(4, 107, t2)

    ap5 = Apartamento()
    ap5.cadastrar(5, 206, t3)

    print("\n----- APTO -----")
    ap1.imprimir()
    ap2.imprimir()
    ap3.imprimir()
    ap4.imprimir()
    ap5.imprimir()

    #listaApto = ListaApartamento()
    #print("\n----- LISTA DE APTO -----")
    #listaApto.imprimirListaApto()
    #listaApto.adicionarListaApto(ap1)
    #listaApto.adicionarListaApto(ap2)
    #listaApto.adicionarListaApto(ap3)
    #listaApto.adicionarListaApto(ap4)
    #listaApto.adicionarListaApto(ap5)
    #listaApto.imprimirListaApto()

    fila = Fila()
    print("\n----- FILA DE VAGA DE ESTACIONAMENTO -----")
    fila.removerAptoFilaEspera("E76")

    print("\n----- APTO ADD NA FILA DE ESPERA -----")
    fila.adicionarAptoFilaEspera(ap1)
    fila.adicionarAptoFilaEspera(ap2)
    fila.adicionarAptoFilaEspera(ap3)
    fila.adicionarAptoFilaEspera(ap4)
    fila.adicionarAptoFilaEspera(ap5)

    fila.imprimirFilaEspera()

    print("\n----- ATUAL ESTADO DOS APTOS -----")
    ap1.imprimir()
    ap2.imprimir()
    ap3.imprimir()
    ap4.imprimir()
    ap5.imprimir()

    print("\n----- REMOVER APTO FILA DE ESPERA -----")
    fila.removerAptoFilaEspera("A12")
    fila.removerAptoFilaEspera("F56")

    fila.imprimirFilaEspera()

    print("\n----- ATUAL ESTADO DOS APTOS -----")
    ap1.imprimir()
    ap2.imprimir()
    ap3.imprimir()
    ap4.imprimir()
    ap5.imprimir()


    
