from distanceMatrix import *

def main():
    fName = "matrix"
    m = readDistanceMatrix(fName)
    #simulatedAnnealing(m)
    #print(cria_solucao_inicial(m))
    #print(temperatura_inicial(m))
    #path = cria_solucao_inicial(m)
    path = ["Atroeira", "Douro", "Pinhal", "Teixoso", "Ulgueira", "Vilar"]
    melhor = simulatedAnnealing(path, fName)
    print(melhor)
if __name__ == '__main__':
     main()