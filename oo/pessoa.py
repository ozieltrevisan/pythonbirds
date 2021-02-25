class Pessoa:
    olhos = 2
    def __init__(self, *filhos,  nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list (filhos)


    def cumprimentar (self):
        return f'Olá {id (self)}'


if __name__ == '__main__':
    oziel = Pessoa(nome='oziel')
    luciano = Pessoa (oziel, nome='luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sbrenome = 'ramalho'
    del luciano.filhos
    luciano.olhos = 1
    oziel.olhos = 4
    del oziel.olhos
    print(luciano.__dict__)
    print(oziel.__dict__)
    print(luciano.olhos)
    print(oziel.olhos)
    print(id(pessoa .olhos), id(oziel.olhos), id(luciano .olhos))





