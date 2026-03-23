#CONDIÇÕES ANINHADAS
nome = str(input('Digite seu nome: ')).upper().strip()
if nome == 'CLAUDIO':
    print('Que nome bonito!')
elif nome == 'JOSIANE' or nome == 'BRIANA':
    print('Seu nome é bem bonito, prazer em te conhecer !!!')
elif nome in 'ELTON NILDO FELIPE RENATO':
    print('AH conheço vocês, são da REK REBOQUES')
else:
    print(f'Tenha um ótimo dia {nome}')