"""
Part-of-speech constants
ADJ, ADV, NOUN, VERB = 'a', 'r', 'n', 'v'
POS_LIST = [NOUN, VERB, ADJ, ADV]
"""

from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize

lemmatizer = WordNetLemmatizer()

word = word_tokenize("cacti better python ran geese rocks cats best")
hi = pos_tag(word)
print hi

for i in hi:

    pos = ''
    tagged_pos = i[1]
    word = i[0]

    if tagged_pos[0] == 'R':
        pos = 'r'

    elif tagged_pos[0] == 'N':
        pos = 'n'

    elif tagged_pos[0] == 'V':
        pos = 'v'

    elif tagged_pos[0] == 'J':
        pos = 'a'

    print lemmatizer.lemmatize(word, pos=pos)
