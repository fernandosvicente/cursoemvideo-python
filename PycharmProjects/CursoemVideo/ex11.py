#sexo = str(input(' informe seu sexo: [M/F]')).strip().upper()[0]
#while sexo not in 'MmFf':
#    sexo = str(input('dado invalido, digite novamente: ')).strip().upper()
#print('opcao {} registrada com sucesso '.format(sexo))



#from random import randint
#computador = randint(0, 10)
#print('cara me fala um numero de 1 a 10')
#print('quero ver se adivinha')
#acertou = False
#palpite = 0
#while not acertou:
#    jogador = int(input('o numero e?: '))
#    palpite = palpite + 1 #ou pode ser escrito:  palpite += 1
#    if jogador == computador:
#        acertou = True
#    else:
#        if jogador < computador:
#            print('ta quente')
#        else:
#            jogador > computador
#            print('ta frio')
#print('acertou com {} palpites'.format(palpite))


#from time import sleep
#n1 = int(input('primeiro valor: '))
#n2 = int(input('segundo valor: '))
#opcao = 0
#resultado = 0
#maior = 0
#while opcao != 5:
#    print('''    [1] somar
#    [2] multiplicar
#    [3] maior
#    [4] novos numeros
#    [5] sair do programa''')
#    opcao = int(input('>>>>> qual a sua opcao?: '))
#    if opcao == 1:
#       resultado = n1 + n2
#       print('a soma fica : {}'.format(resultado))
#    elif opcao == 2:
#       resultado = n1 * n2
#       print('a multiplicacao fica : {}'.format(resultado))
#    elif opcao == 3:
#      if n1 > n2:
#          maior = n1
#      else:
#          maior = n2
#      print('o maior numero e: {}'.format(maior))
#    elif opcao == 4:
#        print('informe os numeros novamente: ')
#        n1 = int(input('primeiro valor: '))
#        n2 = int(input('segundo valor: '))
#        print('os novos valores sao: {} e {}'.format(n1, n2))
#    elif opcao == 5:
#       sleep(1)
#       print('finalizando')
#       sleep(2)
#    else:
#        print('opcao incorreta escolha opcao novamente:')
#    print('=-='*10)
#print('finalizado com sucesso')



#from math import factorial
#n = int(input('digite um numero para fatorial: '))
#f = factorial(n)
#print('0 fatorial de {} e {}'.format(n, f))
# ou dessa forma
#n = int(input('digite um numero: '))
#c = n
#f = 1
#print('calculando {}! = '.format(n), end='')
#while c > 0:
#    print('{}'.format(c), end='')
#    print(' x ' if c > 1 else ' = ', end='')
#    f = f * c #ou f *= c
#    c = c - 1 #ou c -= 1
#print('{}'.format(f))



#print('geraddor de PA')
#print('-=' * 10)
#primeiro = int(input('primeiro termo: '))
#razao = int(input('razao PA: '))
#termo = primeiro
#cont = 1
#while cont <= 10:
#    print('{} -> '.format(termo), end='')
#    termo = termo + razao # ou termo += razao
#    cont = cont + 1 # ou cont += 1
#print('FIM')



#print('geraddor de PA')
#print('-=' * 10)
#primeiro = int(input('primeiro termo: '))
#razao = int(input('razao PA: '))
#termo = primeiro
#cont = 1
#total = 0
#mais = 10
#while mais != 0:
#    total = total + mais
#    while cont <= total:
#        print('{} -> '.format(termo), end='')
#        termo = termo + razao # ou termo += razao
#        cont = cont + 1 # ou cont += 1
#    print('pausa')
#    mais = int(input('quantos termos vc quer mostrar a mais ?: '))
#print('fim')
#print(' progressao finalizda com {} termos mostrados'.format(cont))



#print('-'*30)
#print('sequecia de Fibonacci')
#print('-'*30)
#n = int(input('quantos termos vc quer mostrar: '))
#t1 = 0
#t2 = 1
#print('~'*40)
#print('{} -> {}'.format(t1, t2), end='')
#cont = 3
#while cont <= n:
#    t3 = t1 + t2
#    print(' -> {}'.format(t3), end='')
#    cont = cont + 1
#    t1 = t2
#    t2 = t3
#print(' -> fim')
#print('~'*40)



#num = 0
#cont = 0
#soma = 0 # ou usar expressao: num = cont = soma = 0
#num = int(input('digite um numero [999] para parar: '))
#while num != 999:
#    soma = soma + num #ou expressao: soma += num
#    cont = cont + 1 # ou usar: cont += 1
#    num = int(input('digite um numero [999] para parar: '))
#print('voce usou {} numeros e soma entre eles {}'.format(cont, soma))



resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('digite um numero: '))
    soma = soma + num #ou usar: soma += num
    quant = quant + 1 #ou usar: quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('quer continuar? [S/N]: ')).upper().strip()[0]
media = soma / quant
print('vc digitou {} numeros, a soma deles {} e a media {}'.format(quant, soma, media))
print('o maior {} e o menor {}'.format(maior, menor))



