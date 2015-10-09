class Dendrito():
    def __init__(self, peso):
        self.peso = peso

class Neuronio():
    def __init__(self, dendrito, func):
        self.dendrito = dendrito
        self.funcao = func

def criaDentritos():
    print('Digite o peso dos dendritos, separando por ;')
    print('Exemplo: 4.5;4;1.3;0.7;2;3')
    listaPesoDendritos = raw_input('')

    listaPesoDendritos = listaPesoDendritos.split(';')
    print(listaPesoDendritos)
    for list in listaPesoDendritos:
        try:
            float(list)
            print(list)
        except ValueError:
            print " \n \n \n !!!---ERRO. ALGUM VALOR INSERIDO NAO ESTA NO PADRAO CORRETO---!!!"
            criaDentritos()
    return listaPesoDendritos

def main():
        listaPesoDentritos = criaDentritos()
        print(listaPesoDentritos)
        for list in listaPesoDendritos:
            print('oioe')
    #    for dendrito in listaPesoDendritos:
    #        print 'oi'
    #        listaDentritos[i] = Dendrito(dendrito)
    #        i=i+1
    #        print(dendrito)

main()
