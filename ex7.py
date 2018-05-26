"""
Programa ex7.py
Descrição: Preço a pagar pela energia
Autor: Gabriel Souto Ribeiro Bouyssounade
Data: 25/05/2018
Versão: 0.0.1
"""

# Entrada de dados

consumo = float(input('Insira o consumo de energia:'))
tipo = input('Insira o tipo de instalação sendo R para residências, I para indústrias e C para comércio:')

# Decisão

if tipo == 'R' :
    if consumo > 500 :
        conta = 0.65 * consumo
    else :
        conta = 0.4 * consumo
elif tipo == 'I' :
   if consumo > 1000 :
       conta = 0.6 * consumo
   else :
       conta = 0.55 * consumo
elif tipo == 'C' :
   if consumo > 5000 :
       conta = 0.6 * consumo
   else :
       conta = 0.55 * consumo
else :
   print('Erro, instalação inválida.')

# Saída

if tipo == 'R' or tipo == 'I' or tipo == 'C' :
    print('Sua conta de luz é de:', conta)
