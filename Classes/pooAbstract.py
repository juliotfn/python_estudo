from abc import ABC, abstractmethod

"""
Usar classes abstratas e métodos abstratos com o módulo abc ajuda a garantir 
que certas funcionalidades sejam implementadas em todas as subclasses, proporcionando 
uma maneira estruturada de definir contratos para as classes derivadas.

Se fizesse apenas import abc teria que usar abc.Classe:
import abc
class Animal(abc.ABC):
    @abc.abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        print("Woof!")
class Cat(Animal):
    def make_sound(self):
        print("Meow!")
"""
class Animal(ABC): #Se torna abstrata ao herdar de ABC
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # @abstractmethod é necessário para indicar que não será implementado na classe abstrata
    # e que é obrigatóro a sua implementação
    @abstractmethod
    def speak(self):
        pass

    def descricao(self): # É um método concreto e não abstrato
        return f'{self.nome} é um animal de {self.idade} anos.'
class Dog(Animal): #Exemplo de polimorfismo
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Peixe(Animal):
    pass