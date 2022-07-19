'''
4- Construa uma Fila de Prioridade utilizando a linguagem Python em que sejam
implementadas as funções para inserção de um novo elemento (inteiro) na fila e a
remoção do elemento de mais alta prioridade
'''

import numpy as np

class FilaPrioridade:
  
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def __fila_vazia(self):
        return self.numero_elementos == 0

    def __fila_cheia(self):
        return self.numero_elementos == self.capacidade 
  
    def enfileirar(self, valor):
        if self.__fila_cheia():
            print('A fila está cheia')
            return
    
        if self.numero_elementos == 0:
            self.valores[self.numero_elementos] = valor
            self.numero_elementos += 1
        else:
            x = self.numero_elementos - 1
            while x >= 0:
                if valor > self.valores[x]:
                    self.valores[x + 1] = self.valores[x]
                else:
                    break
                x -= 1
            self.valores[x + 1] = valor
            self.numero_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print('A fila está vazia')
            return
        valor = self.valores[self.numero_elementos - 1]
        self.numero_elementos -= 1
        return valor     
  
    def primeiro(self):
        if self.__fila_vazia():
            return -1
        return self.valores[self.numero_elementos - 1]

print("\n\tPrioridades das Fichas:\n\t1 - Prioridade Alta (101 á 199)\n\t2 - Prioridade Moderada (201 á 299)\n\t3 - Prioridade Baixa (301 á 399)")

fichas = []
p1 = 100
p2 = 200
p3 = 300
while True:
    try:
        ficha = int(input("\nInforme a Prioridade para receber sua ficha ou '0' para finalizar: "))
        if ficha == 1:
            if p1 == 200:
                print("Todas as fichas, 1 - Prioridade Alta foram distribuídas, volte outro dia.")
                continue
            p1 += 1
            fichas.append(p1)
            print(f"Sua ficha é a número: {p1}")
        elif ficha == 2:
            if p2 == 300:
                print("Todas as fichas, 2 - Prioridade Moderada foram distribuídas, volte outro dia.")
                continue
            p2 += 1
            fichas.append(p2)
            print(f"Sua ficha é a número: {p2}")
        elif ficha == 3:
            if p3 == 400:
                print("Todas as fichas, 3 - Prioridade Baixa foram distribuídas, volte outro dia.")
                continue
            p3 += 1
            fichas.append(p3)
            print(f"Sua ficha é a número: {p3}")
        elif ficha == 0:
            break
        else:
            print("\nValor invalido, digite novamente.")
    except:
        print("\nValor invalido, digite novamente.")
        continue

if len(fichas) > 0:
    fila = FilaPrioridade(len(fichas))
    for i in range (len(fichas)):
        fila.enfileirar(fichas[i])

    print(f"\nOrdem de chamada das fichas\n")

    for j in range (len(fila.valores)):
        print(f"\tFicha Nº: {fila.desenfileirar()}")
else:
    print("Nenhuma ficha foi emitida")
