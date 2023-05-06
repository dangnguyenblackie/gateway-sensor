# import tensorflow as tf 
# from tensorflow import keras
# from tensorflow.keras.preprocessing.text import Tokenizer

# sentences = [
#     "toi yeu cho",
#     "toi yeu meo"
# ]

# tkenizer = Tokenizer(num_words=100)
# tkenizer.fit_on_texts(sentences)

# word_index = tkenizer.word_index
# print(word_index)

import speech_recognition as sr 

r = sr.Recognizer()

with sr.Microphone() as source:
    audio_data = r.record(source, duration=5)
    print("Listen:")
    text = r.recognize_google(audio_data, language="vi")
    print(text)
