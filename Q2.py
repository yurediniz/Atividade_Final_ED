'''
2- Desenvolva um programa em Python utilizando uma Pilha de acordo com a situação
problema: Armazene as placas dos carros de luxos (apenas os números) que estão
estacionados em um rua sem saída. Dado uma placa verifique se o carro está estacionado
na rua. Caso esteja, informe a sequência de carros que deverá ser retirada para que o
carro em questão consiga sair.
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
    
    def pesquisar_placa(self):
        while True:
            try:
                placa = int(input("\nInforme a placa do carro que deseja retirar: "))
            except:
                print("\nValor Invalido, digite novamente")
                continue
            break
        qtd_carros = 0
        for i in range (self.__topo, -1, -1):
            if (placa == self.__valores[i]) and qtd_carros == 0:
                print(f"\nO carro de placa {self.__valores[i]}, é o primeiro da saída")
                break
            elif placa == self.__valores[i]:
                print(f"\nPara retirar o carro de placa: {self.__valores[i]}, será necessário retirar {qtd_carros} carro(s) antes:")
                ordem = 0
                for j in range (self.__topo, i, -1):
                    ordem +=1
                    print(f"{ordem}o. O carro de placa: {self.__valores[j]}")
                break
            elif i == 0:
                print("\nEste carro não está estacionado aqui")
            qtd_carros += 1

while True:
    print("\n\tEstacionamento Rua Sem Saída")
    try:
        capacidade = int(input("\nInforme a quantidade de carros estacionados na rua sem saída: "))
    except:
        print("\nValor Invalido, digite novamente")
        continue
    break
estacionamento = Pilha(capacidade)

for i in range(capacidade):
    while True:
        try:
            placa = (int(input(f"\nAgora informe a placa do {i+1}/{capacidade} carro(s) que estão estacionados na rua sem saída: ")))
        except:
            print("\nValor Invalido, digite novamente")
            continue
        break
    estacionamento.empilhar(placa)

print("\nA Rua já está lotada de carros")
estacionamento.pesquisar_placa()
print("")
