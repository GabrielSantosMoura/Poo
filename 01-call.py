from operator import truediv

from exercicio import Pessoa

aluno01 = Pessoa(nome="Gabriel", idade=21, peso=106)
print(aluno01.nome)
print(aluno01.idade)
print(aluno01.peso)

aluno01.falar()
aluno01.comer()
aluno01.dormir()


