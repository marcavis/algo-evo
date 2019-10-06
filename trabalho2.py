#!/usr/bin/python3
import sys, random 
import arvore

paramT = list(range(-5, (5 + 1))) + ['x']
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
tamanhoGerInicial = 2000

def novaFuncao(nivel):
    #chance de gerar mais um nível na árvore cai pela metade a cada nível
    if random.random() < 1 / nivel:
        novaArvore = arvore.Arvore.novoOperador(None, random.choice(paramF))
        novaArvore.esq = novaFuncao(nivel + 1)
        novaArvore.dir = novaFuncao(nivel + 1)
    else:
        novaArvore = arvore.Arvore.novaFolha(None, random.choice(paramT))
    return novaArvore

def main():
    floresta = []
    for i in range(tamanhoGerInicial):
        floresta.append(novaFuncao(1))
    for era in range(5):
        floresta = elitismo(floresta)
        print(len(floresta))
        #cromossomos = cromossomos + novaGeracao(cromossomos)
        #realizarMutacoes(cromossomos)
        pass
    # for a in floresta:
        #print(a)
        # if(a.avaliacao(dados) != None and a.avaliacao(dados) < 20):
            # print(a.avaliacao(dados), a)
        # for (x, fx) in dados:
        #     print(a.resultado(x), fx)
        #print()

def elitismo(solucoes):
    #manter 56% da geração anterior, para que 80% dos sobreviventes
    #completem uma geração do mesmo tamanho, pois
    # 0.56 + (0.56 * 0.8) ~= 1
    qtManter = int(0.56 * tamanhoGerInicial)
    solucoes = [x for x in solucoes if x.avaliacao(dados) != None]
    print(len(solucoes))
    solucoes.sort(key = avaliacao)
    print(solucoes[0], avaliacao(solucoes[0]))
    return solucoes[:qtManter]

def avaliacao(arvore):
    return arvore.avaliacao(dados)

if __name__ == "__main__":
    main()