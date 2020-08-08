#nome = str(input('digite seu nome completo: ')).strip()
#print('analisando seu nome...')
#print('seu nome em maiusculas é {}'.format(nome.upper()))
#print('seu nome em minusculas é {}'.format(nome.lower()))
#print('seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('seu primeiro nome tem {} letras'.format(nome.find(' ')))
#separa = nome.split()
#print('seu nome possui a seguinte lista: {}'.format(nome.split()))
#print('seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

#num = int(input('informe um numero: '))
#u = num // 1 % 10
#d = num // 10 % 10
#c = num // 100 % 10
#m = num // 1000 % 10
#print('analisando o numero {}'.format(num))
#print('unidade: {}'.format(u))
#print('dezena: {}'.format(d))
#print('centena: {}'.format(c))
#print('milhar: {}'.format(m))

#frase = str(input('em que cidade voce nasceu? ')).upper().strip()
#print(frase[0:5] == 'Santo'.upper())
#print('seu nome tem silva? {}'.format(frase))
#print('a letra A aparece {} vezes na frase'.format(frase.count('A')))
#print('a primeira letra A apareceu na posicao {}'.format(frase.find('A')+1))
#print('a ultima letra A apareceu na posiçao {}'.format(frase.rfind('A')+1))
#nomes = frase.split()
#print('muito prazer em te conhecer!')
#print('seu primeiro nome e {}'.format(nomes[0]))
#print('seu ultimo nome e {}'.format(nome[len(nomes)-1]))

#nome = str(input('Qual é o seu nome? '))
#if nome == 'Fernando':
 #   print('Caraca.. é vc? ')
#else:
 #   print('Achei que era outra pessoa')
#print('Bom dia, {}!'.format(nome))

#n1 = float(input('Digite a nota do primeiro bimestre: '))
#n2 = float(input('Digite a nota do segundo bimestre: '))
#n3 = float(input('Digite a nota do terceiro bimestre: '))
#n4 = float(input('Digite a nota do quarto bimestre: '))
#m = (n1 + n2 + n3 + n4)/4
#print('A média do ano foi: {:.1f}'.format(m))
#if m >=6.0:
#    print('Bom aproveitamento!, vamos para o próximo ano')
#else: print('Cara tem que reforçar as aulas!, terá que fica de recuperação')
#print('Vc é um nerd' if m>=8.5 else'quase chegou lá hein kkk...')

#from random import randint
#from time import sleep
#computador = randint(0, 9) #Faz o computador "PENSAR"
#print('-=-'* 20)
#print('Vou pensar em um numero entre 0 e 9. Tente adivinhar...')
#print('-=-' * 20)
#jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
#print('PROCESSANDO')
#sleep(2)
#if jogador == computador:
#    print('caraca!!! que é vc..o guru.. kkk')
#else:
    #print('vc precisa entrar no meu processador se quiser ganhar kkk')
   #print('eu pensei no {} e não no {}'.format(computador, jogador))

#velocidade = float(input('Qual a velocidade que vc passou pela rodovia ?'))
#if velocidade > 80:
#    print('Vc ultrapassou o limite de segurança de 80 km/h')
#    mullta = (velocidade-80) * 7
#    print('Vc deve pagar uma multa de R$ {:.2f}!'.format(mullta))
#print('tenha um bom dia, dirija com segurança :')

#a = int(input('informe um numero : '))
#b = int(input('informe um numero : '))
#c = int(input('informe um numero : '))
#verificando que e menor
#menor = a
#if b < a and b < c:
#    menor = b
#if c < a and c < b:
#    menor = c
# verificndo que e o maior valor
#maior = a
#if b > a and b > c:
#    maior = b
#if c > a and c > b:
#    maior = b
#print('o menor valor e {}'.format(menor))
#print('o maior valor e {}'.format(maior))

#salario = float(input('digite seu salario :'))
#if salario <= 1250:
#    novo = salario + (salario * 15/100)
#else:
#    novo = salario + (salario * 10/100)
#
#print('vc ganha {:.2f} reais e vai passar a ganhar {:.2f} reais'.format(salario,novo))
# customizar cores : \033[STYLE, TEXT, BACK m (padrao ANSI que o python melhor se adpta)
# exemplo: \033[0;33;44 m
#style: 0 (none), 1 (bold), 4 (underline), 7 (negativo - innverte configuração)
#text : entre 30 e 37 do branco ao cinza
#back : entre 40 a 47 do braco ao cinza

#print('=-'*20)
#print('analisador de triangulos')
#print('-='*20)
#r1 = float(input('digite lado 01 : '))
#r2 = float(input('digite lado 02 : '))
#r3 = float(input('digite lado 03 : '))
#if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#    print('\033[1;31;43mos segmentos {:.0f}, {:.0f}, {:.0f} podem formar triangulo\033[m'.format(r1, r2, r3))
#else:
#    print('\033[1;37;40mos segmentos {:.0f}, {:.0f}, {:.0f} nao podem formar um triangulo\033[m'.format(r1, r2, r3))
    # exemplo configuração com cores na etapa de impressão .format
    #nome = numero
    #print('o numero {} {} {} podem formar triangulo'.format('\033[4;34m', numero, '\033[m'))
    #outro exemplo
    #nome = 'fernando'
    #cores = {'limpa':'\033[m', 'azul':'\033[34m', 'amarelo':'\033[33m'}
    #print('ola, {}{}{}!!'.format(cores['azul'], nome, cores['limpa']))

