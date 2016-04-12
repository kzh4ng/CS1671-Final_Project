import operator

class BaseLine:

  def __init__(self, reviews):
    # Determine which season occurs most often in training data
    # and use that season as guess for all test reviews.
	counts = {"winter": 0, "spring": 0, "summer": 0, "fall": 0}
	for review in reviews:
		season = review[0]
		if (season == "winter"):
			counts["winter"] += 1
		elif (season == "spring"):
			counts["spring"] += 1
		elif (season == "summer"):
			counts["summer"] += 1
		elif (season == "fall"):
			counts["fall"] += 1

	self.most_common_season = max(counts.iteritems(), key=operator.itemgetter(1))[0]
	return

  # Classify collection of sentences in parsed_review_sentences (which should be
  # a list of parsed/tokenized sentences for a single review). Return the
  # predicted season for the collection of sentences.
  def classify_all(self, parsed_review_sentences):
    return [self.most_common_season] * len(parsed_review_sentences)
