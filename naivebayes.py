"""
Author: Alex Lederer
Adapted from: logreg.py by Colin Swan
Description: Multinomial or Guassian Naive Bayes based classification of Yelp Reviews,
categorizing reviews into seasons.

"""
import json
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.feature_selection import RFE
from sklearn import metrics
import warnings

class NaiveBayes:

  def __init__(self, reviews, basis):
    corpus = []
    labels = []
    for review in reviews:
    	corpus += [(review[1]["text"])]
    	labels += [(review[0])]

    	# setting variables for the object.
    	self.corpus = corpus
    	self.labels = labels
    	self.reviews = reviews
    	self.basis = basis

    	#print self.corpus[0]
    	#print self.labels[0]

    	self.train() # calling this object's train method.

  def train(self):
  	self.vectorizer = TfidfVectorizer(min_df = 1)
  	X = self.vectorizer.fit_transform(self.corpus)
  	#print "created x"

  	x_names = self.vectorizer.get_feature_names()
  	#print "created x names"
  	y = self.labels

  	#print "created y"

  	if (self.basis == "multinomial"):
  		model = MultinomialNB()
  	elif (self.basis == "gaussian"):
  		model = GaussianNB()

  	# Training the model
  	# supresses log(0) warnings (which occur when some of the classes are not represented at all--i.e. they have a count of zero).
  	with warnings.catch_warnings(): 
  		warnings.simplefilter("ignore")
  		#print "about to fit model"
  		model.fit(X, y)
  		#print "model fitted"
  	self.model = model

  #Classify collection of sentences in parsed_review_sentences (which should be
  #a list of parsed/tokenized sentences for a single review). Return the
  #predicted season for the collection of sentences.
  def classify(self, parsed_review_sentences):
    test_corpus = []
    for sentence in parsed_review_sentences:
      test_corpus += [("", sentence)]

    self.classify_all(test_corpus)

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