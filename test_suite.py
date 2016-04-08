# Importing classes
from baseline import BaseLine
from logreg import LogReg
from review import Review
import argparse
import json
import sys

# Create command line arguments.
parser = argparse.ArgumentParser(description="Uses NLP models to predict the season of a Yelp review.") # TODO: revise so-called project title.
parser.add_argument("-m", required=True, default="baseline", help="the NLP model to be used", action="store", dest="model")
#parser.add_argument("-r", required=True, help="name of training file", action="store", dest="train_file")
#parser.add_argument("-t", required=True, help="name of test file", action="store", dest="test_file")
args = parser.parse_args()

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
model = args.model
if (model == "baseline"):
  model_obj = BaseLine(reviews)

if (model == "logreg"):
  model_obj = LogReg(reviews)
  #testing LogReg class
  model_obj.classify_all(reviews)

else: # put additional models here.
  print("Argument Error: invalid model specified")
  sys.exit()

model_classified = [] #  classifications stored here
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
  model_classified += [(model_obj.classify(json_obj['text']), json_obj)]

correct = 0
index = 0

# Going through every classification baseline made
for classification in model_classified:
  # if the tuple the baseline predicted is correct...
  if classification == reviews[index]:
    correct = correct + 1
  index = index + 1

print (float(correct) / len(reviews)) # print accuracy

