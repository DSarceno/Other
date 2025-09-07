# librerias de manejo de texto
import re
import warnings
import nltk
from nltk.corpus import stopwords
import spacy
import torch
from transformers import BertTokenizer, BertModel

# librerias genéricas
import pandas as pd
import numpy as np



class text_management:
    def __init__(self) -> None:
        self.stop_words = set(stopwords.words('spanish'))
    
    # APLICADO A CADENAS DE TEXTO
    def remove_stop_words(self, text : str) -> str:
        words = text.split()
        cleaned_words = [word for word in words if word.lower() not in self.stop_words]
        return ' '.join(cleaned_words)

    def eliminar_etiquetas_html(self, texto : str) -> str:
        # Usamos una expresión regular para buscar y eliminar etiquetas HTML
        texto_limpio = re.sub(r'<.*?>', '', texto)
        return texto_limpio

    def limpiar_texto(self, texto : str) -> str:
        # Eliminar caracteres especiales o no alfanuméricos
        return re.sub(r'[^A-Za-z0-9 ]+', '', texto)

    def lemmatizador(self, text : str) -> str:
        # cargamos el modelo en espaniol
        nlp = spacy.load("es_core_news_sm")

        # procesamos el texto
        processed = nlp(text)

        # Extraemos los lemas
        lemmas = [token.lemma_ for token in processed]
        return ' '.join(lemmas)
    


class data_text_management:
    def __init__(self) -> None:
        self.stop_words = set(stopwords.words('spanish'))


    # APLICANDO A COLUMNAS DE UN DATAFRAME (pandas en su v1)
    # Función para eliminar etiquetas HTML de una columna
    def eliminar_etiquetas_html(self, df : pd.DataFrame, col_in : str | int, col_out : str | int) -> pd.DataFrame:
        df[col_out] = df[col_in].apply(lambda x: re.sub(r'<.*?>', '', x) if isinstance(x, str) else x)
        return df

    # Función para limpiar caracteres especiales de una columna
    def limpiar_texto(self, df : pd.DataFrame, col_in : str | int, col_out : str | int) -> pd.DataFrame:
        df[col_out] = df[col_in].apply(lambda x: re.sub(r'[^\w\s]', '', x) if isinstance(x, str) else x)
        return df
    
    # ------------->
    # correción de funcion para limpiar caracteres especiales
    def caracteres_especiales(self, df : pd.DataFrame, col_in : str | int, col_out : str | int) -> pd.DataFrame:
        df[col_out] = df[col_in].apply(lambda x: re.sub(r'[^\w\s]', ' ', x) if isinstance(x, str) else x)
        return df

    def espacios_extra(self, df : pd.DataFrame, col_in : str | int, col_out : str | int) -> pd.DataFrame:
        df[col_out] = df[col_in].apply(lambda x: re.sub(r'\s+', ' ', x).strip() if isinstance(x, str) else x)
        return df
    # ------------->

    # Función para eliminar palabras vacías de una columna
    def remove_stop_words(self, df : pd.DataFrame, col_in : str | int, col_out : str | int) -> pd.DataFrame:
        df[col_out] = df[col_in].apply(lambda x: ' '.join([word for word in x.split() if word.lower() not in self.stop_words]) if isinstance(x, str) else x)
        return df

    def lemmatizador(self, df : pd.DataFrame, col_in : str | int, col_out : str | int) -> pd.DataFrame:
        # cargamos el modelo en espaniol
        nlp = spacy.load('es_core_news_sm')

        # aplicamos a cada fila de la columna entrada
        df[col_out] = df[col_in].apply(
            lambda x: ' '.join([token.lemma_ for token in nlp(x)]) if isinstance(x, str) else x
        )
        return df

    def rating(self, df : pd.DataFrame, col_in : str | int, col_out : str | int) -> pd.DataFrame:
        conditions = [
            (df[col_in] >= 0) & (df[col_in] < 4),
            (df[col_in] >= 4) & (df[col_in] <= 6),
            (df[col_in] > 6) & (df[col_in] <= 10)]
        labels = ['Mala', 'Pasable/Normal', 'Buena']
        df[col_out] = np.select(conditions, labels, default=np.nan)
        return df
    
    def cleaning_pipeline(self, df : pd.DataFrame, col_in : str, col_out : str) -> pd.DataFrame:
        result = (df
              .pipe(self.eliminar_etiquetas_html, col_in, col_out)
              .pipe(self.caracteres_especiales, col_out, col_out)
              .pipe(self.espacios_extra, col_out, col_out)
              .pipe(self.remove_stop_words, col_out, col_out)
              .pipe(self.lemmatizador, col_out, col_out))
        return result
    


#no funciona
class tokenizer_transform:
    def __init__(self) -> None:
        # tokenizador
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

        # definimos el modelo para que no sea case-sensitive
        self.model = BertModel.from_pretrained('bert-base-uncased')


    def vectorizador(self, texto : str) -> torch.Tensor:
        # se tokeniza la oración para convertirse en una estructura BERT
        inputs = self.tokenizer(texto, return_tensors='pt')

        # se desactiva el calculo del gradiente
        with torch.no_grad():
            outputs = self.model(**inputs)
        
        # extraemos los embeddings
        embeddings = outputs.last_hidden_state
        return embeddings
    

    def obtener_embeddings(self, texto : str) -> np.array:
        # Mover el modelo a GPU si está disponible
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model.to(device)

        # Tokenización del texto y creacion de tensores
        inputs = self.tokenizer(texto, return_tensors='pt', truncation=True, padding=True, max_length=128)
        inputs = {k: v.to(device) for k, v in inputs.items()}

        # Generar embeddings con BERT sin cálculo de gradientes
        with torch.no_grad():
            outputs = self.model(**inputs)

        # tomar el embedding de la ultima capa
        embeddings = outputs.last_hidden_state.mean(dim=1)
        return embeddings.cpu().numpy()
    

    def get_embedding(self, texto : str) -> np.array:
        # Tokenizacion y creación de tensores
        inputs = self.tokenizer(texto, return_tensors='pt', padding=True, truncation=True, max_length=512)
        with torch.no_grad(): # desactivar el calculo de gradientes
            outputs = self.model(**inputs)
            # extraer el embedding de [CLS] (índice 0)
            embeddings = outputs.last_hidden_state[:, 0, :]
        return embeddings.squeeze().numpy()
    


if '__main__' in __name__:
    warnings.filterwarnings('ignore')

    # leemos el conjunto de datos a utilizar
    imdb_es = pd.read_csv(r'../data/IMDB_spanish.csv', sep=',')

    # creamos el objeto
    dtm = data_text_management()

    # limpiamos el texto con la función de pipe
    imdb_es_mod = dtm.cleaning_pipeline(imdb_es, 'review_es', 'review_es_mod')

    # tokenizar las etiquetas
    imdb_es_mod['sentimiento_token'] = imdb_es_mod['sentimiento'].map({'positivo' : 1, 'negativo' : 0})


    # exportamos a un csv
    imdb_es_mod.to_csv(r'../data/imdb_espaniol_mod.csv', sep=',', index=False)