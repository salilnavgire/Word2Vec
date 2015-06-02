from gensim import models
from gensim import corpora
from gensim.models import Word2Vec
import pandas as pd
import numpy as np
from nltk.corpus import brown, movie_reviews, treebank
import string
import csv
import unicodedata
import sys
from collections import Counter
import pickle
import re
import cPickle
from nltk.corpus import stopwords
stoplist = set(stopwords.words('english'))


path = '/Users/salilnavgire/Downloads/irene_comments.csv'


def read_data(path):
    data = []
    with open(path, 'rb') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            data.append(row)
    return data[0]


def prepare_data(data):
    new_data = []
    for i, res in enumerate(data):
        try:
            s = re.sub('[^a-zA-Z0-9\n\.]', ' ', res)
            new = [x.lower() for x in s.split() if x not in stoplist]
            if i % 10000 == 0:
                print i
            new_data.append(new)
        except IndexError:
            pass
    return new_data


if __name__ == '__main__':
    data = read_data(path)
    print len(data)
    new_data = prepare_data(data)
    print len(new_data)