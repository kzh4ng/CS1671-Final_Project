"""
Author: Kevin Zhang
Description: Topic Modeling with Latent Dirichlet Allocation and logistic regression
for categorizing Yelp reviews

"""

import json
import numpy as np
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from stop_words import get_stop_words
from gensim import corpora, models
from sklearn.linear_model import LogisticRegression
import gensim
import warnings

class TopicModel:

  def __init__(self, reviews):
    corpus = []
    labels = []
    for review in reviews:
      corpus += [(review[1]["text"])]     #access text field in JSON object
      labels += [(review[0])]             #access season

      # setting variables for the object.
    self.corpus = corpus
    self.labels = labels
    self.reviews = reviews

    self.train() # calling this object's train method.

  def train(self):

    
    review_set = self.corpus
    texts = []
    # tokenize review set
    texts = self.tokenize(review_set)
    # turn our tokenized documents into a id <-> term dictionary
    dictionary = corpora.Dictionary(texts)
    self.dictionary = dictionary
    # convert tokenized documents into a document-term matrix
    corpus = [dictionary.doc2bow(text) for text in texts]
    
    # generate LDA model
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=50, id2word = dictionary, passes=30)   
    self.ldamodel = ldamodel

    topics = []
    for dist in corpus:
      tup = self.ldamodel.get_document_topics(dist,0)
      values = [x[1] for x in tup]
      topics.append(values)


    log_reg = LogisticRegression()
    log_reg.fit(topics, self.labels)
    self.log_reg = log_reg

  def classify_all(self, all_test_data):
    test_corpus = []
    for review in all_test_data:
      test_corpus += [review[1]['text']]

    #tokenize, remove stop words, and stem tokens for each review
    texts = self.tokenize(test_corpus)
    #create id - term dictionary
    corpus = [self.dictionary.doc2bow(text) for text in texts]

    test_topics = []
    for dist in corpus:
      tup = self.ldamodel.get_document_topics(dist,0)
      values = [x[1] for x in tup]
      test_topics.append(values)

    results = self.log_reg.predict(test_topics)
    return results

  def tokenize(self, reviews):
    texts = []
    tokenizer = RegexpTokenizer(r'\w+')
    en_stop = get_stop_words('en')
    p_stemmer = PorterStemmer()

    # loop through document list
    for i in reviews:
      # clean and tokenize document string
      raw = i.lower()
      tokens = tokenizer.tokenize(raw)
      # remove stop words from tokens
      stopped_tokens = [i for i in tokens if not i in en_stop]
      # stem tokens
      stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
      # add tokens to list
      texts.append(stemmed_tokens)

    return texts

    
  #Classify collection of sentences in parsed_review_sentences (which should be
  #a list of parsed/tokenized sentences for a single review). Return the
  #predicted season for the collection of sentences.