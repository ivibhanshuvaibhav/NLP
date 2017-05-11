from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example = ["smooth", "smoothening", "smoothly", "smoothed", "smoothener"]

for w in example:
    print ps.stem(w)
