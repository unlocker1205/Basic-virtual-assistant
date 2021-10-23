import json
import pickle
from typing import Sequence # Làm việc với file json
from nltk.stem import WordNetLemmatizer # Chia các từ tương tự nhau về từ gốc
import nltk
# nltk.download('punkt')
# nltk.download('wordnet')
import random
from nltk.tag import sequential
import numpy as np
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, Activation, Dropout
# from tensorflow.keras.optimizers import SGD
# from tensorflow.python.keras.engine import input_spec

lemmatizer = WordNetLemmatizer()

intents = json.loads(open("data.json", encoding="utf8").read())

words = []
classes = []
documents = []
ignore_letters = ["?", "!", ".", ","]

for intent in intents['datas']:
    for pattern in intent['patterns']:
        # word_list = nltk.word_tokenize(pattern)
        words.append(pattern)
        documents.append((pattern, intent['tag']))
        if intent["tag"] not in classes:
            classes.append(intent["tag"])

# words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
words = sorted(set(words)) # Loại bỏ các phần tử trùng lặp

classes = sorted(set(classes))

if 'hey' in documents:
    print("Có phần tử này")

print(words)
print(documents)
print(classes)

# pickle.dump(words, open('words.pkl', "wb")) # Sử dụng pickle để lưu trữ word dưới dạng nhị phân (wb)
# pickle.dump(classes, open('classes.pkl', "wb"))

# training = []
# output_empty = [0] * len(classes)

# for document in documents:
#     bag = []
#     word_patterns = document[0]
#     word_patterns = [lemmatizer.lemmatize(word.lower() for word in word_patterns)]
#     for word in words:
#         bag.append(1) if word in word_patterns else bag.append(0)

#     output_row = list(output_empty)
#     output_row[classes.index(document[1])] = 1
#     training.append([bag, output_row])

# random.shuffle(training)
# training = np.array(training)

# train_x = list(training[:, 0])
# train_y = list(training[:, 1])

# model = Sequential()
# model.add(Dense(128, input_shape = (len(train_x[0]), ), activation='relu'))
# model.add(Dropout(0.5))
# model.add(Dense(64, activation='relu'))
# model.add(Dropout(0.5))
# model.add(Dense(len(train_y[0]), activation='softmax'))

# sgd = SGD(lr=0.01, decay = 1e-6, momentum=0.9, nesterov=True)
# model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
# model.save('chatbot_model.model')
# print("Done")