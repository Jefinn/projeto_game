# JOGO DA FORCA#
def jogar():
    print('\n*******************************')
    print('Seja Bem-Vindo ao Jogo da Forca')
    print('*******************************')

    palavra_secreta = 'banana'
    ltr_certas = ['-' '-' '-' '-' '-' '-']

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):

        chute = input('\nInforme uma letra: ')
        chute = chute.upper()
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            letra = letra.upper()

            if (chute == letra):
                ltr_certas[index] = letra
            index = index + 1

            print(ltr_certas)

        else:
            print('A letra informada não existe')
            print('Tente novamente')

    print('Jogando....')


if (__name__ == "__main__"):
    jogar()
