import requests
from dotenv import load_dotenv
import os
import re
import json



class Notion:
    def __init__(self):
        # cargamos el archivo de entorno con las api keys
        load_dotenv()

        self.url_base = 'https://api.notion.com/v1/'

        # keys
        self.notion_key_roadmap = os.getenv('notion_key_roadmap')
        self.notion_key_dieta = os.getenv('notion_key_diet')
        
        # ids
        self.notion_parent_id_roadmap = '320b399c-2f3e-445f-bd71-adce0c2d9ebe'
        self.notion_database_id_dieta = '1473c821-c23d-4090-b9f2-1cbe325c2264'

    
    def headers(self, key : str) -> dict:
        return {
            "Authorization" : f"Bearer {key}",
            "Content-Type" : "application/json",
            "Notion-Version" : "2022-06-28"
        }
    
    def clean_indexed_line(self, line):
        # Elimina números, letras y puntos del indexado al principio de la línea
        return line[line.find('.') + 1:].strip()
    

    def split_text(self, text : str, max_length = 2000):
        # dividimos el texto en bloques de maximo max_length caracteres
        return [text[i:i + max_length] for i in range(0, len(text), max_length)]



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

        # realizamos la solicitud a la api
        response = requests.get(url, headers=self.headers(self.notion_key_roadmap))

        # verificamos si la solicitud fue exitosa
        if response.status_code == 200:
            data = response.json()
            topics = []
            for block in data['results']:
                if block['type'] == 'to_do':
                    # verifica si el bloque contiene texto
                    to_do_block = block.get('to_do', {})
                    text_elements = to_do_block.get('rich_text', [])
                    if text_elements:
                        # extrae el texto del primer elemento
                        plain_text = text_elements[0].get('plain_text', '')
                        topics.append(plain_text)
            return topics
        else:
            return f'Error: {response.status_code}, {response.text}'


    def structure(self):
        # creamos el url
        url = self.url_base + f'blocks/{self.notion_parent_id_roadmap}/children'

        # realizamos la solicitud a la api
        response = requests.get(url, headers=self.headers(self.notion_key_roadmap))

        # verificamos si la solicitud fue exitosa
        if response.status_code == 200:
            data = response.json()
            with open(r'/home/diego/Documents/Other/automatizations/' + 'learning.json', 'w') as file:
                json.dump(data, file, indent=4)
            file.close()


    
    def page_roadmap(self, title : str, data : str) -> None:
        # creamos la pagina nueva

        # dividimos el texto en bloques de 2000 caracteres
        text_blocks = self.split_text(data)

        # formato de la informacion a mostrar en la pagina
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
                                    "content" : block
                                }
                            }
                        ]
                    }
                } for block in text_blocks
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
        #print(response.status_code, response.text)

        page_data = response.json()
        page_id = page_data.get('id')
        #print(page_id)

        
        print('Agregando info...')
        children_url = self.url_base + f'blocks/{page_id}/children'
        response = requests.patch(children_url, headers=self.headers(self.notion_key_roadmap), json=children_data)
        #print(response.status_code, response.text)
        #if formated == True:
        #    response = requests.patch(children_url, headers=self.headers(self.notion_key_roadmap), json={"children" : self.format_roadmap(data)})
        #else:
        #response = requests.patch(children_url, headers=self.headers(self.notion_key_roadmap), json=children_data)
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
    notion = Notion()       
    #notion.page_roadmap(title=title, data=roadmap)
    #info = notion.info_dieta()
    #with open(r'C:\Users\daalvarado\OneDrive - ine.gob.gt (1)\Documentos\diego_sarceño\temporalFiles\extras' + '\data_dieta.json', 'w') as file:
    #    json.dump(info, file, indent=4)
    #file.close()
    #print(info)

    #topics = notion.topics_learning()
    #print(topics)

    notion.structure()