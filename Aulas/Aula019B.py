print('DADOS FILMES')
filmes = {
    "titulo": 'Mortal Kombat - o Filme',
    "diretor": 'Paul W.S. Anderson',
    "ano": 1995
}
print(filmes)
filmes["tema"] = 'Ação / Aventura'
print(filmes)
del filmes['titulo']
print(filmes)
print(filmes.keys())

# Utilizamos o filmes.itens() para utilizar o k, v como no enummerate.
for k,v in filmes.items():
    print(f'O {k} é {v}')