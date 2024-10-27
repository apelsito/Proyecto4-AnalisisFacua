# 🛒 Análisis de Precios de Supermercados 📊

Este proyecto tiene como objetivo recopilar, procesar y analizar datos de precios de productos en distintos supermercados de España, con el fin de comparar precios, estudiar la evolución de precios a lo largo del tiempo y detectar posibles anomalías. La información recolectada permite visualizar la dispersión de precios entre supermercados y ofrece una base de datos sólida para futuras investigaciones de tendencias de precios.

## Descripción del Proyecto 💡

El proyecto se centra en la recolección de datos de precios de productos de la página [FACUA](https://super.facua.org/): Precios Supermercados mediante técnicas de web scraping. Los datos obtenidos se almacenan en una base de datos SQL y se analizan usando Python y Pandas. Entre los principales componentes de este proyecto se encuentran:

- **Comparación de precios**: Analizamos las diferencias de precios entre supermercados para identificar los más competitivos.
- **Evolución de precios**: Estudiamos cómo han cambiado los precios de distintos productos a lo largo del tiempo.
- **Detección de anomalías**: Identificamos cambios significativos en los precios para señalar anomalías o patrones inesperados.
- **Visualización de datos**: Creamos gráficos interactivos usando Plotly Express para facilitar la interpretación de los resultados.

## Estructura del Proyecto 🗂️

```bash
Proyecto4-AnalisisFacua/
├── datos/                   # Tablas con la información de SQL.
│   ├── 01_backups/          # Backups de webscraping para no tener que rehacerlos.
│   ├── 02_consultas_sql/    # Tablas de las consultas realizadas en SQL.
│
├── notebooks/               # Notebooks de jupyter con el análisis y las visualizaciones.
├── src/                     # Archivos .py para las funciones utilizadas por el proyecto
│    ├── 01_png/             # Fotos de evidencias sobre hallazgos.
│    ├── 02_graficas/        
│    │    ├── html/          # Gráficas interactivas en HTML.  
│    │    ├── png/           # Fotos de las mismas gráficas.
│
└── README.md            # Descripción del proyecto, lo estás leyendo!
```


## Instalación y Requisitos 🛠️
### Requisitos

Para ejecutar este proyecto, asegúrate de tener instalado lo siguiente:

- **Python 3.x** 🐍
- **Jupyter Notebook** 📓 para ejecutar y visualizar los análisis de datos
- **Bibliotecas de Python**:
    - [pandas](https://pandas.pydata.org/docs/) para manipulación de datos 🧹
    - [numpy](https://numpy.org/doc/2.1/) para cálculos numéricos 🔢
    - [plotly.express](https://plotly.com/python/plotly-express/) para visualización de datos interactiva 📊
    - [requests](https://requests.readthedocs.io/en/latest/) para conectar con FACUA y realizar peticiones HTTP 🌐
    - [selenium](https://www.selenium.dev/documentation/) para interactuar con sitios web dinámicos 💻
    - [beautifulsoup4](https://beautiful-soup-4.readthedocs.io/en/latest/) para scraping de sitios web 🕸️
    - [dotenv](https://www.dotenv.org/docs/) para manejar variables de entorno de manera segura 🔐
    - [tqdm](https://tqdm.github.io/) para crear barras de progreso en los procesos largos ⏳
    - [psycopg2](https://www.psycopg.org/docs/) para conectarse y ejecutar consultas en PostgreSQL 🛢️
- **Para crear la Base de Datos**
    - [PostgreSQL](https://www.postgresql.org/) para la gestión y almacenamiento de datos relacionales 📂
    - [DBeaver](https://dbeaver.io/) para administración y consulta visual de bases de datos 🖥️

### Instalación 🛠️

1. Clona este repositorio para visualizarlo en vscode:
```bash
git clone https://github.com/apelsito/Proyecto4-AnalisisFacua.git
cd Proyecto4-AnalisisFacua
```
## Visualización y Análisis de Gráficas 📊

Para profundizar en los datos recolectados, hemos realizado diversas consultas SQL que nos permiten extraer información clave sobre precios, variaciones y patrones de los productos en los supermercados. Estas consultas nos facilitan analizar la dispersión de precios, identificar tendencias y detectar anomalías. A continuación, presentaremos una serie de gráficas interactivas basadas en estos datos, que ofrecen una visión clara y detallada del comportamiento de los precios en el mercado.


## Conclusiones ✈️



# Contribuciones 🤝

Las contribuciones a este proyecto son muy bienvenidas. Si tienes alguna sugerencia, mejora o corrección, no dudes en ponerte en contacto o enviar tus ideas.

Cualquier tipo de contribución, ya sea en código, documentación o feedback, será valorada. ¡Gracias por tu ayuda y colaboración!

# Autores y Agradecimientos ✍️

## Autor ✒️
**Gonzalo Ruipérez Ojea** - [@apelsito](https://github.com/apelsito) en github

## Agradecimientos
Quiero expresar mi agradecimiento a **Hackio** y su equipo por brindarme la capacidad y las herramientas necesarias para realizar este proyecto con solo una semana de formación. Su apoyo ha sido clave para lograr este trabajo.

