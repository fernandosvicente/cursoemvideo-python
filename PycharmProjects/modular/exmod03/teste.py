from exmod03.utilidadescev import moeda
from exmod03.utilidadescev import dado

while True:
    try:
        p = dado.leiadinheiro('digite o preço:R$')
        moeda.resumo(p, 20, 12)
        break
    except:
        print(f'\033[0;31mERRO: o numero é invalido, digite um numero\033[m')
