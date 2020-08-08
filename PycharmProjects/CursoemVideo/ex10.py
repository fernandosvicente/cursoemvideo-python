#from time import sleep
#for cont in range(10, -1, -1):
#    print(cont)
#    sleep(0.5)
#for par in range(1, 51):
#    # outra forma de escreve: print(par)
#    if par % 2 == 0:
#        print(' {} '.format(par), end='')
#        sleep(0.2)
#print('acabou')
#for n in range(2, 51, 2):
#    # outra forma de escreve: print(par)
#    print(' {} '.format(n), end='')
#    sleep(0.2)
#print('acabou')

#soma = 0
#cont = 0
#for c in range(1, 501, 2):
#    if c % 3 == 0:
#     # print(c, end=' '), para extrair os numeros
#        cont = cont + 1 # outra sintaxe cont += 1
#        soma = soma + c # outra sintaxe soma += c
#print('a soma dos numeros e {} e contamos {} numeros'.format(soma, cont))


#num = int(input('digite o numero para ver sua tabuada: '))
#for c in range(1, 11):
#    print('{} x {:2} = {}'.format(num, c, num * c))



#soma = 0
#cont = 0
#for c in range(1, 7):
#    num = int(input(' digite o {}º valor : '.format(c)))
#    if num % 2 == 0:
#        soma = soma + num # outra forma sintaxe, soma += num
#        cont = cont + 1   # outra forma sintaxe, cont += 1
#print('voce informou {} numeros pares e a soma foi {}'.format(cont, soma))



#primeiro = int(input('primeiro termo '))
#razao = int(input('razao '))
#ultimo = int(input('ultimo termo'))
#ultimo = primeiro + (ultimo - 1)* razao
#for c in range(primeiro, ultimo + razao, razao):
#    print('{} '.format(c), end=' -> ')
#print('acabaou')



#num = int(input('digite um numero :'))
#tot = 0
#for c in range(1, num + 1):
#    if num % c == 0:
#        print('\033[33m', end=' ')
#        tot = tot + 1
#    else:
#        print('\033[31m', end=' ')
#    print('{} '.format(c), end='')
#print(' \n\033[mo numero {}, foi divisivel {} vezes'.format(num, tot))
#if tot == 2:
#    print(' E numero primo')
#else:
#    print('E numero nao primo')



#frase = str(input('digite a frase ')).strip().upper()
#palavras = frase.split()
#junto = ''.join(palavras)
#print('vc digitou a frase : {} '.format(junto))
# forma 01 de resolver
#inverso = ''
#for letra in range(len(junto) -1, -1, -1):
#    inverso = inverso + junto[letra]
# forma 02 de resolver
#inverso = junto[::-1]
#print('o inverso de {} e {} '.format(junto, inverso))
#if inverso == junto :
#    print('palidromo')
#else:
#    print('nao e palidromo')



#from datetime import date
#atual = date.today().year
#totmaior = 0
#totmenor = 0
#for pess in range(1, 8):
#    nasc = int(input('em que ano a {}ª pessoa nasceu? '.format(pess)))
#    idade = atual - nasc
#    if idade >= 21:
#        totmaior = totmaior + 1
#    else:
#        totmenor = totmenor + 1
#print('ao todo tivemos {} pessoas maiores de idade '.format(totmaior))
#print('ao todo tivemos {} pessoas menores de idade '.format(totmenor))



#maior = 0
#menor = 0
#for p in range(1, 6):
#    peso = float(input('peso da {}ª pessoa: '.format(p)))
#    if p == 1:
#        maior = peso
#        menor = peso
#    else:
#        if peso > maior:
#            maior = peso
#        if peso < menor:
#            menor = peso
#print('o maior peso lido foi: {} '.format(maior))
#print('o menor peso lido foi: {} '.format(menor))


somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range (1, 5):
    print('-------{}ª PESSOA ------'.format(p))
    nome = str(input('nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('sexo [M/F]: ')).strip()
    somaidade = somaidade + idade # ou somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
         maioridadehomem = idade
         nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20 + 1

mediaidade = somaidade / 4
print(' a media de idade do grupo  e {} anos'.format(mediaidade))
print(' o homem mais velho tem {} anos e se chama {}'.format(maioridadehomem,nomevelho))
print(' ao todo sao {} mulheres menores de 20 anos'.format(totmulher20))