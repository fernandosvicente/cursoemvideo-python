#ajuda do python definições usar a palavra - help() para sair da ajuda interativa digitar - quit
#ajuda interativa digitar - help(entre parentes a função desejada)
#para adiconar observações a uma função criada basta adicionar 03 apas duplas """ apos a descriçao da funçao
# exemplo; def ... apos """ entrada  na saida"""


#def fatorial(num=1):
#    f = 1
#    for c in range(num, 0, -1):
#        f *= c
#    return f
#
#
#n = int(input('digite um valor: '))
#print(f'o fatorial de {n} e igual a {fatorial(n)}')



#def voto(ano):
#    from datetime import date
#    atual = date.today().year
#    idade = atual - ano
#    if idade < 16:
#       return f'com {idade} anos nao pode votar'
#    elif 16 <= idade < 18 or idade >= 65:
#        return f'com {idade} anos voto opcional'
#    else:
#       return f'com {idade} anos voto e obrigatorio'
#
#
#nat = int(input('digite o ano que vc nasceu: '))
#print(voto(nat))



#def fatorial(n, show=False):
#    """
#    -> calcula o faotrial o numero
#    -> docstrigs = utilizar tres aspas para armazenar legenda ao programa
#    :param n: numero do fatorial a executar
#    :param show: mostra a formula - true ou nao - false
#    :return: returna o valor do calculo feito na função
#    """
#    f = 1
#    for c in range(n, 0, -1):
#        if show:
#            if c > 1:
#                print(f'{c} x ', end='')
#            else:
#                print(f'{c} = ', end='')
#        f *= c
#    return f
#
#
#print(fatorial(6, show=True))
#help(fatorial)



#def ficha(jog='<desconhecido>', gol=0):
#    print(f'o jogador {jog} fez {gol} no campeonato')
#
#
#n = str(input("nome do jogador: "))
#g = str(input("numero de gols: "))
#if g.isnumeric():
#    g = int(g)
#else:
#    g = 0
#if n.strip() == '':
#    ficha(gol=g)
#else:
#    ficha(n, g)



#def leiaint(msg):
#    ok = False
#    valor = 0
#    while True:
#        n = str(input(msg))
#        if n.isnumeric():
#            valor = int(n)
#            ok = True
#        else:
#            print('\033[0;31mErro...digite um numero..\033[m')
#        if ok:
#            break
#    return valor
#
#
#n = leiaint('digite um numero: ')
#print(f'vc acabou de digitar o numero {n}')



#def notas(*n, sit=False):
#    r = dict()
#    r['total'] = len(n)
#    r['maior'] = max(n)
#    r['menor'] = min(n)
#    r['media'] = sum(n)/len(n)
#    if sit:
#        if r['media'] >= 7:
#            r['situacao'] = 'boa'
#        elif r['media'] >= 5:
#            r['situacao'] = 'razoavel'
#        else:
#            r['situacao'] = 'ruim'
#    return r
#
#
#resp = notas(5.5, 6.5, 8.7, 9, sit=True)
#print(resp)



c = ('\033[m',         # 0 - sem cores
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[7;30m',      # 4 - branco
     );

def ajuda(com):
    titulo(f'acessando o manual do comando \'{com}\'', 2)
    print(c[4], end='')
    help(com)
    print(c[0], end='')


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


comando = ''
while True:
    titulo('sistema de ajuda Pyhelp', 3)
    comando = str(input("função ou biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ate logo', 1)