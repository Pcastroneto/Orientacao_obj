class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def escreve(self):
        print(self.nome, self.idade)
        
class Estudante(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(self, nome, idade)
        self.graduacao =2024
            
#Use a palavra-chave pass quando não quiser
#Adcionar nenhum aoutra propriedade ou método à classe.

x = Estudante("Jo", 21)
x.escreve()
print(x.graduacao)