class Programa:
        def __init__(self, nome, ano):
            self._nome = nome.title()
            self.ano = ano
            self._likes = 0

        @property
        def likes(self):
            return self._likes

        def curtida(self):
            self._likes += 1

        @property
        def nome(self):
            return self._nome

        @nome.setter
        def nome(self, novo_nome):
            self._nome = novo_nome.title()

        def imprime(self):
            print("Nome: {} - Ano: {} - Curtidas {}".format(self._nome,self.ano,self.likes))

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano)
        self.duracao = duracao

class Documentario(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas


class Serie(Programa):
    def __init__(self,nome ,ano ,temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas


twd = Serie("the walking dead", 2010,11,)

twd.curtida()
twd.curtida()
twd.curtida()
twd.curtida()

print("Nome: {} - Ano: {} - Temporadas: {} - Curtidas {}".format(twd.nome,twd.ano, twd.temporadas,twd.likes))

topgun2 = Filme("top gun: maverick", 2022, 137, )
topgun2.curtida()
topgun2.curtida()
topgun2.curtida()


print("Nome: {} - Ano: {} - Duração: {} Min - Curtidas {}".format(topgun2.nome,topgun2.ano, topgun2.duracao,topgun2.likes))


doc = Documentario("One Strange Rock", 2018, 2)

doc.curtida()

print("Nome: {} - Ano: {} - Temporadas: {} - Curtidas {}".format(doc.nome,doc.ano, doc.temporadas,doc.likes))

print("--------------------------------")

filmes_series = [topgun2,twd,doc]

for programa in filmes_series:
    programa.imprime()