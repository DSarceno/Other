import re
from googletrans import Translator
import sqlite3
import pandas as pd
import time
import tracemalloc
import numpy as np
import polars as pl


# creamos la clase con funciones útiles
class text_manipulation:
    def __init__(self) -> None:
        pass

    def estandarizar_texto(texto : str) -> str:
        """
        Dado un texto lo transforma en texto plano (sin tildes, espacios extra, carácteres especiales, y comas.).

        :param texto: Nombre del script que se está ejecutando.
        :type texto: str
        :returns: El texto plano
        :rtype: str
        :example:

        .. code-block:: python

            text = estandarizar_texto('Nombre, del script que se está ejecutando')
        """
        # funcion que vuelve cualquier texto en texto plano (sin tildes, comas, mayusculas, etc)

        # Convertir todo el texto a minúsculas
        texto = texto.lower()
        
        # Eliminar las , de buena forma
        texto = texto.replace(',', ' ')

        # Eliminar caracteres especiales excepto letras, números y espacios
        texto = re.sub(r'[^\w\s]', '', texto)
        
        # Eliminar tildes
        texto = re.sub(r'[áéíóú]', lambda x: 'aeiou'[('áéíóú'.index(x.group(0)))], texto)
 

        # Eliminar espacios extras y espacios al inicio y al final
        texto = re.sub(r'\s+', ' ', texto).strip()
        
        return texto
    

    def traducir_a_espaniol(self, texto : str) -> str:
        # creamos un traductor
        traductor = Translator()

        # Traducimos el texto a español
        traduccion = traductor.translate(texto, dest='es')

        return traduccion.text
    

class dbConnections:
    def __init__(self) -> None:
        pass


    def query_base_local(self, base : str, query : str) -> pd.DataFrame:
        """
        Ejecuta una consulta SQL en una base de datos local (SQLite3).

        :param base: Ruta a la base de datos local.
        :type base: str
        :param query: Consulta SQL que se desea ejecutar.
        :type query: str
        :returns: Un DataFrame con los resultados de la consulta.
        :rtype: pd.DataFrame
        :raises sqlite3.Error: Si ocurre un error durante la conexión o la ejecución de la consulta.
        :example:

        .. code-block:: python

            conn = dbConnections()

            df = conn.query_base_local('base_datos.db', 'SELECT * FROM tabla')
        """

        # conexion a la base local sqlite3
        try:
            conn = sqlite3.connect(base)

            dataframe = pd.read_sql_query(query, conn)
        except sqlite3.Error as e:
            print(f"Error: {str(e)}")
        finally:
            try:
                conn.close()
            except NameError:
                print("No conexion: ", NameError)
        
        return dataframe

class performance:
    def __init__(self) -> None:
        pass

    def measure_performance(func, *args, **kwargs):
        # Iniciar medición de memoria
        tracemalloc.start()
        # Medir el tiempo
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        # Medición de memoria
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        return result, elapsed_time, current, peak