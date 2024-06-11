class Animal:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
    def speak(self):
        pass

    def make_animal_speak(self):
        # if(hasattr(objeto, 'atributo'): verifica se o objeto tem o atributo o método

        if(self.speak() != None): #Verifica se a classe implementa speak
            return self.speak()
        else:
            return 'instância de {} não implementa o método speak()'.format(self.__class__.__name__)

    def descricao(self):
        return f'{self.nome} é um animal de {self.idade} anos.'

class Dog(Animal): #Exemplo de polimorfismo
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Peixe(Animal):
    pass