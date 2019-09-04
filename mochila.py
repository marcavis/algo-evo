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
#atalhos para trabalhar com maior clareza
volume = [x[1] for x in artigos]
peso = [x[2] for x in artigos]
valor = [x[3] for x in artigos]
tamanhoGerInicial = 200
volumeMax = 125
pesoMax = 125
tamanhoCromossomo = len(artigos) #25 nesse caso
eraMelhorAval = 0
melhorAvaliacao = ()

def main():
    cromossomos = []
    melhorAvaliacao = (0, None, 0)
    for x in range(tamanhoGerInicial):
        q = cromossomo.Cromossomo(tamanhoCromossomo)
        cromossomos.append(q)
        #print(q.genes)
    for era in range(50):
        cromossomos = elitismo(cromossomos)
        cromossomos = cromossomos + novaGeracao(cromossomos)
        realizarMutacoes(cromossomos)
        if(melhorAvaliacao[2] < avaliar(cromossomos[0])):
            melhorAvaliacao = (era, cromossomos[0].genes[:], avaliar(cromossomos[0]))
        print(melhorAvaliacao[0], melhorAvaliacao[1], melhorAvaliacao[2])
        #crossover(None, None)
    mostrarMelhorSolucao(melhorAvaliacao)

def avaliar(crom):
    somaVolume = (sum([crom.genes[i] * volume[i] for i in list(range(tamanhoCromossomo))]))
    somaPeso = (sum([crom.genes[i] * peso[i] for i in list(range(tamanhoCromossomo))]))
    somaValor = (sum([crom.genes[i] * valor[i] for i in list(range(tamanhoCromossomo))]))
    resultado = 0 if somaVolume <= volumeMax else volumeMax - somaVolume
    resultado += 0 if somaPeso <= pesoMax else pesoMax - somaPeso
    return somaValor + somaValor**2 / (somaPeso + somaVolume) + resultado

def mostrarMelhorSolucao(melhorAvaliacao):
    genes = melhorAvaliacao[1]
    era = melhorAvaliacao[0]
    #criar um novo cromossomo com os genes melhor avaliados;
    #não usamos o cromossomo melhor avaliado diretamente, pois ele pode
    #ter sofrido mutação
    crom = cromossomo.Cromossomo(tamanhoCromossomo)
    crom.genes = genes
    somaVolume = (sum([genes[i] * volume[i] for i in list(range(tamanhoCromossomo))]))
    somaPeso = (sum([genes[i] * peso[i] for i in list(range(tamanhoCromossomo))]))
    somaValor = (sum([genes[i] * valor[i] for i in list(range(tamanhoCromossomo))]))
    print("Melhor solução encontrada na era  " + str(era) + ", com avaliação " + str(avaliar(crom)))
    print("Essa solução tem volume = " + str(somaVolume) + ", peso = " + str(somaPeso) + " e valor = " + str(somaValor))
    print("Vetor de artigos escolhidos:\n" + str(genes))
    if somaVolume > 125 or somaPeso > 125:
        print("A solução encontrada é inválida - execute o programa novamente!")

def crossover(c1, c2):
    qtPontosDeCorte = 1 + (tamanhoCromossomo // 20) #2, neste caso
    pontosDeCorte = random.sample(set(range(1, tamanhoCromossomo - 1)), qtPontosDeCorte)
    pontosDeCorte.sort()
    filho1 = cromossomo.Cromossomo(tamanhoCromossomo)
    filho2 = cromossomo.Cromossomo(tamanhoCromossomo)
    for x in list(range(tamanhoCromossomo)):
        #quando chegarmos no ponto de corte, trocar os filhos de lugar
        #para que recebam genes de um pai diferente
        if len(pontosDeCorte) > 0 and x == pontosDeCorte[0]:
            pontosDeCorte.pop()
            filho1, filho2 = filho2, filho1
        filho1.genes[x] = c1.genes[x]
        filho2.genes[x] = c2.genes[x]
    return [filho1, filho2]

def elitismo(solucoes):
    #manter 56% da geração anterior, para que 80% dos sobreviventes
    #completem uma geração do mesmo tamanho, pois
    # 0.56 + (0.56 * 0.8) ~= 1
    qtManter = int(0.56 * tamanhoGerInicial)
    solucoes.sort(key = avaliar, reverse=True)
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
            for y in list(range(tamanhoCromossomo)):
                #alterar, em média, um gene
                if random.random() < (1.0 / tamanhoCromossomo):
                    solucoes[x].genes[y] = 1 - solucoes[x].genes[y]

if __name__ == "__main__":
    main()