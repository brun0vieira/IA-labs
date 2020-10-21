from distanceMatrix import *

if __name__ == '__main__':
    fName = "teste"
    m = readDistanceMatrix(fName)
    print(getAllCities(m))
