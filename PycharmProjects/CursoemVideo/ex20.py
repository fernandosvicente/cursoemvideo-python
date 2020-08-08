import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('o site Pudim nao esta acessivel no momento')
else:
    print('aceeso realizado com sucesso')
