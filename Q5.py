'''
5- Escreva um programa em Python que simule o controle de uma pista de decolagem de
aviões em um aeroporto. Neste programa, o usuário deve ser capaz de realizar as
seguintes tarefas:
a. Listar o número de aviões aguardando na fila de decolagem;
b. Autorizar a decolagem do primeiro avião da fila;
c. Adicionar um avião à fila de espera;
d. Listar todos os aviões na fila de espera;
e. Listar as características do primeiro avião da fila.
'''
import numpy as np

class ListaSequencial:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultimaPosicao = -1
        self.valores = np.empty(self.capacidade, dtype = object)

    def imprimir(self):
        if self.ultimaPosicao == -1:
            print("A Lista está vazia")
        else:
            for i in range(self.ultimaPosicao + 1):
                print(i + 1, " - ", self.valores[i])
    
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
    
class Aviao:
    
    def __init__ (self, cod_id, empresa, fabricante, capacidade):
        self.cod_id = cod_id
        self.empresa = empresa
        self.fabricante = fabricante
        self.capacidade = capacidade
    
    def __repr__(self):
        return str(self.cod_id)

    def __str__ (self):
        return str(f"ID: {self.cod_id} - Empresa: {self.empresa} - Fabricante: {self.fabricante} - Capacidade: {self.capacidade}")
        
lista_decolagem = ListaSequencial(2)
lista_espera = ListaSequencial(10)
opc = 0
# Menu
while True:
    try:
        print(
            """
            MENU

            1 - Listar o número de aviões aguardando na fila de decolagem
            2 - Autorizar a decolagem do primeiro avião da fila
            3 - Adicionar um avião à fila de espera
            4 - Listar todos os aviões na fila de espera
            5 - Listar as características do primeiro avião da fila
            0 - Encerrar o programa
            """
        )
        opc = int(input("Digite a opção desejada: "))
    except:
        print("\nValor Invalido, digite novamente.")
        continue
# Opção 1 - Listar o número de aviões aguardando na fila de decolagem
    if opc == 1:
        print("\nAviões na Lista de Decolagem:\n")
        lista_decolagem.imprimir()
        continue
# Opção 2 - Autorizar a decolagem do primeiro avião da fila
    elif opc == 2:
        if lista_decolagem.ultimaPosicao == - 1:
            print("\nA Lista de Decolagem está vazia")
        else:
            print(f"\nAvião ID: {repr(lista_decolagem.valores[0])} foi autorizado a fazer a decolagem")
            lista_decolagem.excluir(lista_decolagem.valores[0])
            if not lista_espera.ultimaPosicao == - 1:
                lista_decolagem.inserir(lista_espera.valores[0])
                lista_espera.excluir(lista_espera.valores[0])
        continue
# Opção 3 - Adicionar um avião à fila de espera
    elif opc == 3:
        if lista_espera.ultimaPosicao == lista_espera.capacidade - 1:
            print("\nA Lista de Espera está cheia, aguarde a decolagem de algum avião para adicionar mais a lista")

        else:
            while True:
                try:
                    print("\nINFORME OS DADOS DA AERONAVE:\n")
                    cod_id = str(input("Informe o código de identificação do avião: "))
                    empresa = str(input("Informe a empresa responsável pelo voo: "))
                    fabricante = str(input("Informe a fabricante da aeronave: "))
                    capacidade = int(input("Informe a capacidade de passageiros: "))
                    aviao = Aviao(cod_id, empresa, fabricante, capacidade)
                    break
                except:
                    print("\nValor invalido, digite novamente\n")
            
            if not lista_decolagem.ultimaPosicao == lista_decolagem.capacidade - 1:
                print(f"\nAvião ID: {repr(aviao)} foi adicionado direto na lista de decolagem")
                lista_decolagem.inserir(aviao)
                
            else:   
                print(f"\nAvião ID: {repr(aviao)} foi adicionada na lista de espera")
                lista_espera.inserir(aviao)
        continue
# Opção 4 - Listar todos os aviões na fila de espera
    elif opc == 4:
        print("\nAviões na Lista de Espera:\n")
        lista_espera.imprimir()
        continue
# Opção 5 - Listar as características do primeiro avião da fila
    elif opc == 5:
        if lista_decolagem.ultimaPosicao == - 1:
            print("\nAs Listas de Decolagem e Espera estão vazias")
        elif lista_espera.ultimaPosicao == - 1:
            print("Primeiro Avião na Lista de Decolagem:")
            print('1 - ',lista_decolagem.valores[0])
            print("\nA Lista de Espera está vazia")
        else:
            print("\nPrimeiro Avião na Lista de Decolagem:")
            print('1 - ',lista_decolagem.valores[0])
            print("\nPrimeiro Avião na Lista de Espera:")
            print('1 - ',lista_espera.valores[0])
        continue
# Opção 0 - Encerrar programa
    elif opc == 0:
        break
    else:
        print("\nOpção Invalida, digite novamente.")
        continue
