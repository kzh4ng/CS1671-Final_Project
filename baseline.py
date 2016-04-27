import operator

class BaseLine:

  def __init__(self, reviews, categories):
    # Determine which season occurs most often in training data
    # and use that season as guess for all test reviews.
    counts = categories
    for review in reviews:
      counts[review[0]] += 1
    print(counts)

    common_count, common_cat = max((x, y) for y, x in counts.items())
    self.most_common_cat = common_cat
    return

  # Classify collection of sentences in parsed_review_sentences (which should be
  # a list of parsed/tokenized sentences for a single review). Return the
  # predicted season for the collection of sentences.
  def classify_all(self, parsed_review_sentences):
    return [self.most_common_cat] * len(parsed_review_sentences)
