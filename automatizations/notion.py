import requests
from dotenv import load_dotenv
import os
import re
import json



class Notion:
    def __init__(self):
        self.url_base = 'https://api.notion.com/v1/'
        #self.notion_key = os.getenv('notion_key')
        self.notion_key_roadmap = 'secret_yI1JxhCKI4byj8JqjVle7WUaXE5xAti7lctO4pBuRZ2'
        self.notion_key_dieta = 'secret_DTt6rbP0ktgmVQe95E7UySiSIzxo3qzzitFEMbssugC'
        self.notion_parent_id_roadmap = '320b399c-2f3e-445f-bd71-adce0c2d9ebe'
        #self.notion_database_id_dieta = 'a0b587a2-8f01-4e7a-8693-5ca2db02d655'
        self.notion_database_id_dieta = '1473c821-c23d-4090-b9f2-1cbe325c2264'

    
    def headers(self, key : str) -> dict:
        return {
            "Authorization" : f"Bearer {key}",
            "Content-Type" : "application/json",
            "Notion-Version" : "2022-06-28"
        }
    

    def topics(self):
        try: 
            # solicitamos la info a la pagina de notion
            response = requests.get(self.url_base + f'blocks/{self.notion_parent_id_roadmap}/children')

            # extraemos la info
            learning = []
            for topic in response['results']:
                learning.append({
                    "id": topic["id"],
                    "title" : topic["properties"]["name"]["title"][0]["plain_text"]
                })
            return learning
        except Exception as e:
            print(e)
            raise e
    
    
    def clean_indexed_line(self, line):
        # Elimina números, letras y puntos del indexado al principio de la línea
        return line[line.find('.') + 1:].strip()

    def format_roadmap(self, data : str) -> list:
        # dividimos el string en lineas
        lines = data.strip().splitlines()

        # Estructura de lista anidada
        nested_list = []
        current_section = None
        for line in lines:
            if not line:
                continue
            
            cleaned_line = self.clean_indexed_line(line)

            line = line.strip()
            if line[0].isdigit(): # si es numero es nueva seccion
                current_section = {
                    "object": "block",
                    "type": "numbered_list_item",
                    "numbered_list_item": {
                        "rich_text": [{"type": "text", "text": {"content": cleaned_line}}],
                        "children": []
                    }
                }
                nested_list.append(current_section)
            elif line[0].isalpha():
                subitem = {
                    "object": "block",
                    "type": "numbered_list_item",
                    "numbered_list_item": {
                        "rich_text": [{"type": "text", "text": {"content": cleaned_line}}]
                    }
                }
                if current_section is not None:
                    current_section["numbered_list_item"]["children"].append(subitem)
        return nested_list
    

    def topics_learning(self) -> list:
        # creamos el url
        url = self.url_base + f'blocks/{self.notion_parent_id_roadmap}/children'

        # solicitamos la información
        response = requests.get(url, headers=self.headers(self.notion_key_roadmap))

        if response.status_code == 200:
            blocks = response.json().get('results', [])

            checklist_items = []
            for block in blocks:
                if block['type'] == 'to_do':
                    item = {
                        'text' : block['to_do']['text'][0]['text']['content'],
                        'checked' : block['to_do']['checked']
                    }
                    checklist_items.append(item)
            
            return checklist_items
        else:
            print(f'Error: {response.status_code}')



    
    def page_roadmap(self, title : str, data : str) -> None:
        # creamos la pagina nueva
        children_data = {
            "children" : [
#                {
#                    "object" : "block",
#                    "type" : "heading_1",
#                    "heading_1" : {
#                        "rich_text" : [
#                            {
#                                "type" : "text",
#                                "text" : {
#                                    "content" : ''
#                                }
#                            }
#                        ]
#                    }
#                },
                {
                    "object" : "block",
                    "type" : "paragraph",
                    "paragraph" : {
                        "rich_text" : [
                            {
                                "type" : "text",
                                "text" : {
                                    "content" : data
                                }
                            }
                        ]
                    }
                }
            ]
        }

        new_page_url = self.url_base + "pages"
        new_page_data = {
            "parent": {"type" : "page_id", "page_id": self.notion_parent_id_roadmap },
            "properties": {
                "title": {
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": title
                            }
                        }
                    ]
                }
            },
            "children" : []  # Este campo puede ser omitido si no estás añadiendo bloques al momento de crear la página
        }

        print('Inicio...')
        response = requests.post(new_page_url, headers=self.headers(self.notion_key_roadmap), data=json.dumps(new_page_data))
        print(f'Página de: {title} creada...')
        #print(response.status_code)
        #print(response.text)
        page_data = response.json()
        page_id = page_data.get('id')
        print(page_id)

        
        print('Agregando info...')
        children_url = self.url_base + f'blocks/{page_id}/children'
        #response = requests.patch(children_url, headers=self.headers, json=children_data)
        response = requests.patch(children_url, headers=self.headers(self.notion_key_roadmap), json={"children" : self.format_roadmap(data)})
        print('Completado Correctamente!')

    
    def info_dieta(self): 
        # url de la tabla
        url = self.url_base + f'databases/{self.notion_database_id_dieta}/query'

        # solicitamos la info
        try:
            response = requests.post(url, headers=self.headers(self.notion_key_dieta))
            data = response.json()
            return data
        except Exception as e:
            print(e)
            raise e
        







if __name__ in "__main__":
    url_pregunta = 'https://api.notion.com/v1/users'

    title = 'Web Scraping con Selenium'
    roadmap = '''
    1. Introducción al Web Scraping
        a. Definición y conceptos básicos
        b. Importancia del web scraping en la era de big data

    2. Fundamentos de Selenium
        a. Qué es Selenium
        b. Instalación y configuración
        c. Tipos de pruebas que se pueden realizar con Selenium
        d. Comandos y estructura básica de código

    3. Interacción con elementos de la página
        a. Localización de elementos
        b. Interacción con inputs
        c. Selección de elementos
        d. Manejo de ventanas y pestañas
        e. Esperas implícitas y explícitas

    4. Extraindo datos con Selenium
        a. Extracción de información de tablas y listas
        b. Extracción de información de formularios
        c. Simulación de acciones del usuario para obtener datos

    5. Automatización de tareas con Selenium
        a. Escenarios de automatización en web scraping
        b. Creación de scripts para tareas recurrentes
        c. Programación de tareas con cron
    '''


    notion = Notion()       
    #notion.page_roadmap(title=title, data=roadmap)
    info = notion.info_dieta()
    with open(r'C:\Users\daalvarado\OneDrive - ine.gob.gt (1)\Documentos\diego_sarceño\temporalFiles\extras' + '\data_dieta.json', 'w') as file:
        json.dump(info, file, indent=4)
    file.close()
    print(info)