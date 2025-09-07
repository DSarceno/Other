# modulo 2 libreria
# 
# funciones especificas
# 
# Autor: Diego Sarceño
# Contacto: dsarceno68@gmail.com
# Tel: +502 4204 4629
# 
# 
# ------------------------------>
# paquetes necesarios
import re
import pandas as pd
# ------------------------------>

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



def month(mes : str | int, es_numerico : bool = True) -> int | str:
    """
    Cambia el número de mes por el nombre del mes y viceversa.

    :param mes: Nombre o númeor de mes.
    :type mes: str | int
    :param es_numerico: Booleano que dice si el mes ingresado esta en texto (False) o número (True)
    :type es_numerico: bool
    :returns: El nombre del mes o el número del mismo dependiendo de su input.
    :rtype: int | str
    :example:

    .. code-block:: python

        mes = month(2, es_numerico=True) # output: Febrero
    """
    meses = {
        1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 
        5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto", 
        9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
    }

    if es_numerico:
        if mes in meses:
            return meses[mes]
    else: 
        mes = mes.lower()
        meses_invertido = {v.lower(): k for k, v in meses.items()}
        if mes in meses_invertido:
            return meses_invertido[mes]