n1 = int(input('digite um valor :'))
n2 = int(input('digite outro :'))
s = n1 + n2
# print('a soma entre', n1, ' e ',n2, ' vale ', s)

print('a soma entre {} e {} vale {}'.format(n1, n2, s))

n3 = float(input('digite um valor :'))
print(n3)
print(type(n3))

n4 = bool(input('digite um valor : '))
print(n4)

n5 = input('digite algo :')
print(n5.isnumeric())

n6 = input('digite algo : ')
print(n6.isalpha())

n7 = input('digite algo :')
print('o tipo primitivo desse valor é ', type(n7))
print('só tem espaços?', n7.isspace())
print('é um numero?', n7.isnumeric())
print('é alfabético?', n7.isalpha())
print('é alfanumérico?', n7.isalpha())
print('esta em maiuscula?', n7.isupper())
print('esta em minuscula', n7.islower())
print('esta capitalizada?', n7.istitle())