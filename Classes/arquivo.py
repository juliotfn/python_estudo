class Arquivo:
    def escrever(self):
        # arquivo = open('palavras.txt', 'w')
        arquivo = open('palavras.txt', 'a') # "a" de append, uma palavra por linha
        arquivo.write('banana\n')
        arquivo.write('melancia\n')

        #Trabalhar no modo binário
        # imagem = open('foto.jpg', 'rb')

        arquivo.close()

    def ler(self):
        arquivo = open('palavras.txt', 'r')

        #Para ler o arquivo de uma vez use arquivo.read()

        for linha in arquivo:
            # strip() Remove todos os espaços em branco (espaços, tabulações,
            # quebras de linha, etc.) do início e do fim da string
            linha = linha.strip()
            print(linha)

        # Voltando ao início do arquivo
        arquivo.seek(0)

        # Passando para uma lista
        palavras = []
        for linha in arquivo:
            palavras.append(linha)
        for p in palavras:
            print(p)

        arquivo.close()

    def lerComWith(self):
        with open('palavras.txt') as arquivo:
            for linha in arquivo:
                linha = linha.strip() # Remove \n do fim das palavras
                print(linha)

        # with fechará o arquivo mesmo se ocorrer
        # alguma falha na leitura
        # arquivo.close() não é necessário