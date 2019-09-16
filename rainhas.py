#!/usr/bin/python3
import sys, random

#altere para criar tabuleiros com mais rainhas!
tabuleiro = 8

def cromossomo():
    #como python poupa tempo...
    x = random.sample(range(tabuleiro), tabuleiro)
    return [y + 1 for y in x]

tamanhoGerInicial = 50
eraMelhorAval = 0
melhorAvaliacao = ()

def main():
    cromossomos = []
    for x in range(tamanhoGerInicial):
        cromossomos.append(cromossomo())
    era = 0
    solucao = False
    while not solucao:
        era += 1
        cromossomos = elitismo(cromossomos)
        cromossomos = cromossomos + novaGeracao(cromossomos)
        realizarMutacoes(cromossomos)
        avalM  = avaliar(cromossomos[0])
        print ("Era número " + str(era) + ", melhor solução tem " + str(avalM) + " conflitos.")
        if avaliar(cromossomos[0]) == 0:
            solucao = True
            print ("Solução encontrada na era número " + str(era) + "!")
            print ( cromossomos[0])
            mostrarSolucao(cromossomos[0])
        #crossover(None, None)
    #mostrarMelhorSolucao(melhorAvaliacao)

def avaliar(crom):
    resultado = 0
    for i in range(tabuleiro):
        for j in range(i + 1, tabuleiro):
            if abs(i - j) == abs(crom[i] - crom[j]):
                resultado += 1
    return resultado

def mostrarSolucao(crom):
    print("~" * (tabuleiro * 3 ))
    for i in crom:
        print("| " + " | " * (i - 1) + "Q" + "| " + " | " * (tabuleiro - i ))
        print("~" * (tabuleiro * 3 ))

def crossover(c1, c2):
    pontoDeCorte = random.choice(range(1, tabuleiro - 1))
    filho1 = []
    filho2 = []
    for x in list(range(tabuleiro)):
        #quando chegarmos no ponto de corte, trocar os filhos de lugar
        #para que recebam genes de um pai diferente
        if x < pontoDeCorte:
            filho1.append(c1[x])
            filho2.append(c2[x])
        else:
            #após o ponto de corte, adiciona todos os itens do outro
            #pai, na mesma ordem, se não já existirem no filho
            filho1 = filho1 + [y for y in c2 if y not in filho1]
            filho2 = filho2 + [y for y in c1 if y not in filho2]
    return [filho1, filho2]

def elitismo(solucoes):
    #manter 56% da geração anterior, para que 80% dos sobreviventes
    #completem uma geração do mesmo tamanho, pois
    # 0.56 + (0.56 * 0.8) ~= 1
    qtManter = int(0.56 * tamanhoGerInicial)
    solucoes.sort(key = avaliar, reverse=False)
    return solucoes[:qtManter]

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

def realizarMutacoes(solucoes):
    for x in list(range(len(solucoes))):
        #escolher 3% dos cromossomos para alterar
        if random.random() < 0.03:
            #trocar dois genes de lugar
            i, j = random.sample(range(tabuleiro),2)
            solucoes[x][i], solucoes[x][j] = solucoes[x][j], solucoes[x][i]

if __name__ == "__main__":
    main()
