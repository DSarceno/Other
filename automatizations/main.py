import os
from pathlib import Path
from dotenv import load_dotenv
import time


# importamos nuestras librerias
from openaigpt import openaiGPT
from notion import Notion

# instanciamos las clases
notion = Notion()
gptopenai = openaiGPT()


# encontramos los temas a tratar
topics = notion.topics_learning()


# obtenemos la ruta
#ruta_actual = Path().resolve()
#ruta_completa_learned = ruta_actual / 'topics_done.txt'
ruta_actual = os.path.abspath(os.getcwd())
ruta_completa_learned = os.path.join(ruta_actual, 'topics_done.txt')


# leemos los temas ya tratados anteriormente
with open(ruta_completa_learned, 'r') as file:
    learned_topics = [line.strip() for line in file]
file.close()


# navegamos por todos los temas en la pagina 'Learning'
with open(ruta_completa_learned, 'a') as file:
    for topic in topics:
        if topic not in learned_topics:
            # le damos el tema a openAI
            roadmap_not_formated = gptopenai.roadmap(topic=topic)
            #print(roadmap_not_formated)
            
            #if len(roadmap_not_formated) > 2000:
            #    roadmap_not_formated = roadmap_not_formated[:2000]

            try:
                # y lo agregamos al notion
                notion.page_roadmap(title=topic, data=roadmap_not_formated)
                print(f'Pagina para el tema {topic} creada exitosamente...\n')
            except Exception as e:
                print(f'Error al crear la página para el tema {topic}: {e}\n')
                continue # pasar al siguiente paso en caso de error

            # agregamos los temas al archivo de vistos
            file.write(topic + '\n')

            # delay para no saturar la api de notion
            time.sleep(2)


file.close()

