'''
3- Construa um programa em Python de acordo com situação problema descrita: Um grupo
de soldados está cercado e não há esperança de vitória, porém existe somente um cavalo
disponível para escapar e buscar por reforços. Para determinar qual soldado deve escapar
para encontrar ajuda, eles formam um círculo (Fila Circular) e sorteiam um número de um
chapéu. Começando por um soldado sorteado aleatoriamente, uma contagem é realizada
até o número sorteado. Quando a contagem terminar, o soldado em que a contagem
parou é removido do círculo, um novo número é sorteado e a contagem recomeça no
soldado seguinte ao que foi eliminado. A cada rodada, portanto, o círculo diminui em um,
até que somente um soldado reste e seja escolhido para a tarefa.
'''

import numpy as np
from random import randint

class FilaCircular:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.nElementos = 0
        self.valores = np.empty(self.capacidade, dtype = int)
    
    def __filaVazia(self):
        return self.nElementos == 0
    
    def __filaCheia(self):
        return self.nElementos == self.capacidade
    
    def enfileirar(self, valor):
        if self.__filaCheia():
            print("A Fila está Cheia")
            return
        self.final += 1
        if self.final == self.capacidade:
            self.final = 0
        self.valores[self.final] = valor
        self.nElementos += 1

    def desenfileirar(self):
        if self.__filaVazia():
            print("A Fila está Vazia")
            return
        temp = self.valores[self.inicio]
        self.inicio += 1
        if self.inicio == self.capacidade:
            self.inicio = 0
        self.nElementos -= 1
        return temp
    
    def primeiro(self):
        if self.__filaVazia():
            return -1
        return self.valores[self.inicio]

    def escolha_soldado(self):
        # Seleciona por qual Soldado o sorteiro irá começar
        for j in range (randint(1, 100)):
            self.inicio += 1
            if self.inicio == self.capacidade:
                self.inicio = 0

            self.final += 1
            if self.final == self.capacidade:
                self.final = 0
        print(f'\nSoldado selecionado para iniciar o sorteio: {self.primeiro()}')
        
        # Desenfileira o Soldado selecionado até sobrar o escolhido
        for i in range(self.nElementos - 1):
            # Seleciona o Soldado que vai ser Desenfileirado
            for j in range (randint(1, 100)):
                self.inicio += 1
                if self.inicio == self.capacidade:
                    self.inicio = 0

                self.final += 1
                if self.final == self.capacidade:
                    self.final = 0

            self.desenfileirar()

        print(f'\nSoldado escolhido para escapar: {self.primeiro()}\n')

while True:
    print("\n\tSORTEIO DO SOLDADO")
    try:
        qtd_soldados = int(input("\nInforme a quantidade de soldados que vão participar do sorteio: ")) 
    except:
        print("\nValor Invalido, digite novamente")
        continue
    break
soldados = FilaCircular(qtd_soldados)
for i in range(qtd_soldados):
    while True:
        try:
            num_soldados = int(input("\nInforme o número do soldado para o sorteio: "))
        except:
            print("\nValor Invalido, digite novamente")
            continue
        break
    soldados.enfileirar(num_soldados)

soldados.escolha_soldado()
