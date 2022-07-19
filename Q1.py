'''
1- Construa uma Pilha utilizando a linguagem Python. Dada uma sequência contendo N (N > 0) números inteiros, imprimi-la na ordem inversa.
'''
import numpy as np

class Pilha:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1
        self.__valores = np.empty(self.__capacidade, dtype = int)

    def __pilhaVazia(self):
        if self.__topo == -1:
            return True
        else:
            return False
    
    def __pilhaCheia(self):
        if self.__topo == self.__capacidade - 1:
            return True
        else:
            return False

    def empilhar(self, valor):
        if self.__pilhaCheia():
            print("A pilha está cheia")
        else:
            self.__topo += 1
            self.__valores[self.__topo] = valor

    
    def desempilhar(self):
        if self.__pilhaVazia():
            print("A pilha está vazia")
        else:
            self.__topo -= 1
    
    def verTopo(self):
        if self.__topo != -1:
            return self.__valores[self.__topo]
        else:
            return -1
            
    # Imprime a Pilha na ordem inversa que os valores foram inseridos
    def pilhaInvertida(self):
        if self.__pilhaVazia():
            print("A pilha está vazia")
        else:
            for i in range(self.__topo + 1):
                print (self.__valores[i])

pilha = Pilha(5)
pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(3)
pilha.empilhar(4)
pilha.empilhar(5)

pilha.pilhaInvertida()


        
        

