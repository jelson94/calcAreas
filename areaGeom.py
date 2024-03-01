#testandoooooo 
from math import pi

def areaRet(ladoA, ladoB):

    area = ladoA * ladoB

    return area

def areaCir(diâmetro):

    area = pi * (diâmetro ** 2) / 4
    return area

def areaTrian(base, altura):

    area = base * altura / 2

    return area

def areaTrap(baseMaior, baseMenor, altura):

    area = ((baseMaior + baseMenor) * altura / 2)


    return area

print("Ola!")
