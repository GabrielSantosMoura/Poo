class Pessoa():
    def __init__(self, nome, idade, peso):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.falando=False
        self.comendo=False
        self.dormindo=False
    def falar(self):
        print(f"{self.nome} começoua a falar")
    def comer(self, comida):
        if self.comendo == True
        print(f"{self.nome} comeu {comida}")
    def dormir(self):
        print(f"{self.nome} dormiu ")

