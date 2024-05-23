"""
>> Existem três tipos básicos de
sequência: list (lista) , tuple (tupla) e range (objeto de intervalo). Outro tipo de sequência
famoso que já vimos são as strings que são sequências de texto.

>> Sequências podem ser mutáveis ou imutáveis. Sequências imutáveis não podem ter seus valores
modificados. Tuplas, strings e ranges são sequências imutáveis, enquanto listas são sequências
mutáveis.

Funções não vistas:
s.count(x) -> Número total de ocorrências de x em s
"""
class Sequencia:
    def pegaUltimoPenultimo(self):
        lista = [1, 2, 3, 4]
        # valor negativo percorre lista de forma reversa
        print("Último: {} e Penúltimo: {}.".format(lista[-1], lista[-2]))

    def letrasPalavra(self, palavra):
        lista = list(palavra) # lista = [b, a, n, a, n, a]
        for l in lista:
            print(l)

    def pegaSegundoTerceiroPorFatiamento(self):
        lista = [1, 2, 3, 4]
        # valor negativo percorre lista de forma reversa
        print(lista[1:3]) # Retorna da posição 1 a 3 -> [2, 3]
        print(lista[2:]) # Retorna da posição 2 em diante -> [3, 4]

    def addValorLista(self):
        lista = [1, 2, 3, 4] # Converter para Tupla, tupla(lista)
        lista.append(5)
        lista.extend([6, 7]) # Add vários itens de uma vez
        lista += [8, 9, 10]

        print(lista)
        print(lista * 2) # Repete a lista

    def criarTupla(self): #Imutável
        dias = ('domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado')
        print(type(dias)) # <class 'tuple'>

    def criarOperarConjuntos(self):
        # Não aceita valores repetidos e Ñ é ordenado
        # frutas = set(), cria conjunto vazio
        frutas = {'laranja', 'banana', 'uva', 'pera', 'laranja'}
        print(frutas) # Escreve apenas {'banana', 'uva', 'pera', 'laranja'}

        a = {'a', 'e', 'c', 't', 'b'}
        b = {'a', 'x', 'i', 'c', 'b'}
        print(a-b)
        print(a | b) #união
        print(a & b) #interseção
        print(a ^ b) #diferença simétrica -> (a-b) U (b-a)

    def criarOperarDicionario(self):
        pessoa = {'nome': 'João', 'idade': 25, 'cidade': 'São Paulo'}
        pessoa['pais'] = "Brasil" #Adicionar item

        # Outra forma de criar um dicionário
        a = dict(um=1, dois=2, três=3)

        print(pessoa)
        print(pessoa.keys())
        print(pessoa.values())
        print(a)

    def retornaAlgoParaCadaPosicaoDeUmaListaOuString(self):
        palavra_secreta = 'banana'
        return ['_' for letra in palavra_secreta] # Retorna ['_', '_', '_', '_', '_', '_']


