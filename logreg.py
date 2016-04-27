"""
Author: Colin Swan
Description: Logistic Regression based classification of Yelp Reviews,
categorizing reviews into seasons.

"""
import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.linear_model import RandomizedLogisticRegression
from sklearn.feature_selection import RFE
from sklearn.feature_selection import f_classif, SelectKBest

class LogReg:

  """
  Initialization sets the objects model, vectorizer, labels, and corpus
  variables. Initialization also performs the initial training for the model
  and vectorizer using the given reviews.
  """
  def __init__(
      self,
      reviews,
      vectorizer = TfidfVectorizer(max_df = 1, ngram_range = (1,3)),
      model = LinearSVC()
      ):
    self.model = model
    self.vectorizer = vectorizer
    self.selector = RFE(self.model, n_features_to_select = 10000, step = 1000, verbose = 100)

    corpus = []
    labels = []
    for review in reviews:
      corpus += [review[1]["text"]]
      labels += [review[0]]

    #setting variables for the object
    self.corpus = corpus
    self.labels = labels
    self.reviews = reviews

    X = self.vectorizer.fit_transform(self.corpus)
    self.feature_names = self.vectorizer.get_feature_names()
    y = self.labels
    num_labels = []
    for i in self.labels:
      if i == "summer":
        num_labels.append(0)
      if i == "winter":
        num_labels.append(1)
      if i == "fall":
        num_labels.append(2)
      if i == "spring":
        num_labels.append(3)

    #Training the model
    X_new = self.selector.fit_transform(X,self.labels)
    self.model.fit(X_new, self.labels)


  """
  Trains up the vectorizer and model with the given reviews.
  """
  def train(self, reviews):
    #Vectorizing using TfidfVectorizer, which takes a count of all the words
    #and then does some extra work to eliminate ones that are too common among
    #all labels to be worth while.

    #adding to the corpus and to the labels for this object
    for review in reviews:
      self.corpus += [review[1]["text"]]
      self.labels += [review[0]]

    X = self.vectorizer.fit_transform(self.corpus)
    self.feature_names = self.vectorizer.get_feature_names()
    self.feature_names = np.asarray(feature_names)
    y = self.labels

    #Training the model
    X_new = SelectKBest(chi2, k=100).fit_transform(X, y)
    self.model.fit(X_new, y)

  """
  Classifies all the test data given, and returns a list of the
  classifications, which each index corresponding to the index of a review in
  the given test data.
  """
  def classify_all(self, all_test_data):
    test_corpus = []
    y = []
    for review in all_test_data:
      test_corpus += [review[1]['text']]
      y += [review[0]]

    #Used transform instead of fit_transform
    #for test data so number of features will match
    X = self.vectorizer.transform(test_corpus)
    X_new = self.selector.transform(X)
    results = self.model.predict(X_new)
    categories = ["spring", "summer", "fall", "winter"]
    for i, category in enumerate(categories):
      top10 = np.argsort(self.model.coef_[i])[-10:]
      print(top10)
      for j in top10:
        print("%s: %s" % (category, "".join(self.feature_names[j])))
    return results

  """
  TODO
  Returns the vocabulary used to classify the given test data, with the
  highested ranked (that is, most indicative) words / features listed first.
  """
  def vocabulary(self, all_test_data, selector = None):

    #Can't create RFE(self.model, 100, 1) as default for selector directly
    #self must be defined for this scope first.
    if selector == None:
      selector = RFE(self.model, 100, 1)
    test_corpus = []
    y = []
    for review in all_test_data:
      test_corpus += [review[1]['text']]
      y += [review[0]]

    X = self.vectorizer.transform(test_corpus)
    results = self.model.predict(X)
    sel_result = selector.fit(X, y)
    return selector.transform(X)
