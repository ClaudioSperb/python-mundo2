print('Iterando com Dicionários')
estados = []
uf_sigla = dict()
for c in range(3):
    uf_sigla ['uf']= str(input('UF: ')).upper()
    uf_sigla ['sigla']= str(input('Sigla: ')).upper()
    
    estados.append(uf_sigla.copy())
for e in uf_sigla:
    for c,v in uf_sigla.items():
        print(c, v)