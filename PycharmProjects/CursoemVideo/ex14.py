#listanum = [] # ou listanum = lista()
#maior = 0
#menor = 0
#for c in range(0, 5):
#    listanum.append(int(input(f' digite um numero para posicao {c}: ')))
#    if c == 0:
#        maior = menor = listanum[c]
#    else:
#        if listanum[c] > maior:
#            maior = listanum[c]
#        if listanum[c] < menor:
#            menor = listanum[c]
#print('-'*30)
#print(f'voce digitou os valores {listanum}')
#for i, v in enumerate(listanum):
#    if v == maior:
#        print(f'o maior valor digitado foi {maior} na posicao {i}..')
#    else:
#        if v == menor:
#         print(f' e o menor foi {menor} na posicao {i}..')



#numeros = list()
#while True:
#    n = int(input('digite o valor '))
#    if n not in numeros:
#        numeros.append(n)
#        print('valor adicionado')
#    else:
#        print('erro !!! valor duplicado')
#    r = str(input('quer continuar? [S/N]: '))
#    if r in 'nN':
#        break
#numeros.sort()
#print(f'vc digitou os valor {numeros}..')



#lista = []
#for c in range(0, 5):
#    n = int(input(' digite um valor: '))
#    if c == 0:
#        lista.append()
#    elif n > lista[len(lista)-1]: #ou lista[-1]
#        lista.append()
# ou a logica pode ser
#    if c == 0 or n > lista[-1]:
#        lista.append(n)
#        print('adicionado na lista')
#    else:
#        pos = 0
#        while pos < len(lista):
#            if n <= lista[pos]:
#                lista.insert(pos, n)
#                print(f'adicionado na posicao {pos} da lista..')
#                break
#            pos += 1
#print('-'*30)
#print(f'os valores digitados em ordem foram {lista}')



#valores = [] # ou list()
#while True:
#    valores.append(int(input('digite um valor: ')))
#    resp = str(input(' quer continuar?: [S/N]'))
#    if resp in 'Nn':
#        break
#print('-'*30)
#print(f'vc digitou {len(valores)} elementos')
#valores.sort(reverse=True)
#print(f'os valores decrescentes sao {valores}')
#if 5 in valores:
#    print(' o valor 5 faz parte da lista')
#else:
#    print('o 5 nao foi encontrado')



#num = list()
#pares = list()
#impares = list()
#while True:
#    num.append(int(input(' digite um numero')))
#    resp = str(input('vc quer continuar? [S/N]: '))
#    if resp in 'Nn':
#        break
#for i, v in enumerate(num):
#    if v % 2 == 0:
#        pares.append(v)
#    elif v % 2 == 1:
#        impares.append(v)
#print('-'*30)
#print(f'a lista completa {num}')
#print(f' a lista de pares {pares}')
#print(f' a lista de impares {impares}')



expr = str(input('digite a expressao: '))
pilha = []
for sim in expr:
    if sim == '(':
       pilha.append('(')
    elif sim == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('sua expressao esta valida')
else:
    print('sua expressao esta errada')
