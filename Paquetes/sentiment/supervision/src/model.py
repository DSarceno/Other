import pandas as pd
import numpy as np
import json
import keras
import warnings


import tensorflow as tf
from tensorflow.keras.layers import Dense, Input, LSTM, Embedding, Dropout, Activation, Bidirectional, GlobalMaxPool1D
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing import text, sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import EarlyStopping


class Models:
    # Clase con la que se despliega y entrena el modelo.
    # --------> De hacer una actualización que modifique la arquitectura, crear un nuevo método.
    def __init__(self) -> None:
        pass
    

    def shuffle_n_split_data(self, df : pd.DataFrame, test_percentage : float) -> list[pd.Series, pd.Series]:
        # shuffle data
        df = df.sample(frac=1)

        # if test_percentage is bigger than 1 or lesser than 0, we'll take 0.2
        if (test_percentage > 1) or (test_percentage < 0):
            test_percentage = 0.2

        # split dataset in train and test
        df_train = df[test_percentage:]
        df_test = df[:test_percentage]
        return df_train, df_test


    def create_n_save_tokenizer(self, df_column : pd.Series, max_features : int, output_name : str):
        # class instance
        tokenizer = Tokenizer(num_words=max_features)

        # fit on the column texts
        tokenizer.fit_on_texts(df_column)

        # save
        with open(output_name + '.json', 'w') as j:
            json.dump(tokenizer.to_json(), j)
        return tokenizer
    

    def text_sequences(self, to_sec_col : pd.Series, tokenizer, maxlen : int) -> np.ndarray:
        # tokenizamos el texto
        result = tokenizer.text_to_sequences(to_sec_col)

        # generamos un array bidimensional
        result = sequence.pad_sequences(result, maxlen=maxlen, padding='post')
        return result
    
    def create_model(self, max_features : int, embed_size : int) -> keras.models.Sequential:
        # Definimos el modelo y su arquitectura
        model = Sequential([
            Embedding(max_features, embed_size),
            LSTM(60, return_sequences=True),
            GlobalMaxPool1D(),
            Dense(50, activation='relu'),
            Dropout(0.1),
            Dense(2, activation='sigmoid')
        ])
        return model
    
    




if "__main__" in __name__:
    warnings.filterwarnings('filter')

    # creamos el objeto
    mod = Models()

    # importamos el conjunto de datos ya limpio y listo
    data = pd.read_csv(r'../data/imdb_espaniol_mod.csv', sep=',')

    # aislamos las columnas a utilizar y revisamos los tipos de datos
    data = data[['sentiemiento_token', 'review_es_mod']]
    data['sentiemiento_token'] = data['sentiemiento_token'].astype('Int64')

    # aleatorizamos el dataframe y dividimos en test y train
    data_train, data_test = mod.shuffle_n_split_data(data, 0.1)

    # creamos el tokenizador
    max_features = 10000
    tokenizer = mod.create_n_save_tokenizer(data_train['review_es_mod'], max_features=max_features, output_name=r'../model/cs_tokenizer')

    # cambiamos el texto a secuencias para su posterior embedding
    X_train = tokenizer.texts_to_sequences(data_train['review_es_mod'])
    X_test = tokenizer.texts_to_sequences(data_test['review_es_mod'])

    # pad sequences
    maxlen = max([len(x) for x in X_train])
    with open(r'../model/maxlen') as ml:
        ml.write(str(maxlen))

    # creamos los arrays bidimensionales
    X_train = sequence.pad_sequences(X_train, maxlen=maxlen, padding='post')
    X_test = sequence.pad_sequences(X_test, maxlen=maxlen, padding='post')

    # dividimos las etiquetas en train y test
    y_train = data_train['sentiemiento_token'].values
    y_test = data_test['sentiemiento_token'].values

    # validación y evaluación
    validation_split = 0.5
    validation_size = int(len(X_test) * validation_split)

    X_val = X_test[:validation_size]
    y_val = y_test[:validation_size]

    X_eval = X_test[validation_size:]
    y_eval = y_test[validation_size:]

    # dimensionalidad del embedding
    embed_size = 128

    # creamos el modelo
    model = mod.create_model(max_features=max_features, embed_size=embed_size)
    

    # definimos el tamaño de los batches y la cantidad de epochs
    batch_size = 128
    epochs = 30

    # se compila el modelo
    model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    # entrenamos el modelo
    early_stoppping = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)
    model.fit(X_train, y_train, batch_size=batch_size, epochs=epochs, validation_data=(X_val, y_val), callbacks=[early_stoppping]) 

    # vemos la accuracy del modelo
    score = model.evaluate(X_eval, y_eval, batch_size=batch_size)
    print(f'Test loss: {score[0]} - Test accuracy: {score[1]}')


    # ------> guardamos <------ # 
    # modelo
    model.save(r'../model/cs_class_model.h5')
    keras.saving.save_model(model, r'../model/cs_class_model.keras')

    # guardando solo los pesos
    model.save_weights(r'../model/cs_class_model.weights.h5')
