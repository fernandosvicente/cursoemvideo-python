'''
print('Consulta online')
pergunta = input('Cadastro de carros para compra?: [S/N] ').upper()

if pergunta == 'S':
    carro = list()
    carro.append(input('Me informe qual modelo de carro: '))
    cont = input('quer continuar?: [S/N] ').upper()
    while cont == 'S':
        carro.append(input('Me informe qual modelo de carro: '))
        cont = input('quer continuar?: [S/N] ').upper()
    for m in carro:
        print(f'o modelo informado foi: {m}')
else:
    print('Agradeço pelo tempo e..Bom dia')
'''

'''
USO DE INSTRUÇÃO DECISÃO E O ARGUMENTO 'IN'
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car =='bmw':
        print(car.upper())
    else:
        print(car.title())
'''

'''USO DO AGURMENTO NOT IN

usuario = ['andre', 'carolina', 'david']
user = 'andre'

if user not in usuario:
    print(f'o usuario {user} não existe na lista')
else:
    print(f'o usuario {user} já esta na lista')
'''

aliens = []

for alien in range(30):
    novoAlien = {'color': 'verde', 'points': 5, 'speed': 'slow'}
    aliens.append(novoAlien)

print('*'*50)
for alien in aliens[0:3]:
    if alien['color'] == 'verde':
        alien['color'] = 'amarelo'
        alien['points'] = 10
        alien['speed'] = 'medium'

for alien in aliens[:5]:
    print(alien)
print('*'*50)
print(f'foram criados {len(aliens)} aliens na lista')


