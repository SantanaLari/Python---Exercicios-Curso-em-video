time = ('America FC Saf', 'Athletico', 'Atlético Mineiro', 'Bahia', 'Botafogo',
        'Corinthians', 'Coritiba', 'Cruzeiro Saf', 'Cuiabá Saf', 'Flamengo',
        'Fluminense', 'Fortaleza', 'Goiás', 'Grêmio', 'Internacional',
        'Palmeiras', 'Red Bull', 'Santos', 'São Paulo', 'Vasco da Gama')

#a) Os 5 primeiros times
print(time[:5])
#b) Os últimos 4 colocados
print(time[-4:])
#c) Times em ordem alfabética
print(sorted(time))
#d) Em que posição está o time da Chapecoense
chapecoense = 'Chapecoense' in time
if (chapecoense == False):
    print('A Chapecoense não está na lista')
else:
    print(time.index('Chapecoense'))