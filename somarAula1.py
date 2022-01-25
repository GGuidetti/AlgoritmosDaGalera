from re import X


def somar(num):
    i = 0
    x = 0
    while num > i:
        i += 1
        x += i

    return x


print(somar(int(input('Digite um numero'))))
