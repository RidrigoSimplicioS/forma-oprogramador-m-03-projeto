# -*- coding: utf-8 -*-
"""M-02-PROJETOipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RJofISLzwbE9E_0oeCysutXsuj_EoGd-

# JOGO PAR OU IMPAR

1 Definir quem serão os jogadores

2 Definir quem escolhe primeiro

3 Definir a escolha entre par e impar

4 Coletar o os números escolhidos entre os jogadores

5 Calcula se a soma dos números é par ou impar

6 Informar quem ganhou !
"""

jogador1 = input('-> Dijite o nome do primeiro jogador:')
jogador2 = input('-> Dijite o nome do segundo jogador:')
print(f' // Quem escolher primeiro, {jogador1} ou {jogador2}?')
primeiro_jogador = input(f'-> Digite 1 para escolher {jogador1} ou 2 para escolher {jogador2}. ')
segundo_jogador = None

if primeiro_jogador == '1':
  primeiro_jogador = jogador1
  segundo_jogador = jogador2
elif primeiro_jogador == '2':
  primeiro_jogador = jogador2
  segundo_jogador = jogador1

print('// Digite 0 para esolher PAR ou 1 para escolher IMPAR ')
escolha = input(f'{primeiro_jogador}, Você quer par ou impar?')
escolha2 = None

if escolha == 'impar' or 'impar' or escolha == '1':
  escolha = 'impar'
  escolha2 = 'par'
elif escolha == 'par' or escolha == '0':
  escolha = 'par'
  escolha2 = 'impar'

print(f'{segundo_jogador}, Você ficou com {escolha2} ')

numero1 = int(input(f'-> {primeiro_jogador}, escolha um número:'))
numero2 = int(input(f'-> {segundo_jogador}, escolha um número :'))

soma = numero1 + numero2

if soma % 2 == 0 :
  vencedor = 'par'
else:
  vencedor = "impar"
if vencedor == escolha:
  print(f'//{primeiro_jogador} venceu:')
else:
  print(f'//{segundo_jogador} venceu:')