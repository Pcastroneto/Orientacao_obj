class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def escreveNome(abc):
        print("Olá o meu nome é:" + abc.nome)
nome1 = Pessoa("Emengarda",44)
nome1.escreveNome()

#Modificar o objeto
nome1.idade = 23
print(nome1.idade)