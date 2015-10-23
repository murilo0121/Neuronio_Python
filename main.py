__author__ = 'muriloerhardt'
import random
import math


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
                if func == 'sign':
                    resultado = self.sign(self.somatorio(amostra[i]))  #gambi de teste arrumar dpois
                if func == 'sigmoid':
                    resultado = self.sigmoid(self.somatorio(amostra[i]))  #gambi de teste arrumar dpois
                if resultado != saidas[i]:
                    erroAux = saidas[i] - resultado
                    for j in range(len(amostra)):
                        self.dendritos.peso[j] = self.dendritos.peso[j] + taxa_aprendizado * erroAux * amostra[i][j]
                    err = True
            numeroDeEpocas += 1

            if numeroDeEpocas > epocas or not err:
                return 0

    def start(self,amostra,func):
        amostra.insert(0, -1)
        if func == 'sign':
            resultado = self.sign(self.somatorio(amostra))  #gambi de teste arrumar dpois
            if(resultado > 0):
                print ('1')
            if(resultado == 0):
                print('0')
            else:
                print('-1')
        if func == 'sigmoid':
            resultado = self.sigmoid(self.somatorio(amostra))  #gambi de teste arrumar dpois


    def sign(self, x):
        if x > 0:
            return 1
        elif x == 0:
            return 0
        else:
            return -1

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def somatorio(self, amostra):
        soma = 0
        for i in range(len(amostra)):
            soma += dendritos.peso[i]  # self.dendritos.peso[i] + amostra[i]
        return soma


def criaDendridos(quantidadeDentridos):
    dendritos = []
    j = quantidadeDentridos
    for i in range(quantidadeDentridos):
        dendritos.append(random.random())
    return dendritos


if __name__ == '__main__':
    print('Insira a quantidade de dentridos, o valor deve ter a mesma quantidade de valores de entrada:')
    quantidadeDeDendritos = int(input(''))
    dendritos = Dendrito(criaDendridos(quantidadeDeDendritos))
    neuronio = Neuronio(dendritos, 'sign')
    amostras = [[0.1, 0.4, 0.7], [0.3, 0.7, 0.2],
                [0.6, 0.9, 0.8], [0.5, 0.7, 0.1]]
    saidas = [1, -1, -1, 1]
    neuronio.treinamento(amostras, saidas, 1000, 0.1, -1, 'sign')
    amostras = [0.1, 0.4, 0.7]
    neuronio.start(amostras,'sign')
    amostras = [0.3, 0.7, 0.2]
    neuronio.start(amostras,'sign')
    amostras = [0.6, 0.9, 0.8]
    neuronio.start(amostras,'sign')
    amostras = [0.5, 0.7, 0.1]
    neuronio.start(amostras,'sign')
