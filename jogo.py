import random

jogar_novamente = 's'
while jogar_novamente == 's':
    numero_secreto = random.randint(1, 100)
    palpite = int(input('Palpite do Numero:'))
    tentativas= 1

    while palpite != numero_secreto and tentativas < 5:
            if palpite > numero_secreto:
                print('Digite um numero menor')
            else:
                print('Digite um numero maior')

            palpite = int(input('Palpite do Numero:'))
            tentativas+=1

    if palpite == numero_secreto:
        print(f'parabens acertou mo numero : {tentativas}')

    else :
        print (f'Errou o numero era : {numero_secreto}')
    jogar_novamente = input('Deseja jogar novamente? (s/n)').lower()