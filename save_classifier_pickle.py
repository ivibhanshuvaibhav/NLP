import nltk
import random
from nltk.corpus import movie_reviews
import pickle

documents = []

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = []

for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)

word_feature = list(all_words.keys()[:3000])

def find_features(document):
    words = set(document)
    features = {}
    for w in word_feature:
        features[w] = (w in words)

    return features

featuresets = [(find_features(rev), category) for (rev, category) in documents]

random.shuffle(featuresets)

training_set = featuresets[:1900]
testing_set = featuresets[1900:]

classifier = nltk.NaiveBayesClassifier.train(training_set)
print "Naive Bayes algorithm accuracy percent", (nltk.classify.accuracy(classifier, testing_set)) * 100.0
classifier.show_most_informative_features(15)

# saving classifier to pickle file so that we do not have to train our classifier every time we use it

save_classifier = open("naivebayes.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()