print (f'{10 * '~'} CARDÁPIO {10 * '~'}')
cardapio = [
    'FRANGO A KIEV',
    'FILET',
    'BOLINHO DE BACALHAU',
    'BATATA-FRITA',
    'CAMARÃO',
    'COSTELA AO MOLHO BARBECUE'
]

item = cardapio.pop(0)

while item != 'CAMARÃO':
    print('Esse item não é camarão, -> Próximo item -> ')
    item = cardapio.pop(0)
print('Pronto, Camarão encontrado! ')