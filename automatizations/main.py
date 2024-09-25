import os
from pathlib import Path
from dotenv import load_dotenv
import time


# importamos nuestras librerias
from openaigpt import openaiGPT
from notion import Notion
from report import Report


if __name__ == "__main__":
    # instanciamos las clases
    notion = Notion()
    gptopenai = openaiGPT()
    reportLTX = Report()


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
    with open(ruta_completa_learned, 'a', encoding='UTF-8') as file:
        for topic in topics:
            if topic not in learned_topics:
                # le damos el tema a openAI
                roadmap_not_formated = gptopenai.roadmap(topic=topic)

                try:
                    # y lo agregamos al notion
                    notion.page_roadmap(title=topic, data=roadmap_not_formated)
                    print(f'Pagina para el tema {topic} creada exitosamente...\n')
                except Exception as e:
                    print(f'Error al crear la página para el tema {topic}: {e}\n')
                    continue # pasar al siguiente paso en caso de error

                # agregamos los temas al archivo de vistos
                file.write(topic + '\n')


                # generamos el contenido del reporte en base al roadmap generado
                content = gptopenai.roadmap_latex(topic, roadmap_not_formated)

                # agregamos la inforación generada a un documento latex y lo ejecutamos
                reportLTX.reporte(topic, content)

                # eliminamos los archivos extra que genera latex
                reportLTX.delShitFiles('main')
                ### nota: cuando se actualize para que genere tanto el documento
                ###       como las citas, los archivos que ahora dan error dejaran de darlo
                


                # delay para no saturar la api de notion
                time.sleep(2)


    file.close()

