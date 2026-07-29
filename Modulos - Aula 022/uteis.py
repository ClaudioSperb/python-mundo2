def fatorial(n):
    f = 1
    for c in range(1, n +1 ):
        f *= c
    return f


def dobro(n):
    return n * 2


def triplo(n):
    return n * 3

def titulo(msg):
    tam = len(msg)
    print('=-' * tam)
    print(msg.center(tam * 2))
    print('=-' * tam)