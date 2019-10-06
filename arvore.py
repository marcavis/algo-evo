import random, sys

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

    def avaliacao(self, gabarito):
        aval = 0.0
        erros = 0
        for (x, fx) in gabarito:
            if self.resultado(x) == None:
                erros += 1
            else:
                aval += abs(fx - self.resultado(x))    
        
        if erros > 2:
            return None
        return(aval * (2 ** (erros + 1)))

    def resultado(self, x):
        try:
            if self.temOper:
                if self.oper == '+':
                    return self.esq.resultado(x) + self.dir.resultado(x)
                elif self.oper == '-':
                    return self.esq.resultado(x) - self.dir.resultado(x)
                elif self.oper == '*':
                    return self.esq.resultado(x) * self.dir.resultado(x)
                elif self.oper == '/':
                    return self.esq.resultado(x) / self.dir.resultado(x)
                else: #potenciação
                    #evitar números complexos
                    if self.esq.resultado(x) < 0 and int(self.dir.resultado(x)) != self.dir.resultado(x):
                        return None
                    #evitar alguns tipos de overflow
                    if self.dir.resultado(x) > 10000:
                        return None
                    return self.esq.resultado(x) ** self.dir.resultado(x)
            else:
                if self.valor == 'x':
                    return float(x)
                return float(self.valor)
        except (ZeroDivisionError, TypeError, OverflowError) as ex:
            #print("erro:", self.esq.resultado(x), self.oper, self.dir.resultado(x))
            # if isinstance(ex, OverflowError):
            #     sys.exit()
            return None
        
    def __str__(self):
        #print (self.exibicaoLista())
        if self.temOper:
            return "("+ str(self.esq) + " " + str(self.oper) + " " + str(self.dir) + ")"
        else:
            return str(self.valor)
    
    # def conteudo(self, obj):
    #     if obj.temOper:
    #         return obj.oper
    #     return obj.valor

    # def exibicaoLista(self):
    #     tabela = {}
    #     tabela[1] = (self, self.conteudo(self))
    #     return tabela
        