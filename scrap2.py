import time
import requests

params = {'zona':'0080', 'codigo':'3', 'tipo':'1'}
response = requests.get('https://www.padron.gob.ar/publica/armasite.php', headers={'User-Agent': 'Mozilla/5.0'})
cookies = response.cookies

print(response.headers)
print(" ")
print("---------------------------------------")
print(" ")

time.sleep(5)

url = "https://www.padron.gob.ar/publica/mesasres.php"
r = requests.post(url, headers={'User-Agent': 'Mozilla/5.0'}, cookies=cookies, params=params)

print(r.headers)