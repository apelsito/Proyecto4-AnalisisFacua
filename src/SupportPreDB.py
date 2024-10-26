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
# -----------------------------------------------------------------------
# Librerías para visualización de progreso
# -----------------------------------------------------------------------
from tqdm import tqdm  # Para crear barras de progreso durante los bucles

# Manejo de tiempo y solicitudes con espera
# -----------------------------------------------------------------------
from time import sleep          # Para pausar la ejecución del código por un tiempo determinado
import random                   # Para generar valores aleatorios, útil para espaciar solicitudes y evitar bloqueos


def crear_df_unicos(df, nombre_columna):
    columna = nombre_columna
    lista_unicos = df[columna].unique().tolist()
    df_unicos = pd.DataFrame({
                    columna : lista_unicos
                    })
    df_unicos.index = pd.RangeIndex(start=1,
                                    stop = len(df_unicos) + 1,
                                    step=1)
    
    df_unicos.reset_index(inplace=True)
    
    return df_unicos

def crear_dictio(df,columna):
    dictio = {}
    datos = df.groupby(columna)["index"].first()
    indices = list(datos.index)
    valores = list(datos.values)
    for i in range(0, len(indices)):
        dictio[indices[i]] = valores[i] 
    
    return dictio

def crear_df_historico(df_historicos,df_supermercado,df_categoria,df_producto):
    # Creamos los diccionarios
    dictio_supermercados = crear_dictio(df_supermercado,"supermercado")
    dictio_categorias = crear_dictio(df_categoria,"categoria")
    dictio_productos = crear_dictio(df_producto,"producto")
    
    #Ponemos cada valor según cada uno de los diccionarios
    df_historicos["supermercado"] = df_historicos["supermercado"].map(dictio_supermercados)
    df_historicos["categoria"] = df_historicos["categoria"].map(dictio_categorias)
    df_historicos["producto"] = df_historicos["producto"].map(dictio_productos)

    return df_historicos