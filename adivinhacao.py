#JOGO DE ADIVINHÇÃO DE NUMEROS#
import random

def jogar():
    print('\n*************************************')
    print('Seja Bem-Vindo ao Jogo de Adivinhação')
    print('*************************************')

    total_de_tentativas = 0
    rodada = 1
    numero_secreto = random.randrange(1, 100)

    print('\nQual nível de dificuldade')
    print('Fácil (1) - Médio (2) - Díficil (3)')

    nivel = int(input('\nInfome nível que você deseja jogar: '))

    if (nivel == 1):
        total_de_tentativas = 5

    elif (nivel == 2):
        total_de_tentativas = 3

        if (nivel == 3):
            total_de_tentativas = 1

    for rodada in range(1, total_de_tentativas + 1):
        print('\nTentativas {} a {}'.format(rodada, total_de_tentativas))
        chute = int(input('Informe seu chute: '))

        if (chute < 1 or chute > 100):
            print('\nNÚMERAÇÃO INVALIDA !!!')
            print('Informe um número de 1 a 100')
            continue

        elif (chute == numero_secreto):
            print('\nParábens, você acertou número secreto')
            print('\nFIM DE JOGO')
            break

        if (chute < numero_secreto):
            print('\nSeu chute é menor que número secreto')
            print('Tente Novamente')

        elif (chute > numero_secreto):
            print('\nSeu chute é maior que número secreto')
            print('Tente Novamente')

        if (rodada == total_de_tentativas):
            print('\nVocê atingiu número máximo de tentativas')
            print('{} era seu número secreto'.format(numero_secreto))
            print('\nFIM DE JOGO')

if(__name__ == "__main__"):
    jogar()