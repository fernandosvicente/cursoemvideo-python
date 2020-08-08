#soma = cont = 0
#while True:
#    num = int(input('digite um valor (999 para parar): '))
#    if num == 999:
#        break
#    cont = cont + 1 # ou: cont += 1
#    soma = soma + num  # ou: soma += num
# mostrar valor como : print('a soma dos valores foi {}'.format(soma))
#print(f'a soma dos {cont} valores foi {soma}')



#while True:
#    n = int(input('quer ver a tabuada de qqual valor?: '))
#    if n < 0:
#        break
#    print('-'*30)
#    for c in range(1, 11):
#        print(f'{n} x {c} = {n*c}')
#    print('-'*30)
#print('erro!! tabuada de numero negativo, fim!')



#from random import randint
#v = 0
#while True:
#    jogador = int(input('diga o valor: '))
#    computador = randint(0, 6)
#    total = jogador + computador
#    tipo = ' '
#    while tipo not in 'PpIi':
#        tipo = str(input('par ou impar? [P/I] ')).strip().upper()[0]
#    print(f'o jogador {jogador} e o computador {computador}, o total {total} ', end='')
#    print('-> deu par' if total % 2 == 0 else '-> deu impar')
#    if tipo == 'P':
#        if total % 2 == 0:
#            print('jogador venceu')
#            v = v + 1 # v += 1
#        else:
#            print('o computador ganhou')
#            break
#    elif tipo == 'I':
#        if total % 2 == 1:
#            print(' jogador venceu')
#            v = v + 1 # v += 1
#        else:
#            print('o computador venceu')
#            break
#    print('vamos jogar novamente?')
#print(f'o jogador ganhou {v} vezes')



#tot18 = toth = totm20 = 0
#while True:
#    idade = int(input('idade: '))
#    sexo = ' '
#    while sexo not in 'MF':
#        sexo = str(input('sexo: [M/F]')).strip().upper()[0]
#    if idade >= 18:
#        tot18 = tot18 + 1 # ou: tot18 += 1
#    if sexo == 'M':
#        toth = toth + 1 # ou toth += 1
#    if sexo == 'F' and idade < 20:
#        totm20 = totm20 + 1 # ou: totm20 += 1
#    resp = ' '
#    while resp not in 'SN':
#        resp = str(input('quer continuar? [S/N] ')).strip().upper()[0]
#    if resp == 'N':
#       break
#print(f'{tot18} pessoas maiores de 18 anos')
#print(f'{toth} homens cadastrados')
#print(f'{totm20} mulheres com menos de 20 anos')



#total = totmil = menorp = contp = 0
#barato = ' '
#while True:
#    prod = str(input('nome do produto: '))
#    preco = float(input('preco do produto: R$ '))
#    contp = contp + 1 # ou contp =+ 1
#    total = total + preco # ou total += preco
#    if preco > 1000:
#        totmil = totmil + 1 #ou: totmil += 1
#    if contp == 1:
#        menorp = preco
#        barato = prod
#    else:
#        if preco < menorp:
#           menorp = preco
#           barato = prod
# outra forma reduzida de escrever quando bloco forem iguais
#           if contp == 1 or preco < menorp
#               menorp = preco
#               barato = prod
#    resp = ' '
#    while resp not in 'SN':
#        resp = str(input('quer continuar [S/N] ')).strip().upper()[0]
#    if resp == 'N':
#        break
#print('{:-^40}'.format('fim'))
#print(f'o total da compra foi R$ {total:.2f}')
#print(f'temos {totmil} produtos custando acima de R$ 1000')
#print(f'o {barato} tem o menor preco : {menorp:.2f}' )



print('=' * 30)
print('{:^30}'.format('banco ccs'))
print('=' * 30)
valor = int(input('informe o valor de saque: '))
total = valor
céd = 100
totcéd = 0
while True:
    if total >= céd:
        total = total - céd # ou: total -= ced
        totcéd = totcéd + 1 # ou: totced += 1
    else:
        if totcéd > 0:
            print(f'total de {totcéd} cedulas de R$ {céd}')
        if céd == 100:
            céd = 50
        elif céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 5
        elif céd == 5:
            céd = 2
        totcéd = 0
        if total == 0:
            break
print('=' * 30)
print('volte sempre ao banco css')

