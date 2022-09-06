import random
from secrets import choice
bot = random.choice (['pedra','papel','tesoura'])
escolha = input('''Escolha entre pedra papel ou tesoura: ''')

print(f'Você escolheu {escolha}')
print(f'O computador escolheu {bot}')

if bot == escolha:
    print('Empate!')
elif bot == 'pedra' and escolha == 'papel':
    print('Você ganhou!')
elif bot == 'pedra' and escolha == 'tesoura':
    print('Você perdeu!')
elif bot == 'tesoura' and escolha == 'pedra':
    print('Você ganhou!')
elif bot == 'tesoura' and escolha == 'papel':
    print('Você perdeu!')
elif bot == 'papel' and escolha == 'tesoura':
    print('Você ganhou!')
elif bot == 'papel' and escolha == 'pedra':
    print('Você perdeu!')