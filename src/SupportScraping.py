# Importación de librerías necesarias para el proyecto

# Automatización de navegadores (Selenium)
# -----------------------------------------------------------------------
from selenium import webdriver                      # Control automático del navegador para scraping web
from selenium.webdriver.chrome.service import Service  # Manejo del servicio de ChromeDriver
from selenium.webdriver.common.by import By         # Selección de elementos en el DOM
from selenium.webdriver.chrome.options import Options  # Configuración de opciones de navegador (headless mode, etc.)
import time                                         # Para gestionar pausas y temporización

# Extracción de datos y scraping
# -----------------------------------------------------------------------
from bs4 import BeautifulSoup                       # Análisis y extracción de datos de HTML y XML (scraping web)
import requests                                     # Manejo de solicitudes HTTP para obtener datos de la web

# Visualización de progreso
# -----------------------------------------------------------------------
from tqdm import tqdm                               # Creación de barras de progreso durante bucles

# Tratamiento y manipulación de datos
# -----------------------------------------------------------------------
import pandas as pd                                 # Manipulación de estructuras de datos como DataFrames
import numpy as np                                  # Cálculos numéricos y manejo de arrays
import datetime                                     # Manipulación de fechas y tiempos

# Manejo de tiempo y solicitudes con espera
# -----------------------------------------------------------------------
from time import sleep                              # Pausas en la ejecución del código
import random                                       # Generación de valores aleatorios, útil para espaciar solicitudes y evitar bloqueos


def obtener_url_supermercados(xpath):
    """
    Obtiene la URL de una página de supermercados de FACUA tras interactuar con elementos de la interfaz.

    Args:
        xpath (str): Cadena con el XPATH del elemento a hacer clic, una vez que la página ha sido cargada.

    Returns:
        str: URL de la página actual después de hacer clic en el elemento especificado.

    Example:
        >>> xpath = '//*[@id="elemento_supermercado"]'
        >>> url = obtener_url_supermercados(xpath)
        >>> print(url)
        
    Notes:
        - Requiere tener instalado y configurado Selenium junto con el driver de Chrome.
        - La ventana se maximiza y se realiza un scroll antes de hacer clic en el elemento.
        - Asegúrate de ejecutar esta función una sola vez para evitar múltiples instancias del navegador.
    """
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
    """
    Obtiene una lista de URLs de productos por supermercado desde la página de FACUA, navegando e interactuando
    con elementos específicos de la interfaz para cada categoría de productos.

    Args:
        url (str): URL inicial de la página del supermercado en FACUA desde donde se obtendrán las URLs de productos.

    Returns:
        list of str: Lista de URLs correspondientes a diferentes categorías de productos en el supermercado.

    Example:
        >>> url = "https://super.facua.org/supermercado"
        >>> urls_productos = obtener_url_productos_por_supermercado(url)
        >>> print(urls_productos)
        
    Notes:
        - Requiere tener instalado y configurado Selenium junto con el driver de Chrome.
        - La función realiza varias interacciones en la página, incluyendo clics, desplazamiento y navegaciones hacia atrás.
        - Cada URL obtenida representa una categoría de productos en el supermercado especificado.
    """
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
    """
    Obtiene una lista de URLs correspondientes a distintas categorías de productos en tres páginas de supermercados, 
    y devuelve un DataFrame con el nombre del supermercado y las URLs obtenidas.

    Args:
        url1 (str): URL de la primera página del supermercado.
        url2 (str): URL de la segunda página del supermercado.
        url3 (str): URL de la tercera página del supermercado.

    Returns:
        pandas.DataFrame: DataFrame que contiene dos columnas:
                          - "supermercado": Nombre del supermercado, extraído de la primera URL.
                          - "URL": Lista de URLs correspondientes a cada categoría de productos en las páginas.

    Example:
        >>> url1 = "https://super.facua.org/supermercado1"
        >>> url2 = "https://super.facua.org/supermercado2"
        >>> url3 = "https://super.facua.org/supermercado3"
        >>> df_urls = obtener_urls_por_super_producto_y_categoria(url1, url2, url3)
        >>> print(df_urls)
        
    Notes:
        - Requiere tener instalado y configurado Selenium junto con el driver de Chrome.
        - La función realiza varias interacciones en las páginas, incluyendo clics, desplazamiento y navegación.
        - La ventana del navegador se maximiza y se ejecuta un desplazamiento hacia abajo en cada página para alcanzar elementos interactivos.
    """
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
    """
    Extrae enlaces y nombres de productos desde la página de un supermercado en FACUA y los organiza en un DataFrame.

    Args:
        url (str): URL de la página del supermercado en FACUA, de la cual se extraerán los datos de productos.

    Returns:
        pandas.DataFrame: DataFrame con las siguientes columnas:
                          - "supermercado": Nombre del supermercado, extraído de la URL.
                          - "categoria": Categoría de productos, extraída de la URL.
                          - "Producto": Nombre del producto extraído de la página.
                          - "URL": Enlace al producto correspondiente.

    Example:
        >>> url = "https://super.facua.org/supermercado/categoria/productos"
        >>> df_productos = obtener_href(url)
        >>> print(df_productos)
        
    Notes:
        - Requiere las librerías `requests` y `BeautifulSoup` para obtener y analizar el contenido de la página.
        - La función configura encabezados para la solicitud, simulando un navegador Chrome y estableciendo el idioma en español.
        - Los nombres y URLs de los productos se extraen basándose en etiquetas HTML específicas y clases de la página de FACUA.
    """
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
    """
    Obtiene una lista de DataFrames con información de productos desde múltiples URLs de supermercados.

    Args:
        df_super (pandas.DataFrame): DataFrame que contiene una columna "URL" con enlaces a páginas de supermercados en FACUA.

    Returns:
        list of pandas.DataFrame: Lista de DataFrames, donde cada DataFrame contiene información de productos 
                                  (supermercado, categoría, nombre de producto, y URL) extraída de cada URL en `df_super`.

    Example:
        >>> df_super = pd.DataFrame({"URL": ["https://super.facua.org/super1", "https://super.facua.org/super2"]})
        >>> lista_dfs = obtener_href_productos(df_super)
        >>> for df in lista_dfs:
        >>>     print(df.head())
        
    Notes:
        - Requiere la función `obtener_href` para extraer información de productos de cada URL.
        - Cada URL en `df_super` es procesada y se obtiene un DataFrame con información de productos de esa página.
    """
    lista_urls = df_super["URL"].to_list()
    lista_dfs = [obtener_href(url) for url in lista_urls]
    return lista_dfs

