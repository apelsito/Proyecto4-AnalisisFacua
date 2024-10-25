# Importamos las librerías que necesitamos

# Librerías para automatización de navegadores (Selenium)
# -----------------------------------------------------------------------
from selenium import webdriver                   # Control automático del navegador para realizar scraping web

from selenium.webdriver.chrome.service import Service  # Maneja el servicio de ChromeDriver
from selenium.webdriver.common.by import By      # Para seleccionar elementos en la página web (DOM)
from selenium.webdriver.chrome.options import Options  # Configuración de opciones del navegador (headless mode, etc.)
import time                                      # Para gestionar pausas y temporización

# Librerías para extracción de datos y scraping
# -----------------------------------------------------------------------
from bs4 import BeautifulSoup  # Para analizar y extraer datos de HTML y XML (scraping web)

# Librerías para tratamiento y manipulación de datos
# -----------------------------------------------------------------------
import pandas as pd             # Para manipulación de estructuras de datos como DataFrames
import numpy as np              # Para cálculos numéricos y manejo de arrays
import datetime                 # Para manipulación de fechas y tiempos

# Manejo del tiempo y generación de pausas
# -----------------------------------------------------------------------
from time import sleep          # Pausar la ejecución del código durante un tiempo definido


def obtener_url_supermercados(xpath):
    
    driver = webdriver.Chrome() #Para Abrir chrome solo ejecutar once
    url_facua= "https://super.facua.org/"
    driver.get(url_facua)
    #Maximizar ventana
    driver.maximize_window() 
    sleep(1)
    driver.find_element('xpath','/html/body/div/div[2]/button[2]').click()
    sleep(1)
    driver.execute_script("window.scrollTo(0, 100)")
    sleep(1)
    driver.find_element('xpath',xpath).click()
    sleep(1)
    url_obtenida = driver.current_url
    driver.quit()
    return url_obtenida

def obtener_url_productos_por_supermercado(url):
    urls = []
    driver = webdriver.Chrome() #Para Abrir chrome solo ejecutar once
    driver.get(url)
    #Maximizar ventana
    driver.maximize_window() 
    sleep(1)
    driver.find_element('xpath','/html/body/div/div[2]/button[2]').click()
    sleep(1)
    driver.execute_script("window.scrollTo(0, 100)")
    sleep(1)
    driver.find_element('xpath',"/html/body/section[1]/div/div[2]/div[1]/div/div[2]/div").click()
    sleep(1)
    url_obtenida = driver.current_url
    urls.append(url_obtenida)
    sleep(1)
    driver.back()
    sleep(2)
    driver.execute_script("window.scrollTo(0, 100)")
    sleep(1)
    driver.find_element('xpath',"/html/body/section[1]/div/div[2]/div[2]/div/div[2]/div").click()
    url_obtenida = driver.current_url
    urls.append(url_obtenida)
    sleep(1)
    driver.back()
    sleep(2)
    driver.execute_script("window.scrollTo(0, 100)")
    sleep(1)
    driver.find_element('xpath',"/html/body/section[1]/div/div[2]/div[3]/div/div[2]/div").click()
    url_obtenida = driver.current_url
    urls.append(url_obtenida)
    sleep(1)
    driver.quit()
    return urls
