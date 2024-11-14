# modulo 1 libreria
# 
# funciones generales
# 
# Autor: Diego Sarceño
# Contacto: dsarceno68@gmail.com
# Tel: +502 4204 4629
# 
# 
# ------------------------------>
# paquetes necesarios
import json
import pandas as pd
import pyodbc
import warnings
import sqlite3
import locale
from datetime import datetime
import os
from sqlalchemy import create_engine
import importlib.resources as pkg_resources
import time
import importlib.resources
# ------------------------------>

class Connections:
    """
    Clase para manejar conexiones a diferentes bases de datos y ejecutar consultas.

    Métodos:
        connection(query: str, database: int) -> pd.DataFrame:
            Ejecuta una consulta en una base de datos remota.
        
        query_base_local(base: str, query: str) -> pd.DataFrame:
            Ejecuta una consulta en una base de datos local (SQLite3).
    """

    def __init__(self):
        """
        Inicializa la clase Connections. 
        """
        with importlib.resources.open_text('metodosINE', 'credenciales.json', encoding='UTF-8') as cred:
            self.__credentials = json.load(cred)

        

    def odbcfetchdata(self, query : str, database : int) -> pd.DataFrame:
        """
        Ejecuta una consulta SQL en una base de datos remota.

        :param query: Consulta SQL que se desea ejecutar.
        :type query: str
        :param database: Entero que indica a qué base de datos conectarse:
            - 1: `ipc`
            - 2: `inegt-ipc`
            - 3: `diec-critica`
        :type database: int
        :returns: Un DataFrame con los resultados de la consulta.
        :rtype: pd.DataFrame
        :raises Exception: Si ocurre un error en la conexión o durante la ejecución de la consulta.
        :example:

        .. code-block:: python

            conn = Connections()
            df = conn.odbcfetchdata("SELECT * FROM tabla", 1)
        """

        warnings.filterwarnings('ignore')

        databases = {
            1 : 'ipc',
            2 : 'inegt-ipc',
            3 : 'diec-critica'
        }
        db = databases.get(database)
        try:
            conexion = pyodbc.connect(
                driver = self.__credentials['databases'][db]['driver'],
                server = self.__credentials['databases'][db]['server'],
                database = self.__credentials['databases'][db]['database'],
                uid = self.__credentials['databases'][db]['user'],
                pwd = self.__credentials['databases'][db]['password'],
                port = self.__credentials['databases'][db]['port']
            )
            cursor = conexion.cursor()
            
            df = pd.read_sql_query(query, conexion)
        except Exception as e:
            print(f"Error: {str(e)}")
        finally:
            if 'cursor' in locals():
                cursor.close()
            
            if 'conexion' in locals():
                conexion.close()
        return df
    


    def alchemyfetchdata(self, query: str, database : int) -> pd.DataFrame:
        """
        Ejecuta una consulta SQL y devuelve los resultados como un DataFrame de pandas.

        Esta función establece una conexión a una base de datos utilizando SQLAlchemy,
        ejecuta la consulta proporcionada y devuelve el resultado en un DataFrame.

        :param query: La consulta SQL que se desea ejecutar.
        :type query: str
        :param database: Entero que indica a qué base de datos conectarse:
            - 1: `ipc`
            - 2: `inegt-ipc`
            - 3: `diec-critica`
        :type database: int
        :return: Un DataFrame de pandas que contiene los resultados de la consulta.
        :rtype: pd.DataFrame

        :raises Exception: Si ocurre un error durante la conexión o la ejecución de la consulta,
                        se imprime el error y se devuelve un DataFrame vacío.

        **Ejemplo de uso:**

        .. code-block:: python

            conn = Connections()

            query = "SELECT * FROM tabla"
            df = conn.alchemyfetchdata(query, 2)
            print(df)
        """
        warnings.filterwarnings('ignore')

        # Tomamos la base de datos solicitada
        databases = {
            1 : 'ipc',
            2 : 'inegt-ipc',
            3 : 'diec-critica'
        }
        db = databases.get(database)

        # Definición de las credenciales
        driver = self.__credentials['databases'][db]['driver']
        server = self.__credentials['databases'][db]['server']
        data_base = self.__credentials['databases'][db]['database']
        user = self.__credentials['databases'][db]['user']
        password = self.__credentials['databases'][db]['password']
        port = self.__credentials['databases'][db]['port']

        # Construir la URL de conexión utilizando SQLAlchemy
        connection_string = (
            f"mssql+pyodbc://{user}:{password}@{server}:{port}/{data_base}?driver={driver}"
        )

        try:
            # Crear el motor de conexión
            engine = create_engine(connection_string)

            # Leer la consulta SQL y devolver un DataFrame
            df = pd.read_sql_query(query, engine)
        except Exception as e:
            print(f"Error: {str(e)}")
            df = pd.DataFrame()  # Retornar un DataFrame vacío en caso de error
        finally:
            # Cerrar el motor de conexión (el motor se cierra automáticamente al eliminarlo)
            if 'engine' in locals():
                engine.dispose()

        return df


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

            conn = Connections()
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

