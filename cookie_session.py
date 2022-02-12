from importlib.resources import path
import time 
import requests
import json


encabezado = {'Host': 'www.padron.gob.ar',
'Origin': 'https://www.padron.gob.ar',
'Referer': 'https://www.padron.gob.ar/publica/',
'Connection': 'keep-alive',
"sec-ch-ua": "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"98\", \"Chromium\";v=\"98\"",
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'}

session = requests.Session()

#response = session.get('https://www.padron.gob.ar/publica/armasite.php')

#print(response.headers)
print("-------------------------------")
time.sleep(5)

payload = json.dumps({'zona' : '0001' , 'codigo' : '1', 'tipo' : '1'})
print("-------------------------------")

print("payload "+payload)
print("-------------------------------")
resp = session.post('https://www.padron.gob.ar/publica/mesasres.php', data=payload, headers=encabezado)
print("HEADERS ENVIADOS: "+str(resp.request.headers))
print("-------------------------------")
print("RESPUESTA: "+resp.text)



