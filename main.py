__author__ = 'muriloerhardt'
import random
import math
import copy

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
                    for j in range(len(self.dendritos.peso)):
                        self.dendritos.peso[j] = self.dendritos.peso[j] + taxa_aprendizado * erroAux * amostra[i][j]
                    err = True
            numeroDeEpocas += 1

            if numeroDeEpocas > epocas or not err:
                return 0

    def start(self,amostra,func):
        amostra.insert(0, -1)
        if func == 'sign':
            resultado = self.sign(self.somatorio(amostra))  #gambi de teste arrumar dpois
            if(resultado >= 0):
                print ('1')
            if(resultado < 0):
                print('-1')
            resultado = self.sigmoid(self.somatorio(amostra))  #gambi de teste arrumar dpois


    def sign(self, x):
        return 1 if x >= 0 else -1

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

    amostras2 = [[0.72, 0.82], [0.91, -0.69],
                 [0.46, 0.80], [0.03, 0.93],
                 [0.12, 0.25], [0.96, 0.47],
                 [0.8, -0.75], [0.46, 0.98],
                 [0.66, 0.24], [0.72, -0.15],
                 [0.35, 0.01], [-0.16, 0.84],
                 [-0.04, 0.68], [-0.11, 0.1],
                 [0.31, -0.96], [0.0, -0.26],
                 [-0.43, -0.65], [0.57, -0.97],
                 [-0.47, -0.03], [-0.72, -0.64],
                 [-0.57, 0.15], [-0.25, -0.43],
                 [0.47, -0.88], [-0.12, -0.9],
                 [-0.58, 0.62], [-0.48, 0.05],
                 [-0.79, -0.92], [-0.42, -0.09],
                 [-0.76, 0.65], [-0.77, -0.76]]

    saidas2 = [-1, -1, -1, -1, -1, -1, -1, -1,
               -1, -1, -1, -1, -1, 1, 1, 1, 1,
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    testes2 = copy.deepcopy(amostras2)

    print('Insira a quantidade de dentridos, o valor deve ter a mesma quantidade de valores de entrada:')
    quantidadeDeDendritos = int(input(''))
    dendritos = Dendrito(criaDendridos(quantidadeDeDendritos))

    neuronio2 = Neuronio(dendritos, 'sign')
    neuronio2.treinamento(amostras2, saidas2, 1000, 0.1, -1, "sign")
    for teste in testes2:
        neuronio2.start(teste,'sign')


