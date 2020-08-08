from exmod02 import moeda

p = float(input('digite o preço: R$'))
print(f'a metade de {moeda.moeda(p)} e {moeda.metade(p, True)}')
print(f'o dobro de {moeda.moeda(p)} e {moeda.dobro(p, True)}')
print(f'aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'dimuindo 10%, temos {moeda.diminuir(p, 13, True)}')
