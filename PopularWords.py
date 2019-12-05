import db
import nltk
import pymorphy2
from collections import Counter
import string
import re


def search_words():
    texts = db.select_posts_text()
    stopwords_ru = nltk.corpus.stopwords.words('russian')
    morph = pymorphy2.MorphAnalyzer()
    words = []
    for text in texts:
        tokenizer = nltk.tokenize.TreebankWordTokenizer()
        tokens = tokenizer.tokenize(text)
        text = " ".join(morph.normal_forms(token)[0] for token in tokens)
        tokens = tokenizer.tokenize(text)
        for token in tokens:
            if token in stopwords_ru or token in string.punctuation:
                continue
            else:
                if re.search(r'[^а-яА-Я]', token):
                    print("Не подходящее слово")
                else:
                    words.append(token)
    words_popularity = Counter(words)
    # print(words_popularity)
    # print(*words_popularity.most_common(10), sep="\n")
    return words_popularity


search_words()