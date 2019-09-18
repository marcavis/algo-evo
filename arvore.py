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

    def resultado(self):
        try:
            if self.temOper:
                if self.oper == '+':
                    return self.esq.resultado() + self.dir.resultado()
                elif self.oper == '-':
                    return self.esq.resultado() - self.dir.resultado()
                elif self.oper == '*':
                    return self.esq.resultado() * self.dir.resultado()
                elif self.oper == '/':
                    return self.esq.resultado() / self.dir.resultado()
                else: #potenciação
                    return self.esq.resultado() ** self.dir.resultado()
            else:
                return float(self.valor)
        except (ZeroDivisionError, TypeError):
            return None
        
    
    def __str__(self):
        #print (self.exibicaoLista())
        if self.temOper:
            return "("+ str(self.esq) + " " + str(self.oper) + " " + str(self.dir) + ")"
        else:
            return str(self.valor)
    
    def conteudo(self, obj):
        if obj.temOper:
            return obj.oper
        return obj.valor

    def exibicaoLista(self):
        tabela = {}
        tabela[1] = (self, self.conteudo(self))
        return tabela
        