import math
import random


def calcularPotencia(a, b):
    p = a**b
    return p


def sortearValores(c, d):
    rd = random.randrange(c, d)
    return rd


def exibirMenu():
    print('MENU DE OPÇÕES')
    print('1- Exibir a raiz quadrada de 9')
    print('2- Exibir a potencia de 2 numeros')
    print('3- Sortear um numero aleatorio entre dois numeros')
    print('4- Sair')

    teste = int(input('Digite a opção desejada'))

    if (teste == 1):
        print('A raiz quadrada de 9 é: ')
        print(math.sqrt(9))

    elif (teste == 2):
        a = int(input('Digite o numero que receberá a potencia: '))
        b = int(input('Digite a potencia: '))
        pt = calcularPotencia(a, b)
        print(pt)

    elif (teste == 3):
        c = int(input('Digite o numero minimo a ser sorteado: '))
        d = int(input('Digite o numero maximo a ser sorteado: '))
        st = sortearValores(c, d)
        print(st)

    elif (teste >= 4 or teste < 1):
        print('Deu pau no sistema tmj')

    if (teste < 4 and teste > 0):

        exibirMenu()


exibirMenu()
