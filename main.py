#!/usr/bin/python3
import sys, random
import cromossomo

artigos = [
    ("A",6,2,5),
    ("B",2,9,7),
    ("C",1,9,8),
    ("D",8,7,9),
    ("E",2,2,2),
    ("F",3,2,6),
    ("G",5,3,2),
    ("H",9,4,1),
    ("I",8,4,8),
    ("J",8,7,1),
    ("K",6,7,8),
    ("L",2,3,10),
    ("M",7,7,9),
    ("N",9,7,6),
    ("O",7,3,2),
    ("P",10,4,8),
    ("Q",2,10,6),
    ("R",9,2,5),
    ("S",1,5,2),
    ("T",9,8,7),
    ("U",3,10,8),
    ("V",9,2,7),
    ("W",9,8,9),
    ("X",2,6,5),
    ("Y",4,7,6)
]

tamanhoCromossomo = len(artigos) #25 nesse caso

def main():
    print(random.choice(artigos))
    q = cromossomo.Cromossomo(25)
    print(q.genes)

if __name__ == "__main__":
    main()