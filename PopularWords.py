import db
import nltk
import pymorphy2
from collections import Counter
import string


def search_words():
    texts = db.select_posts_text()
    stopwords_ru = nltk.corpus.stopwords.words('russian')
    #print(stopwords_ru)
    morph = pymorphy2.MorphAnalyzer()
    words = []
    other_symbols = ('«', '»', '``')
    for text in texts:
        tokenizer = nltk.tokenize.TreebankWordTokenizer()
        tokens = tokenizer.tokenize(text)
        text = " ".join(morph.normal_forms(token)[0] for token in tokens)
        tokens = tokenizer.tokenize(text)
        for token in tokens:
            if token in stopwords_ru or token in string.punctuation or token in other_symbols:
                continue
            else:
                words.append(token)
    words_popularity = Counter(words)
    print(words_popularity)
    print(*words_popularity.most_common(10), sep="\n")
    return words_popularity
