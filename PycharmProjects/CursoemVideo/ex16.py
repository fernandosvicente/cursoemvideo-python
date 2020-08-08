#aluno = dict()
#aluno['nome'] = str(input('nome: '))
#aluno['media'] = float(input(f'media de {aluno["nome"]} :'))
#if aluno['media'] >= 7:
#    aluno['situacao'] = 'aprovado'
#elif 5 <= aluno['media'] <7:
#    aluno['situacao'] = 'recuperacao'
#else:
#    aluno['situacao'] = 'reprovado'
#print('=-' * 30)
#for k, v in aluno.items():
#    print(f'  - {k} e igual a {v}')



#from random import randint
#from time import sleep
#from operator import itemgetter
#jogo = {'jogador1':randint(1, 6),
#        'jogador2':randint(1, 6),
#        'jogador3':randint(1, 6),
#        'jogador4':randint(1, 6)}
#ranking = list()
#print('valores sorteados: ')
#for k, v in jogo.items():
#    print(f'{k} tirou {v} no dado.')
#    sleep(1)
#ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
#print(ranking)
#for i, v in enumerate(ranking):
#    print((f'{i+1} lugar: {v[0]} com {v[1]}.'))
#    sleep(1)



#from datetime import datetime
#dados = dict()
#dados['nome']= str(input('nome: '))
#nasc = int(input('ano de nascimento: '))
#dados['idade'] = datetime.now().year - nasc
#dados['ctps'] = int(input('digite o ctps (0 nt): '))
#if dados['ctps'] != 0:
#    dados['contrato'] = int(input('ano de contrato: '))
#    dados['salario'] = float(input('seu ultimo salario: '))
#    dados['aposent'] = dados['idade'] + ((dados['contrato'] + 35) - datetime.now().year)
#print('-=-' * 20)
#for k, v in dados.items():
#    print(f' - {k} tem o valor {v}')



time = list()
jogador = dict()
partida = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('nome jogador: '))
    tot = int(input(f'quantas partidas {jogador["nome"]} fez? '))
    partida.clear()
    for c in range(0, tot):
        partida.append(int(input(f'quantos gols na partida {c}')))
    jogador['gols'] = partida[:]
    jogador['total'] = sum(partida)
    time.append(jogador.copy())
    print('=-=' * 20)
    print(jogador)
    print('=-=' * 20)
    for k, v in jogador.items():
        print(f'o campo {k} tem o valor {v}')
    while True:
        resp = str(input('quer continuar [S/N]?: ')).upper()[0]
        if resp in 'SN':
            break
        print('erro, favor digitar "s" para sim e "n" para nao')
    if resp == 'N':
        break
print('=-=' * 20)
print('cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end=' ')
print()
for k, v in enumerate(time):
    print(f'{k:>3} ', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
print('=-=' * 20)
while True:
    busca = int(input('mostrar dados de qual jogador? 999 para parar: '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'erro, nao existe jogadores com esse codigo {busca} ')
    else:
        print(f'------ dados solicitados jogador {time[busca]["nome"]} :')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i} fez {g} gols')
    print('=-=' * 20)
print('pedsquisa concluida')



#galera = list()
#pessoa = dict()
#soma = media = 0
#while True:
#    pessoa.clear()
#    pessoa['nome'] = str(input('nome: '))
#    while True:
#        pessoa['sexo'] = str(input('sexo [M/F]: ')).upper()[0]
#        if pessoa['sexo'] in 'MF':
#            break
#        print('erro! por favor, digite apenas M ou F')
#    pessoa['idade'] = int(input('idade: '))
#    soma += pessoa['idade']
#    galera.append(pessoa.copy())
#    while True:
#        resp = str(input('quer continuar [S/N]? ')).upper()[0]
#        if resp in 'SN':
#            break
#        print('erro! por favor, digite apenas S ou N')
#    if resp == 'N':
#        break
#print('=-=' * 30)
#print(f'ao todo foram {len(galera)} pessoa cadastradas')
#media = soma/len(galera)
#print(f'a media de idade e de {media:5.2f} anos')
#print(f'as mulheres cadastradas foram ', end='')
#for p in galera:
#    if p['sexo'] == 'F':
#        print(f'{p["nome"]} ', end='')
#print()
#print(f'lista das pessoas acima da media: ', end='')
#for p in galera:
#    if p['idade'] >= media:
#        print('   ')
#        for k, v in p.items():
#            print(f'{k} = {v}: ', end='')
#        print()
#print('<<<ENCERRADO>>>')