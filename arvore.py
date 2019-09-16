import random

class Arvore:
    def __init__(self, temOper, oper, valor, esq, dir):
        self.temOper = temOper
        self.oper = oper
        self.valor = valor
        self.esq = esq
        self.dir = dir 
    
    def novoOperador(self, oper):
        return Arvore(True, oper, 0, None, None)
    
    def novaFolha(self, valor):
        return Arvore(False, None, valor, None, None)
        