import requests
import json

url = "https://www.padron.gob.ar/publica/mesasres.php"

param1 = json.dumps({'zona':'0080', 'codigo':'3', 'tipo':'1'})

headers = {
  'Content-Type': 'application/json',
  'Cookie': 'cookiesession1=678A3E0DCDEFGHIJKLNOPQRSTUV08936'
}

response = requests.request("POST", url, headers=headers, data=param1)

print(response.text)

print(response.status_code)