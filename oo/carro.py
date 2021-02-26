class Direçõa:
    rotacão_a_direita_dct={
        NORTE:LESTE, LESTE:SUL, SUL:OESTE, OESTE:NORTE
    }
    rotacão_a_esquerda_dct={
        NORTE:OESTE, OESTE:SUL,SUL:LESTE, LESTE:NORTE}
    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacão_a_direita_dct[self.valor]

    def girar_a_esqurda(self):
        self.valor = self.rotacão_a_esquerda_dct[self.valor]

class motor:
    def __init__(self):
        self.velocidade = 0
    def acelerar(self):
        self.acelerar = += 1
    def frear(self):
        self.velocidade -= 2
        self.velocidade=max(0,self,velocidade)

















