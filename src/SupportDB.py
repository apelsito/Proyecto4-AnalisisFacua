# importamos las librerías con las que vamos a trabajar

# Trabajar con bases de datos y python
# -----------------------------------------------------------------------
import psycopg2
from psycopg2 import OperationalError, errorcodes, errors


# Trabajar con DataFrames
# -----------------------------------------------------------------------
import pandas as pd
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


def insertar_muchos_datos_bd(conexion, query, tupla):
    try:
        cursor = conexion.cursor()
        cursor.executemany(query,tupla)
        conexion.commit()
        cursor.close()
        conexion.close()
        print("Se han añadido los valores correctamente")
    except Exception as e:
        print("No se ha podido realizar la operación:", e)


def generar_tupla(df,drop_index=False):
    if drop_index == True:
        df.drop(columns="index",inplace=True)
    tupla = [tuple(valores) for valores in df.values]
    return tupla

def consulta_sql(conexion, query):
    cursor = conexion.cursor()
    cursor.execute(query)
    resultados = cursor.fetchall()
    columnas = [col[0] for col in cursor.description]
    cursor.close()
    conexion.close()
    df = pd.DataFrame(resultados,columns=columnas)
    return df