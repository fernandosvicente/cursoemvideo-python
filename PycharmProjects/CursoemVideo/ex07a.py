n = int(input('digite um numero: '))
a = n - 1
s = n + 1
d = n*2
t = n*3
r = n**(1/2)
q = n**2
c = n**3
print('analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n,a,s))
print('o dobro de {} é : {}, o triplo de {} é : {} \n a raiz quadrada de {} é : {:.2f}'.format(n,d,n,t,n,r), end="")
print('o quadrado de {} é de: {}, o cubo de {} é de: {}'.format(n,q,n,c))

n1 = int(input('digite um valor: '))
print('analisando o valor {}, seu antecessor é {} e seu sucessor é {}'.format(n1,(n1-1),(n1+1)))

'ordem precedencia (), **, * / // %, + -'\
' + soma, - subtração, * multiplicação, / divisao, ** exponenciaçõ, //divisor inteiro, % resto inteiro'
'para quebrar pagina usar (\n)e para juntar usar (, end="")'

n1 = float(input('primeira nota do aluno: '))
n2 = float(input('segunda nota do aluno: '))
m = (n1 + n2)/2
print('a média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, m))

medida = float(input('uma distância em metros: '))
'km hm dam m dm cm mm'
dm = medida*10
cm = medida*100
mm = medida*1000
dam = medida/10
hm = medida/100
km = medida/1000
print('a medida de {}m corresponde a {:.0f}dm , {:.0f}cm , {:.0f}mm'.format(medida, dm, cm, mm))
print('a medida de {}m corresponde a {}dam , {}hm , {}km'.format(medida, dam, hm, km))

num= int(input('digite um numero para ver sua tabuada: '))
print('-'*14)
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('-'*14)

real = float(input('digite o valor que vc tem na carteira? R$'))
dolar = real / 3.27
print('com R${:.2f} vc pode comprar U$${:.2f}'. format(real, dolar))

print('-'*20)
print('orcamento para pintar parede')
print('ponto importante: 01 litro de tinta para cada 02 m²')
c = float(input('digite a medida do comprimento da parede em metros: '))
alt = float(input('digite a medida da altura da parede em metros: '))
r = float(input('digite a taxa de rendimento para tinta: '))
t = (c * alt)/r

print('as medidas da parede são: {} m e {} m , vc irá usar no total {} l de tinta'.format(c, alt, t))
