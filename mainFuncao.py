from Classes.funcao import Funcao

testeFuncao = Funcao()

testeFuncao.seNaoVaiImplementarAgora()
print(testeFuncao.parametroValorPadrao(idade=34)) #especifiquei o parâmetro

resultado = testeFuncao.retornaMaisDeUmValor()
print(resultado["soma"])
for key in resultado:
    print('{}: {}'.format(key, resultado[key]))

testeFuncao.quandoNaoSabemosTotalArgumentos("Maria", 21, "Campinas", "São Paulo")
lista = ["é", "muito", "legal"]
testeFuncao.quandoNaoSabemosTotalArgumentos('python', *lista)

testeFuncao.argumentosEsquemaDicionario(nome = "Maia")
dicionario = {'nome': 'joao', 'idade': 25}
testeFuncao.argumentosEsquemaDicionario(**dicionario)