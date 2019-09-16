#!/usr/bin/python3
import sys, random 
import arvore

paramT = list(range(-5, (5 + 1)))
paramF = ['+', '-', "*", "/", "^"]
#convertidos em frações para não perderem precisão
dados = [   (1, 2.0/3),
            (2, 6.0/3),
            (3, 12.0/3),
            (4, 20.0/3),
            (5, 30.0/3),
            (6, 42.0/3),
            (7, 56.0/3),
            (8, 72.0/3),
            (9, 90.0/3),
            (10, 110.0/3) ]
floresta = []
tamGeracao = 50

def main():
    for i in range(tamGeracao):
        floresta.append(arvore.Arvore.novaFolha(None, random.choice(paramT)))
    for a in floresta:
        print(a, a.valor)

if __name__ == "__main__":
    main()