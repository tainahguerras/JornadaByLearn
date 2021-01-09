def soma(lista):
  som = sum(lista)
  print('O resultado da soma é', som)
def subtracao(lista):
  sub = lista[0] - lista[1]
  print('O resultado da subtração é', sub)
def divisao(lista):
  div = lista[0] / lista[1]
  print('O resultado da divisão é', div)
def multiplicacao(lista):
  mul = lista[0] * lista[1]
  print('O resultado da multiplicação é', mul)

numeros = []
numeros.append(float(input('Digite o primeiro número:')))
numeros.append(float(input('Digite o segundo número:')))

operacao = input('Digite a operação desejada:')
if operacao.lower() == 'soma':
  soma(numeros)
if operacao.lower() == 'subtração':
  subtracao(numeros)
if operacao.lower() == 'divisão':
  divisao(numeros)
if operacao.lower() == 'multiplicação':
  multiplicacao(numeros)