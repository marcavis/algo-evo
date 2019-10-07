#!/usr/bin/python3
import sys, random 
import arvore

paramT = list(range(-5, (5 + 1))) + ['x']
paramF = ['+', '-', "*", "/"] 
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
tamanhoGerInicial = 20

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
        print(floresta[-1].altura(), floresta[-1])
    for era in range(5):
        floresta = elitismo(floresta)
        print(len(floresta))
        print(floresta[0], floresta[0].avaliacao(dados))
        floresta = floresta + novaGeracao(floresta)
        #realizarMutacoes(cromossomos)
        pass
    for a in floresta:
        print(a)
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
    solucoes.sort(key = avaliacao)
    return solucoes[:qtManter]

def crossover(c1, c2):
    print()
    print(c1)
    print(c2)
    cursor1 = c1.pontoDeCrossover()
    cursor2 = c2.pontoDeCrossover()
    opcao = random.choice([1,2,3,4])
    if opcao == 1:
        cursor1.dir, cursor2.esq = cursor2.esq, cursor1.dir
    elif opcao == 2:
        cursor1.dir, cursor2.dir = cursor2.dir, cursor1.dir
    elif opcao == 3:
        cursor1.esq, cursor2.esq = cursor2.esq, cursor1.esq
    else:
        cursor1.esq, cursor2.dir = cursor2.dir, cursor1.esq
    print(c1)
    print(c2)
    return [c1, c2]

#passa por todos os sobreviventes da seleção, incluindo-os para reprodução
#numa lista, com 80% de chance para cada um.
#Após isso, embaralhar os candidatos para que os pares não sejam elitistas,
#e excluir o último cromossomo se a quantidade for ímpar.
#Depois, cruza os elementos, de dois em dois
def novaGeracao(solucoes):
    pais = []
    filhos = []
    for x in list(range(len(solucoes))):
        if random.random() < 0.8:
            pais.append(solucoes[x])
    random.shuffle(pais)
    if len(pais) % 2 == 1:
        pais.pop()
    while len(pais) > 0:
        pai1 = pais.pop()
        pai2 = pais.pop()
        filhos += crossover(pai1, pai2)
    return filhos

def avaliacao(arvore):
    return arvore.avaliacao(dados)

if __name__ == "__main__":
    main()