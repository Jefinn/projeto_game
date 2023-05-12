import random
def bem_vindo():
    print("\n*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def jogar():
    bem_vindo()

    print('\ntemas disponível para jogo'.upper())
    print('(1)Frutas (2)Comida (3)Desenho'.upper())
    escolha = int(input('\nQual tema você deseja jogar: ').upper())

    if escolha == 1:
        tema_frutas()

    if escolha == 2:
        tema_comida()

    if escolha == 3:
        tema_desenho()
def tema_frutas():
    with open('temas_forca/frutas.txt', 'r') as arquivo:
        palavra = []

        for linha in arquivo:
            linha = linha.strip()
            palavra.append(linha)

    posicionamento = random.randrange(0, len(palavra))
    palavra_secreta = palavra[posicionamento].upper()

    letras_acertadas = ['_' for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not acertou and not enforcou):

        chute = input("\nQual letra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1

        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print('\nVocê acertou a palavra secreta')

        print('\nDeseja jogar de novo'.upper())
        loop = int(input(' (1) Sim  (2) Não '.upper().strip()))
        if loop == 1:
            jogar()
        else:
            print('Fim de Jogo'.upper())

    if enforcou:
        print('\nVocê errou a palavra secreta')
        print('A palavra secreta é {}'.format(palavra_secreta))

        print('\nDeseja jogar de novo'.upper())
        loop = int(input(' (1) Sim  (2) Não '.upper().strip()))
        if loop == 1:
            jogar()
        else:
            print('Fim de Jogo'.upper())

def tema_comida():
    with open('temas_forca/comida.txt', 'r') as arquivo:
        palavra = []
        for linha in arquivo:
            linha = linha.strip()
            palavra.append(linha)

    posicionamento = random.randrange(0, len(palavra))

    palavra_secreta = palavra[posicionamento].upper()

    letras_acertadas = ['_' for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not acertou and not enforcou):

        chute = input("\nQual letra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1

        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print('\nVocê acertou a palavra secreta')

        print('\nDeseja jogar de novo'.upper())
        loop = int(input(' (1) Sim  (2) Não '.upper().strip()))
        if loop == 1:
            jogar()
        else:
            print('Fim de Jogo'.upper())

    if enforcou:
        print('\nVocê errou a palavra secreta')
        print('A palavra secreta é {}'.format(palavra_secreta))

        print('\nDeseja jogar de novo'.upper())
        loop = int(input(' (1) Sim  (2) Não '.upper().strip()))
        if loop == 1:
            jogar()
        else:
            print('Fim de Jogo'.upper())

def tema_desenho():
    with open('temas_forca/desenho.txt', 'r') as arquivo:
        palavra = []
        for linha in arquivo:
            linha = linha.strip()
            palavra.append(linha)

    posicionamento = random.randrange(0, len(palavra))

    palavra_secreta = palavra[posicionamento].upper()

    letras_acertadas = ['_' for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not acertou and not enforcou):

        chute = input("\nQual letra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1

        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print('\nVocê acertou a palavra secreta')

        print('\nDeseja jogar de novo'.upper())
        loop = int(input(' (1) Sim  (2) Não '.upper().strip()))
        if loop == 1:
            jogar()
        else:
            print('Fim de Jogo'.upper())

    if enforcou:
        print('\nVocê errou a palavra secreta')
        print('A palavra secreta é {}'.format(palavra_secreta))

        print('\nDeseja jogar de novo'.upper())
        loop = int(input(' (1) Sim  (2) Não '.upper().strip()))
        if loop == 1:
            jogar()
        else:
            print('Fim de Jogo'.upper())

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if __name__ == '__main__':
    jogar()
