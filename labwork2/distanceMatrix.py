import random
import numpy as np
import math

# reads a distance matrix (composed of a list of cities and the matrix itself)
# given file name fName
def readDistanceMatrix(fName):
    cities = []
    distances = []
    with open(fName, 'r') as f:
        i=0
        for line in f:
            if i == 0:
                l = [line.rstrip().split()]
                city = l[0][1]
                cities.append(city)
            else:
                row = []
                l = [line.rstrip().split()]
                city = l[0][0]
                cities.append(city)
                j = 1
                while j<= i:
                    row.append(l[0][j])
                    j += 1
                distances.append(row)
            i += 1
    f.close()   
    dm = []
    dm.append(cities)
    dm.append(distances)
    return dm

# creates a distance matrix given another, m, and a list containing a subset
# of the cities occurring in m
def createSmallMatrix(m,clist):
    cities = clist
    distances = []
    for c in range(1,len(cities)):
        row = []
        for v in range(0,c):
            row.append(distance(m,cities[c],cities[v]))      
        distances.append(row)  
    dm = []
    dm.append(cities)
    dm.append(distances)
    return dm

# creates a distance matrix given another, m, and a String, filter, containing 
# the initals of a subset of the cities occurring in m
def createFilterMatrix(m,filter):
    return createSmallMatrix(m,getCities(m,filter))
    
# returns the distance between two cities c1 and c2, given distance matrix m
def distance (m,c1,c2):
    index1 = m[0].index(c1)
    index2 = m[0].index(c2)
    if index1<index2:
        return int(m[1][index2-1][index1])
    else:
        return int(m[1][index1-1][index2])
        
# shows the distance matrix m
def showDistances(m):
    cities = '         '
    for i in range(0,len(m[0])-1):
        cities = cities + ' ' + "{:>9}".format(m[0][i])
    print(cities)
    for i in range(0,len(m[1])):
        row = "{:>9}".format(m[0][i+1])
        for j in range(0,len(m[1][i])):
            row = row + ' ' + "{:>9}".format(m[1][i][j])
        print(row)

# from a distance matrix m returns a list of all the cites of m
def getAllCities(m):
    return m[0]

# from a distance matrix m and a String filter returns a subset of cites of m
# with initials in filter 
def getCities(m,filter):	
    cityList = []
    for initial in filter:
        cityList.append(getCity(m[0],initial))
    return cityList
    
# from a list of cities cityList return the one with the first letter initial
def getCity(cityList,initial):	
    for city in cityList:
        if city[0] == initial:
            return city
    return None

# from a list of cities cityList return a String with their initials
def getInitials(cityList):
    initials = ""
    for city in cityList:
        initials += city[0]
    return initials

# funcao que cria uma solucao inicial de forma aleatória
def cria_solucao_inicial(matrix):
    cities = getAllCities(matrix)
    path = []
    while len(cities) != 0:
        index = random.randint(0,len(cities)-1)
        path.append(cities[index])
        cities.pop(index)

    return path

# funcao que determina a temperatura inicial a partir do problema
def temperatura_inicial(matrix):
    max_distance = 0
    min_distance = 500 # caso contrário, ficaria a zero
    prob = 0.9
    array = np.array(matrix[1])

    for x in array:
        for y in x:
            distance = int(y)
            if max_distance < distance:
                max_distance = distance
            if min_distance > distance:
                min_distance = distance

    delta_max = 2*max_distance - 2*min_distance
    t_inicial = -delta_max/(math.log(prob))

    return t_inicial

# funcao de variacao do numero de iteracoes a cada temperatura
def var_n_iter(n_iter):
    beta = 1.1
    n_iter *= beta
    return n_iter

# funcao que retorna true no caso de se ter atingido o criterio de paragem
def criterio_de_paragem(temperatura_inicial, temperatura_actual):
    if  (temperatura_actual/temperatura_inicial) < 0.1 :
        return True
    return False

# funcao de decaimento da temperatura
def decaimento(temperatura):
    alpha = 0.8 # quanto mais alto mais lento é o arrefecimento
    temperatura *= alpha
    return temperatura

# funcao que retorna um vizinho a partir de uma solucao
def vizinho(solucao):
    vizinho = []

    firstIndex = random.randint(0, len(solucao)-1)
    secondIndex = random.randint(0, len(solucao)-1)
    diff = abs(secondIndex-firstIndex)
    # we can't have consecutive or equal indexes
    while diff==1 or diff==0: # diff=1 and diff=0 means, respectively, consecutive and equal indexes
        secondIndex = random.randint(0,len(solucao)-1)
        diff = abs(secondIndex-firstIndex)

    vizinho.append(solucao[firstIndex])
    vizinho.append(solucao[secondIndex])

    # swap positions
    solucao[firstIndex], solucao[secondIndex] = vizinho[1], vizinho[0]
    nova_solucao = inverte_ligacoes(solucao,firstIndex,secondIndex)

    return nova_solucao

# Ao retirarmos as ligacoes (i,i+1) e (j,j+1) a unica forma admissivel de criar um outro circuito é ligando (i,j) e (i+1,j+1) e invertendo a direcao das ligacoes entre i+1 e j (vizinho)
# Esta funcao serve para inverter as tais ligacoes
def inverte_ligacoes(solucao, firstIndex, secondIndex):

    i = firstIndex
    j = secondIndex

    if firstIndex - secondIndex > 0:
        i, j = secondIndex, firstIndex
    solucao[i+1:j] = solucao[j-1:i:-1]
    return solucao

def pathDistances(clist, fname):
    cost = 0
    matrix = readDistanceMatrix(fname)
    for i in range(0, len(clist)-1):
        if i == len(clist)-1 :
            cost += distance(matrix, clist[i] , clist[0])
        cost += distance(matrix, clist[i], clist[i+1])  
    return cost

def randomProb(t,d):
    bool_list = [0, 1]
    distribution = [1-math.exp(-d/t), math.exp(-d/t)]
    random_number = random.choices(bool_list, distribution)
    return random_number

def simulatedAnnealing(matrix, fName):
    # n_iter é um valor arbitrário -> 10 000
    m = readDistanceMatrix(fName)
    corrente = cria_solucao_inicial(m)
    melhor = corrente
    t_inicial = temperatura_inicial(m)
    t = t_inicial
    n_iter = 10000
    print(t_inicial)
    while 1:
        for i in range (1, int(n_iter)):
            proximo = vizinho(corrente)
            d = pathDistances(proximo, fName) - pathDistances(melhor, fName)
            if d < 0:
                corrente = proximo
                if pathDistances(corrente, fName) < pathDistances(melhor, fName):
                    melhor = corrente
            else:
                if randomProb(t, d):
                    corrente = proximo
        if criterio_de_paragem(t_inicial, t):
            return melhor
        n_iter = var_n_iter(n_iter)  
        t = decaimento(t)  
        print('Temperatura inicial :',t)