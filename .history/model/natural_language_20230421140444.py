# import tensorflow as tf 
# from tensorflow import keras

# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# import re

# def no_accent_vietnamese(s):
#     s = re.sub('[áàảãạăắằẳẵặâấầẩẫậ]', 'a', s)
#     s = re.sub('[ÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬ]', 'A', s)
#     s = re.sub('[éèẻẽẹêếềểễệ]', 'e', s)
#     s = re.sub('[ÉÈẺẼẸÊẾỀỂỄỆ]', 'E', s)
#     s = re.sub('[óòỏõọôốồổỗộơớờởỡợ]', 'o', s)
#     s = re.sub('[ÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢ]', 'O', s)
#     s = re.sub('[íìỉĩị]', 'i', s)
#     s = re.sub('[ÍÌỈĨỊ]', 'I', s)
#     s = re.sub('[úùủũụưứừửữự]', 'u', s)
#     s = re.sub('[ÚÙỦŨỤƯỨỪỬỮỰ]', 'U', s)
#     s = re.sub('[ýỳỷỹỵ]', 'y', s)
#     s = re.sub('[ÝỲỶỸỴ]', 'Y', s)
#     s = re.sub('đ', 'd', s)
#     s = re.sub('Đ', 'D', s)
#     return s

# sentences = [
#     "tôi yêu chó",
#     "tôi yêu mèo"
# ]

# sentences = [no_accent_vietnamese(sentence) for sentence in sentences]
# print(sentences)

# tokenizer = Tokenizer(num_words = 100, oov_token="<OOV>")
# tokenizer.fit_on_texts(sentences)
# word_index = tokenizer.word_index

# sequences = tokenizer.texts_to_sequences(sentences)

# padded = pad_sequences(sequences, maxlen=5)
# print("\nWord Index = " , word_index)
# print("\nSequences = " , sequences)
# print("\nPadded Sequences:")
# print(padded)


# # Try with words that the tokenizer wasn't fit to
# test_data = [
#     no_accent_vietnamese('tôi rất yêu chó của tôi'),
#     no_accent_vietnamese('chó của tôi rất yêu mèo của tôi')
# ]

# test_seq = tokenizer.texts_to_sequences(test_data)
# print("\nTest Sequence = ", test_seq)

# padded = pad_sequences(test_seq, maxlen=10)
# print("\nPadded Test Sequence: ")
# print(padded)

# import speech_recognition as sr 

# r = sr.Recognizer()

# with sr.Microphone() as source:
#     audio_data = r.record(source, duration=3)
#     print("Listen:")
#     text = r.recognize_google(audio_data, language="vi", show_all = True)
#     print(text)


import openai

openai.api_key = ""

output = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    message=[{
        "role":"user",
        "content": "Hello, how are you?"
    }]
)

print(output)

import openai
openai.api_key = "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"

def generate_text(prompt, model, length):
    response = openai.Completion.create(
      engine=model,
      prompt=prompt,
      max_tokens=length
    )
    return response.choices[0].text

prompt = "Write a short story about a robot that goes on an adventure"
model = "davinci" # or any other available model
length = 100 # length of the generated text in tokens

generated_text = generate_text(prompt, model, length)
print(generated_text)

# import speech_recognition as sr

# # obtain audio from the microphone
# r = sr.Recognizer()
# print("Say something!")
# with sr.Microphone() as source:
#     audio_data = r.record(source, duration=5)
    
#     text = r.recognize_google(audio_data, language="vi-VN")
#     print(text)


# from gtts import gTTS
# import os
# import playsound


# tts = gTTS(text = "Xin chào",lang='vi')
# tts.save("Siri.mp3")
# playsound.playsound('Siri.mp3', True)