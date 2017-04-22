from nltk.tokenize import word_tokenize, sent_tokenize

sentence = "Hello Mr. Smith, how are you doing today? I hope you are doing well. Good Day! See you later."

print word_tokenize(sentence)

print sent_tokenize(sentence)