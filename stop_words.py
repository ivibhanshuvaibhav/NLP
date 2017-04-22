from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words("english"))

sentence = "Hello Mr. Smith, how are you doing today? I hope you are doing well. Good Day! See you later."

words = word_tokenize(sentence)

filtered_sentence = []

for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)

print filtered_sentence