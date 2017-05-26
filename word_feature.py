import nltk
import random
from nltk.corpus import movie_reviews

documents = []

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

for i in documents:
    print i

all_words = []

for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)

for i in all_words.viewitems():
    print i[0]
    print i[1]

word_feature = list(all_words.keys()[:3000])

def find_features(document):
    words = set(document)
    features = {}
    for w in word_feature:
        features[w] = (w in words)

    return features

print find_features(movie_reviews.words("pos/cv000_29590.txt"))

featuresets = [(find_features(rev), category) for (rev, category) in documents]

