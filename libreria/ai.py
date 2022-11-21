import csv
import string

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer


spam_or_ham = pd.read_csv("spam.csv", encoding='latin-1')[["v1", "v2"]]
spam_or_ham.columns = ["label", "text"]
spam_or_ham.head()

spam_or_ham["label"].value_counts()

punctuation = set(string.punctuation)
def tokenize(sentence):
    tokens = []
    for token in sentence.split():
        new_token = []
        for character in token:
            if character not in punctuation:
                new_token.append(character.lower())
        if new_token:
            tokens.append("".join(new_token))
    return tokens

spam_or_ham.head()["text"].apply(tokenize)

demo_vectorizer = CountVectorizer(
    tokenizer = tokenize,
    binary = True
)