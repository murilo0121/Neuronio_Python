__author__ = 'muriloerhardt'
import random
import math
import copy


def sign(x):
    return 1 if x >= 0 else -1


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def setp(x):
    a = 2.5  # ESSE É O VALOR DO SETP, CASO DESEJE ALTERAR
    return 1 if x < a else 0


class Axonio():
    def __init__(self, valor):
        self.valor = valor


class Dendrito():
    def __init__(self, peso):
        self.peso = peso


class Neuronio():
    def __init__(self, dendritos, func):
        self.dendritos = dendritos
        self.funcao = func

    def treinamento(self, amostra, saidas, epocas, taxa_aprendizado, limiar):
        for matriz in amostra:
            matriz.insert(0, -1)

        self.dendritos.peso.insert(0, limiar)  # LIMIAR AQUI É USADO PARA BALANCEAR É DIFERENTE DO LIMIAR DA FUNC STEP
        numeroDeEpocas = 0

        while True:
            print(numeroDeEpocas)
            err = False

            for i in range(len(amostra)):
                resultado = self.funcao(self.somatorio(amostra[i]))
                if resultado != saidas[i]:
                    erroAux = saidas[i] - resultado
                    for j in range(len(self.dendritos.peso)):
                        self.dendritos.peso[j] = self.dendritos.peso[j] + taxa_aprendizado * erroAux * amostra[i][j]
                    err = True
            numeroDeEpocas += 1

            if numeroDeEpocas > epocas:
                return 0

    def mostra(self):
        print(self.dendritos.peso)

    def start(self, amostra):
        amostra.insert(0, -1)
        resultado = self.funcao(self.somatorio(amostra))
        if (resultado >= 0):
            print('1')
            return 1
        if (resultado < 0):
            print('-1')
            return -1

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
    amostras = [[0,0,0,0,1], [0,0,1,0,1],[0,1,1,1,0],[1,1,0,0,0],[0,1,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,1,1,0,0],
                [1,0,1,0,0],[1,1,1,0,1],[1,0,1,1,0],[1,1,0,1,0],[0,1,0,1,1],[1,1,0,0,0],[0,1,1,0,0],[1,1,0,1,0]]

    # ESSA SAIDA CORRESPONDE A SAIDA DE CADA UM DOS CONJUTNOS DE NEURONIO DA AMOSTRAS
    # EX: [0.72, 0.82] SAIDA -1, [0.91, -0.69] SAIDA -1
    saidas = [0,0,1,0,0,0,0,0,0,1,1,1,1,0,0,1]

    quantidadeDeDendritos = len(amostras[0])
    dendritos = Dendrito(criaDendridos(quantidadeDeDendritos))  # CRIA OS DENDRITOS, COM VALORES RAND ENTRE -1 E 1
    neuronio = Neuronio(dendritos, sign)  # ENVIAR A LISTA DE DENDRITOS E A FUNCAO QUE SE DESEJA PASSAR
    neuronio.mostra()
    neuronio.treinamento(amostras, saidas, 1000, 0.3, -1)  # TREINA
    neuronio.mostra()
    amostras = [1,1,1,0,1]
    a = neuronio.start(amostras)  # INICIA A AMOSTRA PARA VERIFICAR O RESULTADO ATRAVEZ DOS PESOS DE DENDRITOS TREINADOS ATERIORMENTE
    axonio1 = Axonio(a)
