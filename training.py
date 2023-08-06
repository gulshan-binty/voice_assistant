import random
import json
import pickle
import numpy as np
import nltk 
from nltk.stem import WordNetLemmatizer
import tensorflow as tf
from tensorflow import keras

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense,Activation,Dropout
from tensorflow.python.keras.optimizers import gradient_descent_v2
#from tensorflow.python.keras.optimizers import SDG
#from tensorflow.python.keras.optimizer_v1 import SGD


lemmatizer = WordNetLemmatizer()

intents = json.loads(open('intents.json').read())

words = []
classes = []
documents = []
ignoreLetters = ['?', '!', '.', ',']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        wordList = nltk.word_tokenize(pattern)
        words.extend(wordList)
        documents.append((wordList, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [lemmatizer.lemmatize(word) for word in words if word not in ignoreLetters]
words = sorted(set(words))

classes = sorted(set(classes))

pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

training = []
output_Empty = [0] * len(classes)

for document in documents:
    bag = []
    word_Patterns = document[0]
    word_Patterns = [lemmatizer.lemmatize(word.lower()) for word in word_Patterns]
    for word in words:
        bag.append(1) if word in word_Patterns else bag.append(0)

    output_Row = list(output_Empty)
    output_Row[classes.index(document[1])] = 1
    training.append([bag, output_Row])

random.shuffle(training)
training = np.array(training)

trainX =list(training[:, 0])
trainY = list(training[:, 1])

model =Sequential()
model.add(Dense(128, input_shape=(len(trainX[0]),), activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(len(trainY[0]), activation='softmax'))

sgd = gradient_descent_v2.SGD(lr=0.01,decay=1e-6,momentum=0.9,nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

model.fit(np.array(trainX), np.array(trainY), epochs=200, batch_size=5, verbose=1)
model.save('chatbotmodel.h5')








