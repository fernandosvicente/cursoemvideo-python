#temp = []
#princ = []
#maior = menor = 0
#while True:
#    temp.append(str(input('nome: ')))
#    temp.append(float(input('peso: ')))
#    if len(princ) == 0:
#        maior = menor = temp[1]
#    else:
#        if temp[1] > maior:
#            maior = temp[1]
#        if temp[1] < menor:
#            menor = temp[1]
#    princ.append(temp[:])
#    temp.clear()
#    resp = str(input('quer continuar? [S/N] '))
#    if resp in 'Nn':
#        break
#print('*=*'*30)
#print(f'os dados foram {princ}')
#print(f' ao todo vc cadastrou {len(princ)} pessoas')
#print(f' o maior peso foi {maior} kg, ', end=' ')
#for p in princ:
#    if p[1] == maior:
#        print(f'{p[0]}')
#print()
#print(f' o menor peso foi {menor} kg,  ', end=' ')
#for p in princ:
#    if p[1] == menor:
#        print(f'{p[0]}')



#num = [[], []]
#valor = 0
#for c in range(1, 8):
#    valor = int(input(f'digite o {c}º valor: '))
#    if valor % 2 == 0:
#        num[0].append(valor)
#    else:
#        num[1].append(valor)
#print('-=-'*30)
#num[0].sort()
#num[1].sort()
#print(f'os valores pares digitados foram : {num[0]}')
#print(f'os valores impares digitados foram : {num[1]}')



#matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#spar = maior = scol = 0
#for l in range(0, 3):
#    for c in range(0, 3):
#        matriz[l][c] = int(input(f'digite um valor para {l}; {c}: '))
#print('-=-'*10)
#for l in range(0, 3):
#    for c in range(0, 3):
#        print(f'[{matriz [l][c]:^3}]', end='')
#        if matriz[l][c] % 2 == 0:
#            spar += matriz[l][c]
#    print()
#print(f'a soma dos valores pares é {spar}')
#for l in range(0, 3):
#    scol += matriz[l][2]
#print(f'a soma da terceira coluna e: {scol}')
#for c in range(0, 3):
#    if c == 0:
#        maior = matriz[1][c]
#    elif matriz [1][c] > maior:
#        maior = matriz[1][c]
#print(f'o maior valor da segunda linha e: {maior}')



#from random import randint
#lista = list()
#jogos = list()
#quant = int(input('quantos jpgps vc vai fazer? : '))
#tot = 1
#while tot <= quant:
#    cont = 0
#    while True:
#        num = randint(1, 60)
#        if num not in lista:
#            lista.append(num)
#            cont += 1 # ou cont = cont + 1
#        if cont >= 6:
#            break
#    lista.sort()
#    jogos.append(lista[:])
#    lista.clear()
#    tot = tot + 1
#print('-=-'*3, f'sorteando {quant} jogos ')
#for i, l in enumerate(jogos):
#    print(f'jogo {i+1}: {l}')



ficha = list()
while True:
    nome = str(input('nome: '))
    nota1 = float(input('nota 1: '))
    nota2 = float(input('nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('quer continur? [S/N] '))
    if resp in 'Nn':
        break
print('='*30)
print(f'{"nº":<4}{"nome":<10}{"media":>8}')
print('='*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('='*35)
    opc = int(input('mostrar nota de qual aluno? (999 - intenrrompe'))
    if opc == 999:
        print('finalizando')
        break
    if opc <= len(ficha) - 1:
       print(f'notas de {ficha[opc][0]} sao {ficha[opc][1]}')
print('concluido')