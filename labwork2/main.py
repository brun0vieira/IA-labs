from distanceMatrix import *

def main():
    fName = "matrix"
    m = readDistanceMatrix(fName)
    vizinho(cria_solucao_inicial(m))

if __name__ == '__main__':
    main()