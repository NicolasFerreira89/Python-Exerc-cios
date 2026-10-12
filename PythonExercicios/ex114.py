import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://pudim.com.br')
except:
    print('ERRO')
else:
    print('OK')
    print(site.read())