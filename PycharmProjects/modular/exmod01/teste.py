from exmod01 import moeda

p = float(input('digite o preço: R$'))
print(f'a metade de R$ {p} e R$ {moeda.metade(p)}')
print(f'o dobro de R$ {p} e R$ {moeda.dobro(p)}')
print(f'aumentando 10%, temos R$ {moeda.aumentar(p, 10)}')
print(f'dimuindo 10%, temos R$ {moeda.diminuir(p, 10)}')