class Other:
    """
    Clase que contiene métodos auxiliares para registrar eventos y mostrar mensajes.

    Métodos:
        record(script_name: str, exec_time: str) -> None:
            Registra el nombre del script y el tiempo de ejecución en un archivo.
        
        exito(show: bool = True) -> None:
            Imprime un mensaje ASCII de éxito en la consola.
    """
        
    def __init__(self):
        """
        Inicializa la clase Other. No recibe parámetros ni realiza ninguna acción durante la inicialización.
        """
                
        pass

    def record(self, script_name : str, exec_time : str) -> None:
        """
        Registra el nombre del script, la fecha y hora, y el tiempo de ejecución en el archivo 'record.txt'.

        :param script_name: Nombre del script que se está ejecutando.
        :type script_name: str
        :param exec_time: Tiempo de ejecución del script.
        :type exec_time: str
        :returns: None
        :example:

        .. code-block:: python

            logger = Other()
            logger.record("mi_script.py", "1452 segundos")
        """
        #locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")
        locale.setlocale(locale.LC_TIME, "Spanish")
        current_datetime = datetime.now()
        format_current_datetime = current_datetime.strftime("%A, %d de %B de %Y, %H:%M:%S")
        with open("record.txt", 'a') as f:
            f.write(script_name + ', ' + format_current_datetime + ', ' + exec_time + "\n")
        f.close()


    def listar_directorios(self, base_path, archivo_salida, nivel=0):
        """Lista los directorios y archivos en formato de árbol y los guarda en un archivo."""
        # Abre el archivo para escribir con codificación UTF-8
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            archivo.write("```markdown\n")
            archivo.write(f"{base_path}/\n")
            self._listar_directorios_recursivo(base_path, archivo, nivel)
            archivo.write("```\n")

    def _listar_directorios_recursivo(self, base_path, archivo, nivel):
        """Función recursiva para listar directorios y archivos."""
        espacios = '    ' * nivel  # Espacio para el nivel
        items = os.listdir(base_path)  # Lista de elementos en el directorio
        items.sort()  # Ordena alfabéticamente
        
        for index, item in enumerate(items):
            ruta_completa = os.path.join(base_path, item)
            # Comprobar si es el último elemento para la visualización correcta del árbol
            if os.path.isdir(ruta_completa):
                if index == len(items) - 1:
                    archivo.write(f"{espacios}└── {item}/\n")
                else:
                    archivo.write(f"{espacios}├── {item}/\n")
                self._listar_directorios_recursivo(ruta_completa, archivo, nivel + 1)
            else:
                if index == len(items) - 1:
                    archivo.write(f"{espacios}└── {item}\n")
                else:
                    archivo.write(f"{espacios}├── {item}\n")



class decorators:
    def __init__(self) -> None:
        pass


    def tiempo_ejecucion(self, func):
        def wrapper(*args, **kwargs):
            global tiempo_global
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            tiempo_global = end - start
            print('Tiempo de ejecución: {:.6f}'.format(tiempo_global))
            return result
        return wrapper
    

    def inicio_y_fin(self, func):
        def wrapper(*args, **kwargs):
            print(f"Inicio de la función: {func.__name__}")
            result = func(*args, **kwargs)
            print(f"Fin de la función: {func.__name__}")
            print()
            return result
        return wrapper

    

    def exito(self, show : bool = True) -> None:
        """
        Muestra un mensaje ASCII en la consola indicando el éxito de una operación.

        :param show: Si es True, imprime el mensaje ASCII. Por defecto es True.
        :type show: bool
        :returns: None
        :example:

        .. code-block:: python

            notifier = Other()
            notifier.exito()
        """

        if show:
            print("         _nnnn_")
            print('        dGGGGMMb     ,""""""""".')
            print("       @p~qp~~qMb    | ¡Éxito! |")
            print("       M|@||@) M|   _;.........'")
            print("       @,----.JM| -'")
            print("      JS^\__/  qKL")
            print("     dZP        qKRb")
            print("    dZP          qKKb")
            print("   fZP            SMMb")
            print("   HZM            MMMM")
            print("   FqM            MMMM")
            print(' __| ".        |\dS"qML')
            print(" |    `.       | `' \Zq")
            print("_)      \.___.,|     .'")
            print("\____   )MMMMMM|   .'")
            print("     `-'       `--' ")
            return None
