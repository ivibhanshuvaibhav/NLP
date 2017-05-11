from nltk.corpus import wordnet

syn = wordnet.synsets("program")

for i in syn:
    print i.name()
    print i.lemmas()
    print i.lemmas()[0].name()
    print i.definition()
    print i.examples()
    print ""


synonym = []
antonym = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonym.append(l.name())
        if l.antonyms():
            antonym.append(l.antonyms()[0].name())

print set(synonym)
print set(antonym)


w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('boat.n.01')
print(w1.wup_similarity(w2))


w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('car.n.01')
print(w1.wup_similarity(w2))


w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('cat.n.01')
print(w1.wup_similarity(w2))