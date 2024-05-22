class Funcao:
    def seNaoVaiImplementarAgora(self):
        pass

    def parametroValorPadrao(self, nome=None, idade=25):
        if nome is not None:
            return ("Nome: {} Idade: {}".format(nome, idade))
        else:
            return (idade)

    def retornaMaisDeUmValor(self):
        return {'soma': 2+3, 'subtração': 6-4}

    def quandoNaoSabemosTotalArgumentos(self, *args): # O * que importa
        for a in args:
            print('outro argumento: {}'.format(a))

    def argumentosEsquemaDicionario(self, **kwargs):
        for key, value in kwargs.items():
            print('{0} = {1}'.format(key, value))
