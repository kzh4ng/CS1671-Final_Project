class BaseLine:

  def __init__(self, reviews):
    #Ignoring the reviews for baseline, but in actual models use
    #the (category, review_json) tuples in the reviews list to train the model!
    pass

  #Classify collection of sentences in parsed_review_sentences (which should be
  #a list of parsed/tokenized sentences for a single review). Return the
  #predicted season for the collection of sentences.
  def classify(self, parsed_review_sentences):
    return "summer"
