# Script de treinamento do modelo

# pip install tensorflow

# Imports
import json 
import pickle
import numpy as np 
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, GlobalAveragePooling1D
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder

import tensorflow as tf   
tf.get_logger().setLevel('ERROR')

# Abre o arquivo de intents
with open('intents.json') as file:
    data = json.load(file)
    
# Listas para os dados
training_sentences = []
training_labels = []
labels = []
responses = []

# Loop
for intent in data['intents']:
    for pattern in intent['patterns']:
        training_sentences.append(pattern)
        training_labels.append(intent['tag'])
    responses.append(intent['responses'])
    
    if intent['tag'] not in labels:
        labels.append(intent['tag'])
        
# Número de classes
num_classes = len(labels)

# Encoder
lbl_encoder = LabelEncoder()
lbl_encoder.fit(training_labels)
training_labels = lbl_encoder.transform(training_labels)

# Vocabulário
vocab_size = 1000
embedding_dim = 16
max_len = 20
oov_token = "<OOV>"

# Tokenizador
tokenizer = Tokenizer(num_words = vocab_size, oov_token = oov_token)
tokenizer.fit_on_texts(training_sentences)
word_index = tokenizer.word_index
sequences = tokenizer.texts_to_sequences(training_sentences)
padded_sequences = pad_sequences(sequences, truncating = 'post', maxlen = max_len)

# Modelo
model = Sequential()
model.add(Embedding(vocab_size, embedding_dim, input_length = max_len))
model.add(GlobalAveragePooling1D())
model.add(Dense(16, activation = 'relu'))
model.add(Dense(16, activation = 'relu'))
model.add(Dense(num_classes, activation = 'softmax'))

# Compila o modelo
model.compile(loss = 'sparse_categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

# Sumário
model.summary()

# Treinamento
epochs = 500
history = model.fit(padded_sequences, np.array(training_labels), epochs = epochs)

# Salva o moodelo
model.save("./modelo/chatBot_model")

# Salva o tokenizador
with open('./modelo/tokenizer.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol = pickle.HIGHEST_PROTOCOL)
    
# Salva o encoder
with open('./modelo/label_encoder.pickle', 'wb') as ecn_file:
    pickle.dump(lbl_encoder, ecn_file, protocol = pickle.HIGHEST_PROTOCOL)


