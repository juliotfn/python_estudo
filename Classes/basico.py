import random
class Basico:
    def __init__(self, num):
        self.num = num

    def escreveParImpar(self):
        resposta = ""
        for i in range(1, self.num):
            if i % 2 == 0:
                resposta += str(i) + ') Número par \n'
            elif i == 3:
                resposta += "Exceção) Número {} \n".format(i)
            else:
                resposta += str(i) + ') Número impar \n'
        return resposta

    def forRangeStep(self):
        for i in range(1, 10, 2):
            print(i)

    def forItemTupla(self):
        numeros = (1, 2, 3, 4)
        for n in numeros:
            print(n)

    def forChaveValor(self):
        mapa = {'a': 1, 'b': "dois", 'c': 3.14}
        for chave, valor in mapa.items():
            print(chave, valor, type(valor))

    def potenciacao(self):
        x = 2
        y = 3
        print(x**y) #Potenciação-Print 8

    def divisaoInteira(self):
        print(7//2) #Divisão inteira - Print 3

    def multiplicacaoTexto(self):
        texto = "python"
        textoM = texto.upper() # texto.lower()
        textoC = texto.capitalize()
        print(textoM * 2, " - ", textoC)

    def printDuasCasasDecimais(self):
        #:.2f - Print com duas casas decimais (245.23)
        x = 245.2346
        print('{:.2f}'.format(x))

    def usoBool(self):
        print(bool(3 > 8))
        print(bool(""))
        print(bool(None)) #Semelhante ao Null, mas ocupa espaço de memória
        print(bool(2 == '2'))
        print(bool(0))
        print(bool(3 > 1))

    def usoIs(self):
        # is verifica que é o mesmo objeto
        # == se o valor é igual
        a = 1
        b = 2
        c = 1
        print(a is b)
        print(a is c)

    def usoInt(self):
        a = "245"
        print(5 + int(a))

    def embaralhaLista(self):
        # Embaralha lista
        lista = [1, 2, 3, 4, 5]
        lista.append(8)
        lista.pop(2) # 0, 1, 2, portanto excluirá o 3
        print(lista)
        random.shuffle(lista)
        print(lista)
        print("Valor mínimo {} e Máximo {}.".format(min(lista), max(lista)))
        print("Primeiro da lista: {}.".format(lista[0]))
        print("Tamanho da lista: {}.".format(len(lista)))

    def escolheItemAleatorio(self):
        # Escolhe um item aleatório
        lista = [1, 2, 3, 4, 5]
        item_aleatorio = random.choice(lista)
        print(item_aleatorio)

    def geraNumero(self, a, b, op):
        if op == 1:
            # Inclui o a e b na geração
            numero_aleatorio = random.randint(a, b)
        elif op == 2:
            # 0.0 <= N < 1.0
            numero_aleatorio = random.random()
        return numero_aleatorio

    def usoWhile(self):
        x = 0
        while(x <= 10):
            print("{}) Aleatório: {}".format(x, self.geraNumero(1, self.num, 1)))
            if(x == 8): #Sai do while
                break;
            x += 1 #Não existe ++ ou --
        acertou = False
        acertou1 = False
        x = 0
        while(not acertou or not acertou1): # and
            x += 1
            if x > 5:
                acertou = True
                print("{}) Acertou é True".format(x))
            if x > 10:
                print("{}) Acertou1 é True".format(x))
                acertou1 = True

    def testaInput(self):
        nome = input("digite seu nome:\n")
        idade = input("digite sua idade:\n")
        print("Nome: {} e Idade: {}".format(nome, idade))

    def achaLetraEmPalavraScreta(self, chute):
        palavra_secreta = "banana"
        #in e not in pode ser usado em listas. Ex: chute in [a, b, c]
        if(chute in palavra_secreta):
            posicao = 0
            for letra in palavra_secreta:
                posicao += 1
                if(chute.lower() == letra.lower()):
                    print("Achou letra na posição {}.".format(posicao))
        elif(chute not in palavra_secreta):
            print("Não achou letra")
