import unittest
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from unittest.mock import patch
from unittest.mock import Mock
from logreg import LogReg

class testLogReg(unittest.TestCase):

  def setUp(self):
    self.mockV = Mock()
    self.mockM = Mock()

    self.test_obj = LogReg([
      ('summer', {'text': "some_text!"}),
      ('winter', {'text': 'some_text2!'})
      ],
      vectorizer = self.mockV,
      model = self.mockM
    )


  """
  After object creation, a LogReg object should have:
    a TfidVectorizer named vectorizer
    a list of labels named labels
    a LogisticRegression model named model.

  model should have called the "fit" method to ensure that the initial model
  has been trained.

  vectorizer should have called the fit_transform method to create a vector for
  the model.fit method.

  This test uses mocks to test that the initial training methods are being
  called without actually performing the associated operations.
  """

  def test_init_trained(self):
    assert self.mockV.fit_transform.called #vectorizer "trained"
    assert self.mockM.fit.called #model trained

  """
  After object creation, the labels variable should contain a list of labels
  given in the reviews tuple list. This test mocks the vectorizer and model
  and asserts that the expected labels are present after initialization.
  """
  def test_init_labels(self):
    assert self.test_obj.labels == ['summer', 'winter']

  """
  After object creation, the corpus variable should contain a list of training
  data given in the reviews tuple list. This test mocks the vectorizer and model
  and asserts that the expected review text is present after initialization.
  """
  def test_init_corpus(self):
    assert self.test_obj.corpus == ['some_text!', 'some_text2!']

  """
  After object creation, the review variable should contain the reviews given
  upon initialization. This test mocks the vectorizer and model
  and asserts that the expected reviews are present after initialization.
  """
  def test_init_reviews(self):
    assert self.test_obj.reviews == [
      ('summer', {'text': "some_text!"}),
      ('winter', {'text': 'some_text2!'})
      ]

  """
  After calling the train method the corpus should be expanded to include the
  text for those reviews that are passed into the method. Test mocks the
  vectorizer and model created in the initialization of the object and checks
  to see that the new reviews are parsed and saved correctly in the corpus
  variable.
  """
  def test_train_corpus(self):
    #setting initial corpus so we don't rely on initialization setting it
    #correctly
    self.test_obj.corpus = ["Hello world!"]
    self.test_obj.train([('summer', {'text': 'some_text!'})])
    assert self.test_obj.corpus == ["Hello world!", "some_text!"]

  """
  After calling the train method the labels should be expanded to include the
  text for those reviews that are passed into the method. Test mocks the
  vectorizer and model created in the initialization of the object and checks
  to see that the new reviews are parsed and saved correctly in the labels
  variable.
  """
  def test_train_labels(self):
    #setting initial labels so we don't rely on initialization setting it
    #correctly
    self.test_obj.labels = ["winter"]
    self.test_obj.train([('fall', {'text': 'some_text!'})])
    assert self.test_obj.labels == ["winter", "fall"]

  """
  After calling the train method the labels should be expanded to include the
  text for those reviews that are passed into the method. Test mocks the
  vectorizer and model created in the initialization of the object and checks
  to see that the new reviews are parsed and saved correctly in the labels
  variable.
  """
  def test_train_trained(self):
    #Mocking the return value for fit_transform, since that result is passed to
    #the models' fit method.
    self.mockV.fit_transform.return_value = ["THIS IS A VECTOR!"]

    #Setting initial labels and corpus
    self.test_obj.labels = ["winter"]
    self.test_obj.corpus = ["Hello world!"]

    self.test_obj.train([('fall', {'text': 'some_text!'})])
    self.mockV.fit_transform.assert_called_with(["Hello world!", "some_text!"])
    self.mockM.fit.assert_called_with(
        ["THIS IS A VECTOR!"],
        ["winter", "fall"]
        )

  def test_classify_all(self):


if __name__ == '__main__':
  unittest.main()


