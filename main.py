__author__ = 'muriloerhardt'
import random
import math
import copy


def sign(x):
    return 1 if x >= 0 else -1


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def setp(x):
    a = 5  # ESSE É O VALOR DO SETP, CASO DESEJE ALTERAR
    return 1 if x < a else 0


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

        self.dendritos.peso.insert(0, limiar) #LIMIAR AQUI É USADO PARA BALANCEAR É DIFERENTE DO LIMIAR DA FUNC STEP
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

    def start(self, amostra):
        amostra.insert(0, -1)
        resultado = self.funcao(self.somatorio(amostra))
        if (resultado >= 0):
            print('1')
        if (resultado < 0):
            print('-1')

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
    amostras = [[0.72, 0.82], [0.91, -0.69],
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
    
    #ESSA SAIDA CORRESPONDE A SAIDA DE CADA UM DOS CONJUTNOS DE NEURONIO DA AMOSTRAS
    #EX: [0.72, 0.82] SAIDA -1, [0.91, -0.69] SAIDA -1
    saidas = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ]
    
    quantidadeDeDendritos = len(amostras[0])    
    dendritos = Dendrito(criaDendridos(quantidadeDeDendritos)) #CRIA OS DENDRITOS, COM VALORES RAND ENTRE -1 E 1 
    neuronio = Neuronio(dendritos, sign) #ENVIAR A LISTA DE DENDRITOS E A FUNCAO QUE SE DESEJA PASSAR

    neuronio.treinamento(amostras, saidas, 1000, 0.1, -1, sign) #TREINA
    amostras = [0.72, 0.82]
    neuronio.start(amostras)    #INICIA A AMOSTRA PARA VERIFICAR O RESULTADO ATRAVEZ DOS PESOS DE DENDRITOS TREINADOS ATERIORMENTE

    amostras = [-0.12, -0.9]
    neuronio.start(amostras)
