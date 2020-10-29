from distanceMatrix import *

def main():
    fName = "matrix"
    m = readDistanceMatrix(fName)
    #path = cria_solucao_inicial(m)
    path = ['A','C','E','G','H','I','J','M','O','P','Q','U','W','X','Y','Z']
    melhor = simulatedAnnealing([path,m[1]], fName)
    print('Melhor caminho: ', melhor)
    print(getInitials(melhor))

if __name__ == '__main__':
     main()