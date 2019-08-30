import random

class Cromossomo:
    def __init__(self, tamanho):
        self.genes = [random.randrange(0, 2) for x in range(tamanho)] 