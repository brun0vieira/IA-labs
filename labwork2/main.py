from distanceMatrix import *

if __name__ == '__main__':
    fName = "matrix"
    m = readDistanceMatrix(fName)
    #simulatedAnnealing(m)
    #print(cria_solucao_inicial(m))
    #print(temperatura_inicial(m))
    path = cria_solucao_inicial(m)
    print(path)
    viz = vizinho(path)
    print(viz)