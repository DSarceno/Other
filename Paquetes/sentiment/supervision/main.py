# project
from src.data_preprocessing import data_text_management, text_management, tokenizer_transform
from src.utils import performance

# libraries
import pandas as pd
import numpy as np
import json
import warnings

# model libraries
import tensorflow as tf
import keras
from tensorflow.keras.models import load_model
from tensorflow.preprocessing.text import tokenizer_from_json
from tesnorflow.keras.preprocessing import sequence



if "__main__" in __name__:
    warnings.filterwarnings('ignore')

    # creamos los objetos
    dtm = data_text_management()


    # llamamos al modelo
    ruta_modelo = r'model/my_mnodel.h5'
    #ruta_modelo = r'model/my_model.keras'
    model = load_model(ruta_modelo)


    # importamos el tokenizer
    with open(r'model/cs_tokenizer.json') as f:
        data = json.load(f)
        tokenizer = tokenizer_from_json(data)

    