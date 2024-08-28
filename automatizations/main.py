import os
from dotenv import load_dotenv
from openai import OpenAI

# Cargamos la info del archivo .env (api)
load_dotenv()

# seteamos el cliente de la api con nuestra api-key
client = OpenAI(
    api_key = os.getenv("openai_key")
)

role = "Eres un profesor dedicado a hacer material de estudio."
tema = 'Web Scraping con Selenium'
prompt = f'Soy un Científico de Datos que quiere aprender sobre nuevos temas. Me gustaría que generaras un roadmap basado en el siguiente tema: {tema}'

print('Generando Roadmaps...')
try:
    completion = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt = prompt,
        max_tokens = 250
    )

    generated_text = completion.choices[0].text
    print(generated_text)
except Exception as e:
    print(f'Error: {e}')


print('Éxito!')