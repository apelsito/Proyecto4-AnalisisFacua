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

# -----------------------------------------------------------------------
# Librerías para visualización de progreso
# -----------------------------------------------------------------------
from tqdm import tqdm  # Para crear barras de progreso durante los bucles

# Librerías para tratamiento y manipulación de datos
# -----------------------------------------------------------------------
import pandas as pd             # Para manipulación de estructuras de datos como DataFrames
import numpy as np              # Para cálculos numéricos y manejo de arrays
import datetime                 # Para manipulación de fechas y tiempos

# Manejo de tiempo y solicitudes con espera
# -----------------------------------------------------------------------
from time import sleep          # Para pausar la ejecución del código por un tiempo determinado
import random                   # Para generar valores aleatorios, útil para espaciar solicitudes y evitar bloqueos
import requests                 # Repetido (puedes eliminar este segundo import de requests)


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


def obtener_urls_por_super_producto_y_categoria(url1,url2,url3):
    urls = []
    supermercado = url1.split("/")[3]
    driver = webdriver.Chrome() #Para Abrir chrome solo ejecutar once
    driver.get(url1)
    #Maximizar ventana
    driver.maximize_window() 
    sleep(1)
    driver.find_element('xpath','/html/body/div/div[2]/button[2]').click() #Cookie time
    sleep(1)
    url_obtenida = driver.current_url
    urls.append(url_obtenida)
    sleep(1)
    driver.quit()
    sleep(1)

    driver = webdriver.Chrome()
    driver.get(url2)
    #Maximizar ventana
    driver.maximize_window() 
    sleep(1)
    driver.find_element('xpath','/html/body/div/div[2]/button[2]').click() #Cookie time
    sleep(1)
    driver.execute_script("window.scrollTo(0, 100)")
    sleep(1)
    driver.find_element('xpath',"/html/body/section[1]/div/div[2]/div[1]/div/div[2]/div").click()
    sleep(1)
    url_obtenida = driver.current_url
    urls.append(url_obtenida)
    sleep(1)
    driver.back()
    sleep(1)
    driver.find_element('xpath',"/html/body/section[1]/div/div[2]/div[2]/div/div[2]/div").click()
    sleep(1)
    url_obtenida = driver.current_url
    urls.append(url_obtenida)
    sleep(1)
    driver.back()
    sleep(1)
    driver.find_element('xpath',"/html/body/section[1]/div/div[2]/div[3]/div/div[2]/div").click()
    sleep(1)
    url_obtenida = driver.current_url
    urls.append(url_obtenida)
    sleep(1)
    driver.quit()
    sleep(1)

    driver = webdriver.Chrome()
    driver.get(url3)
    #Maximizar ventana
    driver.maximize_window() 
    sleep(1)
    driver.find_element('xpath','/html/body/div/div[2]/button[2]').click() #Cookie time
    sleep(1)
    driver.execute_script("window.scrollTo(0, 100)")
    sleep(1)
    driver.find_element('xpath',"/html/body/section[1]/div/div[2]/div[1]/div/div[2]/div").click()
    sleep(1)
    url_obtenida = driver.current_url
    urls.append(url_obtenida)
    sleep(1)
    driver.back()
    sleep(1)
    driver.find_element('xpath',"/html/body/section[1]/div/div[2]/div[2]/div/div[2]/div").click()
    sleep(1)
    url_obtenida = driver.current_url
    urls.append(url_obtenida)
    sleep(1)
    driver.back()
    sleep(1)
    driver.find_element('xpath',"/html/body/section[1]/div/div[2]/div[3]/div/div[2]/div").click()
    sleep(1)
    url_obtenida = driver.current_url
    urls.append(url_obtenida)
    sleep(1)
    driver.quit()
    sleep(1)
    supermarket = []
    for i in range(0,len(urls)):
        supermarket.append(supermercado)

    df = pd.DataFrame({
        "supermercado" : supermarket,
        "URL" : urls

    })
    return df

def obtener_href(url):
    headers = {
            # Decirle al server lenguaje español
            'accept-language': 'es', 
            # Simulamos que somos el navegador Chrome
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
            }
    url_facua= url

    res_facua = requests.get(url_facua,headers=headers,timeout=5)
    sopa= BeautifulSoup(res_facua.content, "html.parser")
    n_productos = sopa.find_all("div",{"class":"card-footer p-4 pt-0 border-top-0 bg-transparent"})
    nombres = sopa.find_all("p",{"class":"fw-bolder"})
    df_productos = []
    supermercado = []
    supermer = url_facua.split("/")[3]
    categoria = []
    categ = url_facua.split("/")[4] + "-"+url_facua.split("/")[5]
    urls_productos = []
    nombres_productos = []
    for i in range(0,len(n_productos)):
        supermercado.append(supermer)
        categoria.append(categ)
        producto = nombres[i].getText()
        nombres_productos.append(producto)
        url = n_productos[i].find("a").get('href')
        urls_productos.append(url)

    df = pd.DataFrame({
    "supermercado" : supermercado,
    "categoria" : categoria,
    "Producto": nombres_productos,
    "URL": urls_productos
    })
    return df

def obtener_href_productos(df_super):
    lista_urls = df_super["URL"].to_list()
    lista_dfs = [obtener_href(url) for url in lista_urls]
    return lista_dfs

def crear_df_rn(supermercado,categoria,producto,url):
    headers = {
                # Decirle al server lenguaje español
                'accept-language': 'es', 
                # Simulamos que somos el navegador Chrome
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
                }
    res_facua = requests.get(url,headers=headers,timeout=5)
    sopa= BeautifulSoup(res_facua.content, "html.parser")
    search = sopa.find_all("table",{"class":"table table-striped table-responsive text-center"})
    cols = search[0].find_all("th")
    columnas = [] 
    for c in range(0,len(cols)):
        columnas.append(cols[c].getText())
    body = search[0].find_all('tbody')[0].find_all('tr')
    dias = []
    precios = []
    variaciones = []
    for i in range(0,len(body)):
        row = body[i].find_all('td')
        dia = row[0].getText()
        dias.append(dia)
        precio = row[1].getText().replace(",",".")
        precios.append(precio)
        variacion = row[2].getText()
        variaciones.append(variacion)
  
    supermercados = [supermercado] * len(dias)
    categorias = [categoria] * len(dias)
    productos = [producto] * len(dias)

    df_result = pd.DataFrame({
        "supermercado" : supermercados,
        "categoria" : categorias,
        "producto" : productos,
        columnas[0] : dias,
        columnas[1] : precios,
        columnas[2] : variaciones
    })
    return df_result

def crear_df_productos_con_historico(df_que_entra):
    lista_supermercado = df_que_entra["supermercado"].to_list()
    lista_categoria = df_que_entra["categoria"].to_list()
    lista_productos = df_que_entra["Producto"].to_list()
    lista_urls = df_que_entra["URL"].to_list()
    
    dfs_results = [crear_df_rn(lista_supermercado[i],lista_categoria[i],lista_productos[i],lista_urls[i]) for i, x in tqdm(enumerate(lista_urls))]
    return dfs_results