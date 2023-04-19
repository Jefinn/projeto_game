import adivinhacao
import forca

print('***********************')
print('****Escolha um jogo****')
print('***********************')

print('\n (1) ADIVINHA - (2) FORCA')

jogo = int(input('Qual jogo você deseja jogar: '))

if(jogo == 1):
    print('\nJogando Adivinha')
    adivinhacao.jogar()

elif(jogo == 2):
    print('\nJogando Forca')
    forca.jogar()

