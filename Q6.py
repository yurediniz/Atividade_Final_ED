'''
6- Construa uma Lista Sequencial utilizando a linguagem Python com as seguintes operações:
a. Verificar se um número pertence lista;
b. Inserir um novo elemento na lista;
c. Remover um elemento da lista;
d. Imprimir os valores da lista;
'''

import numpy as np

class ListaSequencial:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultimaPosicao = -1
        self.valores = np.empty(self.capacidade, dtype = int)

    def imprimir(self):
        if self.ultimaPosicao == -1:
            print("A lista está vazia")
        else:
            for i in range(self.ultimaPosicao + 1):
                print(f"Pos{i} - {self.valores[i]}")
    
    def inserir(self, valor):
        self.ultimaPosicao += 1
        self.valores[self.ultimaPosicao] = valor
    
    def pesquisar(self, valor):
        for i in range(self.ultimaPosicao + 1):
            if valor == self.valores[i]:
                return i
        return -1
    
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultimaPosicao):
                self.valores[i] = self.valores[i + 1]
            self.ultimaPosicao -= 1

lista = ListaSequencial(5)
opc = 0
valor = 0
# Menu
while True:
    try:
        print(
            """
            MENU

            1 - Verificar se um número pertence lista
            2 - Inserir um novo elemento na lista
            3 - Remover um elemento da lista
            4 - Imprimir os valores da lista
            0 - Encerrar programa
            """
        )
        opc = int(input("Digite a opção desejada: "))
    except:
        print("Valor Invalido, digite novamente")
        continue
# Opção 1 - Verificar se um número pertence lista
    if opc == 1:
        print("\t\n1 - Verificar se um número pertence lista")
        while True:
            try:
                valor = int(input("\nDigite o valor que deseja pesquisar: "))
            except:
                print("\nValor Invalido, digite novamente")
                continue
            break
        if lista.pesquisar(valor) != -1:
            print(f"\nO número {valor} pertence a lista")
        else:
            print(f"\nO número {valor} não pertence a lista")
        continue
# Opção 2 - Inserir um novo elemento na lista
    elif opc == 2:
        print("\t\n2 - Inserir um novo elemento na lista")
        if lista.ultimaPosicao == lista.capacidade - 1:
            print("\nCapacidade maxima da lista atingida")
        else:
            while True:
                try:
                    valor = int(input("\nDigite o valor que deseja inserir: "))
                except:
                    print("\nValor Invalido, digite novamente")
                    continue
                break
            lista.inserir(valor)
            print(f"Número {valor}, inserido na lista com sucesso.")
        continue
# Opção 3 - Remover um elemento da lista
    elif opc == 3:
        print("\t\n3 - Remover um elemento da lista")
        if lista.ultimaPosicao == - 1:
            print("\nA Lista está Vazia")
        else:
            while True:
                try:
                    valor = int(input("\nDigite o valor que deseja remover: "))
                except:
                    print("\nValor Invalido, digite novamente")
                    continue
                break
            if lista.excluir(valor) == - 1:
                print(f"\nO número {valor} não pertence a lista")
            else:
                print(f"\nO número {valor}, foi removido com sucesso")
            continue
# Opção 4 - Imprimir os valores da lista
    elif opc == 4:
        print("\t\n4 - Imprimir os valores da lista")
        lista.imprimir()
# Opção 0 - Encerrar programa
    elif opc == 0:
        break
    else:
        print("\nOpção Invalida, digite novamente.")
        continue
        

        