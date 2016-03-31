#importing classes
from baseline import BaseLine
from review import Review

#creating object for baseline model
base_obj = BaseLine() #Models will probably take training data here.
test_review = Review("Went to get icecream here yesterday. It was very"
    + "beautiful! We sat outside on their patio and watched the clouds"
    + "roll by while we ate. Lovely experience.")
test_2 = Review("Lame winter review")

#creating a list of reviews to classify
parsed_reviews = [test_review, test_2]

#empty list that will contain baseline's classification of each review.
baseline_classified = []

#list of expected (classification, review) tuples.
expected_classifications = [('summer', test_review), ('winter', test_2)]

for review in parsed_reviews:
  baseline_classified += [(base_obj.classify(review.sentences), review)]

correct = 0
index = 0

#Going through every classification baseline made
for classification in baseline_classified:
  #if the tuple the baseline predicted is correct...
  if classification == expected_classifications[index]:
    correct = correct + 1
  index = index + 1

#print accuracy
print(correct / len(expected_classifications))

