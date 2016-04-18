"""
Author: Colin Swan
Description: Logistic Regression based classification of Yelp Reviews,
categorizing reviews into seasons.

"""
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE

class LogReg:

  def __init__(
      self,
      reviews,
      vectorizer = TfidfVectorizer(min_df = 1),
      model = LogisticRegression()
      ):
    self.model = model
    self.vectorizer = vectorizer

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
    x_names = self.vectorizer.get_feature_names()
    y = self.labels

    #Training the model
    self.model.fit(X, y)


  def train(self, reviews):
    #Vectorizing using TfidfVectorizer, which takes a count of all the words
    #and then does some extra work to eliminate ones that are too common among
    #all labels to be worth while.
    
    #adding to the corpus and to the labels for this object
    for review in reviews:
      self.corpus += [review[1]["text"]]
      self.labels += [review[0]]

    X = self.vectorizer.fit_transform(self.corpus)
    x_names = self.vectorizer.get_feature_names()
    y = self.labels

    #Training the model
    self.model.fit(X, y)

  #Classify collection of sentences in parsed_review_sentences (which should be
  #a list of parsed/tokenized sentences for a single review). Return the
  #predicted season for the collection of sentences.
  def classify(self, parsed_review_sentences):
    test_corpus = []
    for sentence in parsed_review_sentences:
      test_corpus += [("", sentence)]

    self.classify_all(test_corpus)
    return 'summer' #TODO: do we need this or should it be removed?

  #This is mainly a test method while I work on some implementation details
  def classify_all(self, all_test_data):
    test_corpus = []
    y = []
    for review in all_test_data:
      test_corpus += [review[1]['text']]
      y += [review[0]]
    
    #Used transform instead of fit_transform
    #for test data so number of features will match
    X = self.vectorizer.transform(test_corpus)
    results = self.model.predict(X)
    return results

  #Work in progress, may be able to use RFE
  #to determine most useful words for classifcation
  def vocabulary(self, all_test_data):
    test_corpus = []
    y = []
    for review in all_test_data:
      test_corpus += [review[1]['text']]
      y += [review[0]]

    X = self.vectorizer.transform(test_corpus)
    results = self.model.predict(X)
    selector = RFE(self.model, 100, 1)
    sel_result = selector.fit(X, y)
    print(selector.transform(X))
