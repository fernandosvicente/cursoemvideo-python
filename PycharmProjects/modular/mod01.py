from uteis import numeros

num = int(input('digite um numero'))
fat = numeros.fatorial(num)
print(f'o fatorial de {num} e {fat}')
print(f'o dobro de {num} e {numeros.dobro(num)}')
print(f'o triplo de {num} e {numeros.triplo(num)}')

# pode ser feito dessa forma a importação do modulo essa e a mais segura
#import uteis
#
#num = int(input('digite um numero'))
#fat = uteis.fatorial(num)
#print(f'o fatorial de {num} e {fat}')
#print(f'o dobro de {num} e {uteis.dobro(num)}')
#print(f'o triplo de {num} e {uteis.triplo(num)}')