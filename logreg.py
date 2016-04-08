import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

class LogReg:

  def __init__(self, reviews):
    #Ignoring the reviews for baseline, but in actual models use
    #the (category, review_json) tuples in the reviews list to train the model!
    corpus = []
    labels = []
    for review in reviews:
      corpus += [review[1]["text"]]
      labels += [review[0]]

    self.corpus = corpus
    self.labels = labels

    self.reviews = reviews
    self.train()

  def train(self):
    vectorizer = TfidfVectorizer(min_df = 1)
    X = vectorizer.fit_transform(self.corpus)
    y = self.labels

    model = LogisticRegression()
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

