class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    lucinano = Pessoa(renzo, nome='Lucionano')
    print(Pessoa.cumprimentar(lucinano))
    print(id(lucinano))
    print(lucinano.cumprimentar())
    print(lucinano.nome)
    print(lucinano.idade)
    for filho in lucinano.filhos:
        print(filho.nome)
    lucinano.sobrenome = 'Ramalho'
    del lucinano.filhos
    print(lucinano.__dict__)
    print(renzo.__dict__)