def crear_df_rn(supermercado,categoria,producto,url):
    """
    Extrae información histórica de precios de productos desde una página de FACUA y organiza los datos en un DataFrame.

    Args:
        supermercado (str): Nombre del supermercado.
        categoria (str): Categoría del producto.
        producto (str): Nombre del producto.
        url (str): URL de la página donde se encuentran los datos históricos de precios del producto.

    Returns:
        pandas.DataFrame: DataFrame con columnas para supermercado, categoría, producto, fecha, precio y variación de precio.

    Example:
        >>> df_historico = crear_df_rn("Super1", "Lácteos", "Leche", "https://super.facua.org/producto1")
        >>> print(df_historico.head())

    Notes:
        - Requiere las librerías `requests` y `BeautifulSoup` para obtener y analizar el contenido de la página.
        - La función extrae las columnas directamente desde la tabla en la página, por lo que es importante que la estructura de la página no cambie.
    """
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
    """
    Crea una lista de DataFrames con datos históricos de precios de productos, utilizando la información de un DataFrame de entrada.

    Args:
        df_que_entra (pandas.DataFrame): DataFrame que contiene las columnas "supermercado", "categoria", "Producto" y "URL",
                                         con la información necesaria para extraer los datos de precios históricos.

    Returns:
        list of pandas.DataFrame: Lista de DataFrames, donde cada DataFrame contiene los datos históricos de precios de un producto,
                                  incluyendo supermercado, categoría, producto, fecha, precio y variación.

    Example:
        >>> df_productos = pd.DataFrame({
                "supermercado": ["Super1", "Super2"],
                "categoria": ["Lácteos", "Cereales"],
                "Producto": ["Leche", "Cereal"],
                "URL": ["https://super.facua.org/producto1", "https://super.facua.org/producto2"]
            })
        >>> historicos = crear_df_productos_con_historico(df_productos)
        >>> for df in historicos:
        >>>     print(df.head())

    Notes:
        - Utiliza `crear_df_rn` para extraer datos históricos desde cada URL en `df_que_entra`.
        - La función requiere `tqdm` para mostrar una barra de progreso durante el procesamiento de múltiples URLs.
    """
    lista_supermercado = df_que_entra["supermercado"].to_list()
    lista_categoria = df_que_entra["categoria"].to_list()
    lista_productos = df_que_entra["Producto"].to_list()
    lista_urls = df_que_entra["URL"].to_list()
    
    dfs_results = [crear_df_rn(lista_supermercado[i],lista_categoria[i],lista_productos[i],lista_urls[i]) for i, x in tqdm(enumerate(lista_urls))]
    return dfs_results


