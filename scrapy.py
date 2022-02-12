from cgitb import html
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver = webdriver.Chrome(chrome_options=options)

driver.get('https://www.padron.gob.ar/publica/')

time.sleep(3)

select = Select(driver.find_element_by_id('site'))
select.select_by_visible_text('BUENOS AIRES')

time.sleep(3)

select = Select(driver.find_element_by_id('elec'))
select.select_by_value(str(3))

time.sleep(3)

select = Select(driver.find_element_by_id('secm'))
select.select_by_value("00003")

time.sleep(3)

input = driver.find_element_by_id('mesa')
input.send_keys('1')

time.sleep(3)

btn = driver.find_element_by_id('btnVer')
btn.click()

time.sleep(3)
# Ahora con los resultados que se tienen hacer scraping

#tabla = driver.find_elements_by_tag_name('table')

tabla = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[1]/div/div/div[2]/table')

#"tbl table table-striped table-bordered table-hover"
# obtener todas las filas de la tabla

#print(tabla)

#/html/body/div/div[2]/div/div/div[1]/div/div/div[2]/table/thead/tr


#for row in rows:
#    col = row.find_elements_by_tag_name('td')[1] 
#    print(col.text) 

