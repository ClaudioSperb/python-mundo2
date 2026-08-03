def metade(num=0, formato=False):

    '''
    Função que divide o valor na metade
    :param num: Recebe o valor do input do programa principal
    :param formato: True ele foramata o valor chamando a função moeda e False fica somente o valor normal
    :return: Retorna o valor pela metade.
    '''

    res = num / 2
    return res if formato is False else moeda(res)


def dobro(num=0, formato=False):
    '''
    Função que duplica o valor
    :param num: Recebe o valor do input do programa principal
    :param formato: True ele foramata o valor chamando a função moeda e False fica somente o valor normal
    :return: Retorna o valor em dobro
    '''

    res = num * 2
    return res if formato is False else moeda(res)


def aumentar(num=0, porc=0, formato=False):
    '''
    Função que aumenta o valor em (porc)%
    :param num: Recebe o valor do input do programa principal
    :param porc: Recebe o valor e converte em porcentagem
    :param formato: True ele foramata o valor chamando a função moeda e False fica somente o valor normal
    :return: Retorna o valor final com a porcentagem aplicada
    '''

    res = num + (num * porc) / 100
    return res if formato is False else moeda(res)


def diminuir(num=0, porc=0, formato=False):
    '''
    Função que diminui o valor (num) em (porc) %
    :param num: Recebe o valor do input do programa principal
    :param porc: Recebe o valor e converte em porcentagem
    :param formato: True ele foramata o valor chamando a função moeda e False fica somente o valor normal
    :return: Retorna o valor final com a porcentagem aplicada
    '''

    res = num - (num * porc) / 100
    return res if formato is False else moeda(res)


def moeda(num=0, moeda='R$'):
    '''
    Função que formata o valor em RS
    :param num: Recebe o valor do input do programa principal
    :param moeda: Adiciona o R$ e substitui o '.' por ',' - Deixando formatado o valor em Real
    :return: O valor de num ja com R$ e ' , '
    '''

    return f'{moeda}{num:.2f}'.replace('.', ',')


def titulo(msg):
    tam = len(msg)
    print('=====' * tam)
    print(msg.center(tam * 5))
    print('=====' * tam)


def resumo(num, taxaa=10, taxadim=5):
    '''
    Função que passa um resumo das Informações.
    :param num: Recebe o valor do input do programa principal
    :param taxaa: Tem que ser passado na chamada da função
    :param taxadim: Tem que ser passado na chamada da função
    :return: Retorna uma tabela com todos os dados
    '''

    titulo('RESUMO')
    print(f'Valor Analisado: \t{moeda(num)}')
    print(f'Dobro do Valor: \t{dobro(num, True)}')
    print(f'Metade do Valor: \t{metade(num, True)} ')
    print(f'{taxaa}% de Aumento: \t{aumentar(num, taxaa, True)}')
    print(f'{taxadim}% de Redução: \t{diminuir(num, taxadim, True)}')
    print('-' * 30)
