# importamos las librerías con las que vamos a trabajar

# Trabajar con bases de datos y python
# -----------------------------------------------------------------------
import psycopg2
from psycopg2 import OperationalError, errorcodes, errors


# Trabajar con DataFrames
# -----------------------------------------------------------------------
import pandas as pd

from geopy.geocoders import Nominatim
import dotenv    
import os

def conectarse_a_bd(db,user,pwd):
    try:
        conexion = psycopg2.connect(
            database = db,
            user = user,
            password = pwd,#Esto en un .env
            host = "localhost",
            port = "5432" )
        print (f"Conectado a la base de datos: {db}")
        return conexion
    except OperationalError as e:
        if e.pgcode == errorcodes.INVALID_PASSWORD:
            print("La contraseña es errónea")
        elif e.pgcode == errorcodes.CONNECTION_EXCEPTION:
            print("Error de conexión")
        else:
            print(f"Ocurrió el error {e}")

def modificar_bd(conexion, query):
    try:
        cursor = conexion.cursor()
        cursor.execute(query)
        conexion.commit()
        cursor.close()
        conexion.close()
        print("Se ha modificado correctamente la base de Datos")
    except Exception as e:
        print("No se ha podido realizar la operación:", e)

            
