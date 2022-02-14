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
import sys


#procesamiento de parámetros

#print("Número de parámetros: ", len(sys.argv))
#print("Lista de argumentos: ", sys.argv)
#print(type(sys.argv[1]))
#print(type(sys.argv[2]))
#print(type(sys.argv[3]))


options = webdriver.ChromeOptions()
options.add_argument('--disable-extensions')
#options.headless = True

driver = webdriver.Chrome(chrome_options=options)

driver.get('https://www.padron.gob.ar/publica/')
time.sleep(1)

select = Select(driver.find_element_by_id('site'))
select.select_by_visible_text('BUENOS AIRES')

time.sleep(1)
# elecciones = True
# while elecciones
select = Select(driver.find_element_by_id('elec'))
select.select_by_value('1')

time.sleep(1)

try:
    select = Select(driver.find_element_by_id('secm'))
    select.select_by_value("00001")
except:
    print("No se requiere sección")



time.sleep(1)

input = driver.find_element_by_id('mesa')
input.send_keys('1')

time.sleep(1)

btn = driver.find_element_by_id('btnVer')
btn.click()

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