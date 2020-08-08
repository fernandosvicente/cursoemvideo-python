#def area(larg, comp):
#    a = larg * comp
#    print(f'a area do terreno {larg} x {comp} : {a} metros quatrados')
#
#
#
#print('controle de terrenos')
#print('=-=' * 20)
#l = float(input('largura (m) '))
#c = float(input('comprimento (m) '))
#area(l, c)



#def escreva(msg):
#    tam = len(msg)
#    print('-' * tam)
#    print(msg)
#    print('~' * tam)
#
#
#escreva('fernando')



#from time import sleep
#
#
#def contador(i, f, p):
#    print('=-=' * 30)
#    print(f'contagem de {i} ate {f} de {p} em {p}')
#    if p < 0:
#        p *= -1
#    if p == 0:
#        print('erro !! vou contar de 1 em 1')
#        p = 1
#    if i < f:
#        cont = i
#        while cont <= f:
#            print(f'{cont} ', end='')
#            sleep(0.3)
#            cont += p
#        print('fim')
#    else:
#        cont = i
#        while cont >= f:
#            print(f'{cont} ', end='')
#            sleep(0.3)
#            cont -= p
#        print('fim')
#
#
#contador(1, 10, 1)
#contador(10, 0, 2)
#print('agora quais os seus nuemros? :')
#inicio = int(input('numero inicial: '))
#fim = int(input('numero final: '))
#passo = int(input('o passo deve ser de: '))
#contador(inicio, fim, passo)



#def maior(* num):
#    cont = maior = 0
#    print('=-=' * 10)
#    print('analisando os numeros.... ')
#    for valor in num:
#        print(f'{valor} ', end='')
#        if cont == 0:
#            maior = valor
#        else:
#            if valor > maior:
#                maior = valor
#        cont += 1
#    print(f'\nforam informados {cont} valores ao todo')
#    print(f'o maior valor e {maior}')
#
#
#maior(2, 5 , 8 , 1, 6, 7)
#maior(9, 5, 1, 3, 5, 7)
#maior(8, 5)
#maior(-1, -5, 0, 7)
#maior(6)
#maior()



from random import randint


def sorteia(lista):
    print('sorteando os numeros sao: ')
    for c in range(0, 6):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'\nsomando os valores pares de {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
somapar(numeros)
