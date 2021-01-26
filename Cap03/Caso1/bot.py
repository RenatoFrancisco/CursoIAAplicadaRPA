# Script ppara fazer previsões (usar o bot)

# Imports
import json 
import random
import pickle
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
import colorama 
colorama.init()
from colorama import Fore, Style, Back

import tensorflow as tf   
tf.get_logger().setLevel('ERROR')

# Carrega as intents
with open("intents.json") as file:
    data = json.load(file)

# Bot
def chat():
    # load trained model
    model = keras.models.load_model('./modelo/chatBot_model')

    # Carrega o tokenizador
    with open('./modelo/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    # Carrega o encoder
    with open('./modelo/label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)

    # Parâmetros
    max_len = 20
    
    # Loop
    while True:
        print(Fore.LIGHTBLUE_EX + "Você: " + Style.RESET_ALL, end = "")
        inp = input()
        if inp.lower() == "fim":
            break

        # Previsões com o modelo
        result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]), truncating = 'post', maxlen = max_len))

        # Encoding
        tag = lbl_encoder.inverse_transform([np.argmax(result)])

        for i in data['intents']:
            if i['tag'] == tag:
                print(Fore.GREEN + "Bot Joana:" + Style.RESET_ALL , np.random.choice(i['responses']))

print(Fore.YELLOW + "Inicie a conversa com o bot (digite FIM para encerrar)!" + Style.RESET_ALL)
chat()


