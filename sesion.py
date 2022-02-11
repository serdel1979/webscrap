import time
import requests

param1 = {'zona':'0080', 'codigo':'3', 'tipo':'1'}
param_buscabase = {'site' : '18'}
param_armaelec = {'site' : '18'}
param_armasecc = {'site' : '18', 'zona' : 't_secc'}
param_buscaelecc = {'site' : '18', 'orden' : '0'}

s = requests.Session()

r = s.get('https://www.padron.gob.ar/publica/armasite.php')
print(r)

time.sleep(5)

url = "https://www.padron.gob.ar/publica/mesasres.php"
r = s.post(url, data=param1)

print(r)