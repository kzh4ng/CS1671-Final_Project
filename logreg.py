"""
Author: Colin Swan
Description: Logistic Regression based classification of Yelp Reviews,
categorizing reviews into seasons.

"""
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

class LogReg:

  def __init__(self, reviews):
    corpus = []
    labels = []
    for review in reviews:
      corpus += [review[1]["text"]]
      labels += [review[0]]

    #setting variables for the object
    self.corpus = corpus
    self.labels = labels

    self.reviews = reviews
    #calling this object's train method
    self.train()

  def train(self):
    #Vectorizing using TfidfVectorizer, which takes a count of all the words
    #and then does some extra work to eliminate ones that are too common among
    #all labels to be worth while.
    vectorizer = TfidfVectorizer(min_df = 1)
    X = vectorizer.fit_transform(self.corpus)
    y = self.labels

    model = LogisticRegression()
    #Training the model
    model.fit(X, y)
    self.model = model


  #Classify collection of sentences in parsed_review_sentences (which should be
  #a list of parsed/tokenized sentences for a single review). Return the
  #predicted season for the collection of sentences.
  def classify(self, parsed_review_sentences):
    test_corpus = []
    for sentence in parsed_review_sentences:
      test_corpus += [sentence]

    return 'summer'

  #This is mainly a test method while I work on some implementation details
  def classify_all(self, all_test_data):
    test_corpus = []
    y = []
    for review in all_test_data:
      test_corpus += [review[1]]
      y += [review[0]]

    vectorizer = TfidfVectorizer(min_df = 1)
    X = vectorizer.fit_transform(self.corpus)
    results = self.model.predict(X)
    print("results: " )
    print(results)

