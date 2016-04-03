#importing classes
from baseline import BaseLine
from review import Review
import json

reviews = [] #  creating a list of reviews to classify

#  Reading training data into reviews list
with open("spring-pittsburgh-training.json") as json_file:
  for line in json_file:
    json_obj = json.loads(line)
    reviews += [('spring',json_obj)]

with open("summer-pittsburgh-training.json") as json_file:
  for line in json_file:
    json_obj = json.loads(line)
    reviews += [('summer',json_obj)]

with open("fall-pittsburgh-training.json") as json_file:
  for line in json_file:
    json_obj = json.loads(line)
    reviews += [('fall',json_obj)]

with open("winter-pittsburgh-training.json") as json_file:
  for line in json_file:
    json_obj = json.loads(line)
    reviews += [('winter',json_obj)]

#  Creating model objects
base_obj = BaseLine(reviews)
baseline_classified = [] #  classifications stored here

reviews = [] #  resetting reviews list to save memory


#  Reading test data into reviews list
with open("spring-pittsburgh.json") as json_file:
  for line in json_file:
    json_obj = json.loads(line)
    reviews += [('spring',json_obj)]

with open("summer-pittsburgh.json") as json_file:
  for line in json_file:
    json_obj = json.loads(line)
    reviews += [('summer',json_obj)]

with open("fall-pittsburgh.json") as json_file:
  for line in json_file:
    json_obj = json.loads(line)
    reviews += [('fall',json_obj)]

with open("winter-pittsburgh.json") as json_file:
  for line in json_file:
    json_obj = json.loads(line)
    reviews += [('winter',json_obj)]

for __, json_obj in reviews:
  baseline_classified += [(base_obj.classify(json_obj['text']), json_obj)]

correct = 0
index = 0

#Going through every classification baseline made
for classification in baseline_classified:
  #if the tuple the baseline predicted is correct...
  if classification == reviews[index]:
    correct = correct + 1
  index = index + 1

#print accuracy
print (float(correct) / len(reviews))

