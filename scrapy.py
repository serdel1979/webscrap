from cgitb import html
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import pandas as pd
import csv
# Armo la lista de secciones
secciones = []
for i in range(137):
    val = ("0000"+str(i+1))[-5:]
    secciones.append(val)
secciones.append("00998")
secciones.append("00999")


options = webdriver.ChromeOptions()
options.add_argument('--disable-extensions')
options.headless = True

driver = webdriver.Chrome(chrome_options=options)

driver.get('https://www.padron.gob.ar/publica/') # <-- poner en el catch
time.sleep(1)

select = Select(driver.find_element_by_id('site'))
select.select_by_visible_text('BUENOS AIRES')

time.sleep(1)
for i in secciones:
    select = Select(driver.find_element_by_id('secm'))
    select.select_by_value(i)
    print("------------->", select)
    
    time.sleep(1)

    hayMesa = True
    numMesa = 1

    while hayMesa:
        input = driver.find_element_by_id('mesa')
        input.clear()
        input.send_keys(str(numMesa))

        time.sleep(1)
        btn = driver.find_element_by_id('btnVer')
        btn.click()

        time.sleep(1)
        try:
            btn = driver.find_element_by_id('btnVolver')
            btn.click()
            numMesa = numMesa + 1
            time.sleep(1)
        except:
            #Si falla es porque se terminaron las mesas
            hayMesa = False
            driver.get('https://www.padron.gob.ar/publica/') 
            time.sleep(1)
            select = Select(driver.find_element_by_id('site'))
            select.select_by_visible_text('BUENOS AIRES')
            time.sleep(1)



# Hasta acá va el while de mesas

# Ahora con los resultados armar el archivo

soup = BeautifulSoup(driver.page_source,'html.parser')
try:
    table = soup.find_all("table", {"class": "tbl table table-striped table-bordered table-hover"})
except:
    print("No hay resultados")

rows = table[0].find_all("tr")

csvFile = open("./mesa.csv", 'wt', newline='', encoding='utf-8')
writer = csv.writer(csvFile)

try:
    for row in rows:
        csvRow = []
        for cell in row.find_all(['td','th']):
            el = cell.get_text().strip("\"").lstrip().rstrip()
            csvRow.append(el)
        writer.writerow(csvRow)
  
finally:
    csvFile.close()