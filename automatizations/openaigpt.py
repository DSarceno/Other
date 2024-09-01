import os
from dotenv import load_dotenv
from openai import OpenAI

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