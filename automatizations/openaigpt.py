import os
from dotenv import load_dotenv
from openai import OpenAI
import json
import subprocess

class openaiGPT:
    def __init__(self) -> None:
        # Cargamos la info del archivo .env (api)
        load_dotenv()

        # seteamos el cliente de la api con nuestra api-key
        self.client = OpenAI(
            api_key = os.getenv("openai_key")
        )
    
    def roadmap(self, topic : str):
        role = "Eres un profesor dedicado a hacer material de estudio."
        prompt = f'Soy un Científico de Datos que quiere aprender sobre nuevos temas. Me gustaría que generaras un roadmap (como lista anidada) basado en el siguiente tema: {topic}.'

        print(f'Generando Roadmap del tema: {topic}...')
        try:
            completion = self.client.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt = prompt,
                max_tokens = 750
            )
            generated_text = completion.choices[0].text
            return generated_text
        except Exception as e:
            print(f'Error: {e}')
        print(f'Roadmap de {topic} generado...')

    
    def macros(self, food : str):
        basic_prompt = '''
            Eres un nutricionista. A partir de la información que te proporcione sobre una comida, genera unicamente un diccionario en el siguiente formato:

                {
                    "Calorías (kcal)": # cantidad total de calorías,
                    "Proteínas (gramos)": # cantidad total de proteínas en gramos,
                    "Carbohidratos (gramos)": # cantidad total de carbohidratos en gramos,
                    "Grasas (gramos)": # cantidad total de grasas en gramos,
                    "Fibra (gramos)": # cantidad total de fibra en gramos
                }

            Comida consumida: \n
        '''

        prompt = basic_prompt + food

        print('Generando información...')
        try:
            completion = self.client.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt = prompt,
                max_tokens = 100,
                n=1,
                stop=None,
                temperature=0.5
            )
            diet_info = completion.choices[0].text.strip()
            return diet_info
        except Exception as e:
            print(f"Error: {e}")
        print('Informacion de dieta generada...')


    def roadmap_latex(self, topic : str):
        prompt = f'Eres un profesor. Necesito que generes un reporte de latex acerca de: {topic}.'

        print('Generando reporte...')

        try:
            completion = self.client.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt=prompt,
                max_tokens=1500,
                n=1,
                stop=None,
                temperature=0.5
            )
            diet_info = completion.choices[0].text
            return diet_info
        except Exception as e:
            print(f'Error: {e}')
        print('Reporte generado...')


if __name__ == "__main__":
    ogpt = openaiGPT()


    '''
    food = '2 huevos revueltos con 3 chorizos perri y 4 panqueques con jalea de fresa'

    info = ogpt.macros(food=food)
    print(info)

    print('\n')

    try: 
        nutinfo = json.loads(info)
        print(nutinfo)
    except Exception as e:
        print(f'Error: {e}')
    '''
    topic = 'PyTorch'
    reporte = ogpt.roadmap_latex(topic)
    print(reporte)

    with open('main.tex', 'w', encoding='UTF-8') as f:
        f.write(reporte)
    f.close()

    comando = '.\dockerrun.bat'
    try:
        ejecucion = subprocess.run(comando, shell=True, check=True, text=True, capture_output=True)
        print(ejecucion.stdout)

        os.rename('main.pdf', 'PyTorch.pdf')
        os.rename('main.tex', 'PyTorch.tex')
    except subprocess.CalledProcessError as e:
        print(f'Error al ejecutar el comando: {e.stderr}')


    