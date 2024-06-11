from Classes.pooAbstract import Animal
from Classes.pooAbstract import Dog
from Classes.pooAbstract import Cat
from Classes.pooAbstract import Peixe

testeDog = Dog("Spike", 10)
testeCat = Cat("Tica", 4)
# testePeixe = Peixe("Moana", 1) Não pode ser instanciada porque não implementa o método abstrato speak

print(testeDog.speak())
print(testeCat.speak())
"""
Exemplo usando herança, onde a nome, idade e o método descrição é acessada da classe pai pelos filhos
"""
print(testeDog.descricao())
print(testeCat.descricao())

