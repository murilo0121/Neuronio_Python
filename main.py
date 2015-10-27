__author__ = 'muriloerhardt'
import random
import math
import copy

def sign(x):
    return 1 if x >= 0 else -1


class Dendrito():
    def __init__(self, peso):
        self.peso = peso

class Neuronio():
    def __init__(self, dendritos, func):
        self.dendritos = dendritos
        self.funcao = func

    def treinamento(self, amostra, saidas, epocas, taxa_aprendizado, limiar, func):
        for matriz in amostra:
            matriz.insert(0, -1)

        self.dendritos.peso.insert(0, limiar)
        numeroDeEpocas = 0

        while True:
            print(numeroDeEpocas)
            err = False

            for i in range(len(amostra)):
                resultado = func(self.somatorio(amostra[i]))
                if resultado != saidas[i]:
                    erroAux = saidas[i] - resultado
                    for j in range(len(self.dendritos.peso)):
                        self.dendritos.peso[j] = self.dendritos.peso[j] + taxa_aprendizado * erroAux * amostra[i][j]
                    err = True
            numeroDeEpocas += 1

            if numeroDeEpocas > epocas:
                return 0

    def start(self,amostra):
        amostra.insert(0, -1)
        resultado = self.funcao(self.somatorio(amostra))
        if(resultado >= 0):
            print ('1')
        if(resultado < 0):
            print('-1')

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def somatorio(self, amostra):
        soma = 0
        for i in range(len(amostra)):
            soma += dendritos.peso[i] * amostra[i]  # self.dendritos.peso[i] + amostra[i]
        return soma


def criaDendridos(quantidadeDentridos):
    dendritos = []
    j = quantidadeDentridos
    for i in range(quantidadeDentridos):
        dendritos.append(0.5)
    return dendritos


if __name__ == '__main__':
    print('Insira a quantidade de dentridos, o valor deve ter a mesma quantidade de valores de entrada:')
    #colocar para ler a quantidade de dentritos automaticamente,
    quantidadeDeDendritos = int(input(''))
    dendritos = Dendrito(criaDendridos(quantidadeDeDendritos))
    neuronio = Neuronio(dendritos, sign)
    amostras = [[0.1, 0.4, 0.7], [0.3, 0.7, 0.2],
                [0.6, 0.9, 0.8], [0.5, 0.7, 0.1]]
    saidas = [1, -1, -1, 1]
    neuronio.treinamento(amostras, saidas, 1000, 0.1, -1, sign)
    amostras = [0.1, 0.4, 0.7]
    neuronio.start(amostras)
    amostras = [0.3, 0.7, 0.2]
    neuronio.start(amostras)
    amostras = [0.6, 0.9, 0.8]
    neuronio.start(amostras)
    amostras = [0.5, 0.7, 0.1]
    neuronio.start(amostras)

    amostras2 = [[1,4000,45,1], [1,5000,40,1], [2,3500,40,0],[2,300,39,1],[1,200,18,0],[1,400,50,1],[2,5000,40,1],[2,200,25,0]]

    saidas2 = [1,1,1,0,0,1,1,0]

    testes2 = copy.deepcopy(amostras2)

    print('Insira a quantidade de dentridos, o valor deve ter a mesma quantidade de valores de entrada:')
    quantidadeDeDendritos = int(input(''))
    dendritos = Dendrito(criaDendridos(quantidadeDeDendritos))

    neuronio2 = Neuronio(dendritos, sign)
    neuronio2.treinamento(amostras2, saidas2, 1000, 0.1, -1, sign)
    teste = [1, 300, 80, 1]
    neuronio2.start(teste)


