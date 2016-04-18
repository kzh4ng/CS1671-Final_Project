import unittest
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from unittest.mock import patch
from unittest.mock import Mock
from logreg import LogReg

class testLogReg(unittest.TestCase):

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
    mockV = Mock()
    mockM = Mock()

    test_obj = LogReg([('summer',{'text': "some_text!"})], vectorizer = mockV,
        model = mockM)
    assert mockV.fit_transform.called #vectorizer "trained"
    assert mockM.fit.called #model trained

  
  """
  After object creation, the labels variable should contain a list of labels
  given in the reviews tuple list. This test mocks the vectorizer and model
  and asserts that the expected labels are present after initialization.
  """
  def test_init_labels(self):
    mockV = Mock()
    mockM = Mock()

    test_obj = LogReg([
      ('summer', {'text': "some_text!"}),
      ('winter', {'text': 'some_text2!'})
      ],
      vectorizer = mockV,
      model = mockM
    )
    assert test_obj.labels == ['summer', 'winter']

  """
  After object creation, the corpus variable should contain a list of training
  data given in the reviews tuple list. This test mocks the vectorizer and model
  and asserts that the expected review text is present after initialization.
  """
  def test_init_corpus(self):
    mockV = Mock()
    mockM = Mock()

    test_obj = LogReg([
      ('summer', {'text': "some_text!"}),
      ('winter', {'text': 'some_text2!'})
      ],
      vectorizer = mockV,
      model = mockM
    )
    assert test_obj.corpus == ['some_text!', 'some_text2!']

  """
  After object creation, the review variable should contain the reviews given
  upon initialization. This test mocks the vectorizer and model
  and asserts that the expected reviews are present after initialization.
  """
  def test_init_reviews(self):
    mockV = Mock()
    mockM = Mock()

    test_obj = LogReg([
      ('summer', {'text': "some_text!"}),
      ('winter', {'text': 'some_text2!'})
      ],
      vectorizer = mockV,
      model = mockM
    )
    assert test_obj.reviews == [
      ('summer', {'text': "some_text!"}),
      ('winter', {'text': 'some_text2!'})
      ]




if __name__ == '__main__':
  unittest.main()


