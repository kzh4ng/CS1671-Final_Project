import math
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn import neighbors
import numpy as np
class knn:
    def __init__(self, reviews, target):
        self.vectorizer = CountVectorizer(ngram_range=(1,2), min_df=1)
        corpus = []
        thing = np.asarray(target)
        for __, json_obj in reviews:
            corpus.append(json_obj['text'])
        self.X = self.vectorizer.fit_transform(corpus)
        self.estimate = KNeighborsClassifier(n_neighbors=150)
        self.estimate.fit(self.X,thing)
        pass

    def classify_all(self, parsed_review_sentences):
        model_classified = []
        for __, json_obj in parsed_review_sentences:
            model_classified += [self.classify(json_obj['text'])]
        return model_classified


    def classify(self, sentence):
        L = self.vectorizer.transform([sentence]).toarray()
        value = self.estimate.predict(L)
        if (value == 0):
            return "spring"
        elif (value == 1):
            return "summer"
        elif (value == 2):
            return "fall"
        elif (value == 3):
            return "winter"