#casa = float(input('qual o valor do investimento R$ ? : '))
#salario = float(input('qual o seu salario R$ : '))
#anos = int(input('em quantas prestacao quer pagar R$ ? :'))
#prestacao = casa / (anos * 12)
#minimo = salario * 30/100
#print('para pagar R${:.2f} em {} anos'. format(casa, anos), end='')
#print(' a prestacao sera de R$ {:.2f}'.format(prestacao))
#if prestacao <= minimo:
#    print('emprestimo concedido')
#else:
#    print('emprestimo nao concedido')

#num = int(input('digite um nummero inteiro : '))
#print(''' escolha uma das base para conversao:
#[1] converter para binario
#[2] converter para octal
#[3] converter para hexadecimal''')
#opcao = int(input('sua opcao: '))
#if opcao == 1:
#    print('{} convertido para binario e igual a {}'.format(num, bin(num)[2:]))
#elif opcao == 2:
#    print('{} convertido para octal e igual a {}'.format(num, oct(num)[2:]))
#elif opcao == 3:
#    print('{} convertido para hexadecimal e igual a {}'.format(num, hex(num)[2:]))
#else:
#    print('opcao invalida')

#from datetime import date
#atual = date.today().year
#nasc = int(input('informe o seu ano de nascimento : '))
#idade = atual - nasc
#print('quem nasceu em {}, tem {} anos em {} '. format(nasc, idade, atual))
#if idade == 18:
#    print('vc tem que se alistar imediatamente')
#elif idade < 18:
#    saldo = 18 - idade
#    print('vc ainda nao tem 18 anos, ainda falta {} anos para alistar'.format(saldo))
#    ano = atual + saldo
#    print('seu alistamento sera em {}'.format(ano))
#else:
#    idade > 18
#    saldo = idade - 18
#    print('o alistamento deveria ser a {} anos'.format(saldo))
#    ano = atual - saldo
#    print('seu alistamento foi em {}'.format(ano))

#nota1 = float(input(' digite a primeira nota : '))
#nota2 = float(input('digite a segunda nota : '))
#media = (nota1 + nota2) / 2
#print('tirando {:.1f} e {:.1f}, a media do aluno e {:.1f}'.format(nota1, nota2, media))
#if media >= 5 and media < 7:
#    print('o aluno esta em recuperacao')
#elif media < 5 :
#    print('o aluno esta reprovado')
#else:
#    print('aluno aprovado')


#r1 = float(input('lado 1'))
#r2 = float(input('lado 2'))
#r3 = float(input('lado 3'))
#if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
#    print('os segmentos acima podem formar um triangulo ', end='')
#    if r1 == r2 and r2 == r3: # outra forma somente quando for igual r1 == r2 == r3
#        print('equilatero')
#    elif r1 != r2 and r2!= r3 and r1!=r3: # outra forma r1 != r2 != r3 != r1
#        print('escaleno')
#    else:
#        print('isosceles')
#else:
#    print('os segmentos acima nao pode formar um triangulo')

#peso = float(input('informe o seu peso - kg : '))
#altura = float(input('informe sua altura - m : '))
#imc = peso / (altura ** 2)
#print('o seu imc e : {:.2f}'.format(imc))

#print('{:=^40}'.format(' lojas cem '))
#preco = float(input('preco das compras: R$ '))
#print('''formas de pagamento
#[1] a vista dinheiro/cheque
#[2] a vista cartao
#[3] 02x no cartao
#[4] 03x ou mais cartao''')
#opcao = int(input('qual a opcao? : '))
#if opcao == 1:
#    total = preco - (preco * 10/100)
#    print('o valor fica em : R$ {}'.format(total))
#elif opcao == 2:
#    total = preco - (preco * 5/100)
#    print('o valor fica em : R$ {}'.format(total))
#elif opcao == 3:
#    parcela = preco / 2
#    print('o valor total fica em R$ {}, sendo 02 parcelas de R$ {}'.format(preco,parcela))
#elif opcao == 4:
#    total = preco + (preco * 20/100)
#    print('o preco total ficara em R$ {}'.format(total))
#    parcela = int(input('quantas parcelas deseja fazer? :'))
#    vparcela = total / parcela
#    print('o valor das parcelas sera de R$: {}'.format(vparcela))
#else:
#   print('opcao invalida')


print('{:=^40}'.format(' jogo '))
from random import randint
from time import sleep
itens = ('pedra','papel','tesoura')
computador = randint(0,2)
print('''a opcao :
[0] pedra
[1] papel
[2] tesoura''')
jogador = int(input(' sua jogada : '))
print('pedra')
sleep(1)
print('papel')
sleep(1)
print('tesoura')
sleep(1)
print('-='*11)
print('o computador jogou {} :'.format(itens[computador]))
print('o jogador jogou {} :'.format(itens[jogador]))
print('-='*11)
if computador == 0:
    if jogador == 0:
        print('jogo empate')
    elif jogador == 1:
        print('jogador venceu')
    elif jogador == 2:
        print('computador vence')
    else:
        print('jogo invalido')
elif computador == 1:
    if jogador == 0:
        print('computador vence')
    elif jogador == 1:
        print('jogo empate')
    elif jogador == 2:
        print('jogador vence')
    else:
        print('jogo invalido')
elif computador == 2:
    if jogador == 0:
        print('jogodor vence')
    elif jogador == 1:
        print('computador vence')
    elif jogador == 2:
        print('jogo empate')
    else:
        print('jogo invalido')
else:
    print('jogada inavalida')
