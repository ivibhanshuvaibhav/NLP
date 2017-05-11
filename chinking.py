from nltk import pos_tag, RegexpParser
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer, word_tokenize

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sentence_tokenizer = PunktSentenceTokenizer(train_text)

tokenized_data = custom_sentence_tokenizer.tokenize(sample_text)

for i in tokenized_data:

    words = word_tokenize(i)
    tagged = pos_tag(words)

    chunkGram = r"""Chunk: {<.*>+}
                                }<VB.?|IN|DT|TO>+{"""
    chunkParser = RegexpParser(chunkGram)
    chunked = chunkParser.parse(tagged)
    chunked.draw()