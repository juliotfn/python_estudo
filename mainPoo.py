from Classes.poo import Animal
from Classes.poo import Dog
from Classes.poo import Cat
from Classes.poo import Peixe

testeAnimal = Animal()
testeDog = Dog("Spike", 10)
testeCat = Cat("Tica", 4)
testePeixe = Peixe("Moana", 1)

print(testeDog.make_animal_speak())
print(testeCat.make_animal_speak())
print(testePeixe.make_animal_speak())

print("-------------------")

"""
Exemplo usando herança, onde a nome, idade e o método descrição é acessada da classe pai pelos filhos
"""
print(testeDog.descricao())
print(testeCat.descricao())
print(testePeixe.descricao())
