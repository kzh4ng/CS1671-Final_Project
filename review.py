class Review:

  #__init__ serves as a constructor, review_text is the raw text for the
  #review.
  def __init__(self, review_text):
    self.text = review_text

  #Some method to return the text, incase work must be done on it beforehand,
  #such as parsing. Method may not be necessary.
  #
  #Class methods need the "self"
  #parameter at start of each method, including if there are parameters for the
  #method.
  def sentences(self):
    return self.text
