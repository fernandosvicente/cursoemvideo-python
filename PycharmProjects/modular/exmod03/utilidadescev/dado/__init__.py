def leiadinheiro(msg):
    valido = False
    while not valido:
            entrada = str(input(msg)).replace(',','.').strip()
            if entrada.isalpha():
                print(f'\033[0;31mERRO: \"{entrada}\" é invalido, digite um numero\033[m')
            elif entrada == '':
                print(f'\033[0;31mERRO: \"{entrada}\" o campo esta vazio, digite um numero\033[m')
            else:
                valido = True
                return float(entrada)
