import db
import nltk
import pymorphy2
from collections import Counter
import string
import re


def search_words():
    texts, count = db.select_posts_text()
    posts_percent = int((count / 100) * 30)
    stopwords_ru = nltk.corpus.stopwords.words('russian')
    morph = pymorphy2.MorphAnalyzer()
    words = []
    for text in texts[:posts_percent]:
        tokenizer = nltk.tokenize.TreebankWordTokenizer()
        tokens = tokenizer.tokenize(text)
        text = " ".join(morph.normal_forms(token)[0] for token in tokens)
        tokens = tokenizer.tokenize(text)
        for token in tokens:
            if token in stopwords_ru:
                continue
            else:
                if re.search(r'[^а-яА-Я]', token):
                    continue
                else:
                    if len(token) >= 5:
                        words.append(token)
    words_popularity = Counter(words)
    # print(words_popularity)
    print(*words_popularity.most_common(10), sep="\n")
    return words_popularity


search_words()