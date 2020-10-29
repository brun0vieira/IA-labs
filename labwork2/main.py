from distanceMatrix import *

def main():
    fName = "matrix"
    m = readDistanceMatrix(fName)
    #path = cria_solucao_inicial(m)
    path = ["Atroeira", "Douro", "Pinhal", "Teixoso", "Ulgueira", "Vilar"]
    melhor = simulatedAnnealing(path, fName)
    print('Melhor caminho: ', melhor)

if __name__ == '__main__':
     main()