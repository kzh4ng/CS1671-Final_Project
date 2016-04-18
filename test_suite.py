# Importing classes
from baseline import BaseLine
from logreg import LogReg
from naivebayes import NaiveBayes
from review import Review
import argparse
import json
import sys

# Create command line arguments.
parser = argparse.ArgumentParser(description="Uses NLP models to predict the season of a Yelp review.") # TODO: revise so-called project title.
parser.add_argument("-m", required=True, default="baseline", help="the NLP model to be used", action="store", dest="model")
parser.add_argument("-c", required=True, help="the classifier for datasets, i.e. city name", action="store", dest="classifier")
args = parser.parse_args()


reviews = [] #  creating a list of reviews to classify
classifier = args.classifier.lower() # stores file classifier (i.e. "pittsburgh")

#  Reading training data into reviews list
with open("spring-"+classifier+"-training.json") as json_file:
  for line in json_file:
    json_obj = json.loads(line)
    reviews += [('spring',json_obj)]

with open("summer-"+classifier+"-training.json") as json_file:
  for line in json_file:
    json_obj = json.loads(line)
    reviews += [('summer',json_obj)]

with open("fall-"+classifier+"-training.json") as json_file:
  for line in json_file:
    json_obj = json.loads(line)
    reviews += [('fall',json_obj)]

with open("winter-"+classifier+"-training.json") as json_file:
  for line in json_file:
    json_obj = json.loads(line)
    reviews += [('winter',json_obj)]

#  Creating model objects
model = args.model
if (model == "baseline"):
  model_obj = BaseLine(reviews)

elif (model == "logreg"):
  model_obj = LogReg(reviews)

elif (model == "multinomialNB"):
  model_obj = NaiveBayes(reviews, "multinomial")

elif (model == "gaussianNB"):
  model_obj = NaiveBayes(reviews, "gaussian")

else: # put additional models here.
  print("Argument Error: invalid model specified")
  sys.exit()

model_classified = [] #  classifications stored here
reviews = [] #  resetting reviews list to save memory

#  Reading test data into reviews list
with open("spring-"+classifier+".json") as json_file:
  for line in json_file:
    json_obj = json.loads(line)
    reviews += [('spring',json_obj)]

with open("summer-"+classifier+".json") as json_file:
  for line in json_file:
    json_obj = json.loads(line)
    reviews += [('summer',json_obj)]

with open("fall-"+classifier+".json") as json_file:
  for line in json_file:
    json_obj = json.loads(line)
    reviews += [('fall',json_obj)]

with open("winter-"+classifier+".json") as json_file:
  for line in json_file:
    json_obj = json.loads(line)
    reviews += [('winter',json_obj)]

"""
for __, json_obj in reviews:
  model_classified += [(model_obj.classify(json_obj['text']), json_obj)]
"""

#Made more sense in my case to just pass all the test reviews at once,
#since the LogisiticRegression classify method expects all of the test corpus
#at once. I imagine the other models will work in a similar manner, but if not
#we can add more logic.
model_classified = model_obj.classify_all(reviews)

correct = 0
index = 0

# Going through every classification baseline made
for classification in model_classified:
  # if the tuple the baseline predicted is correct...
  if classification == reviews[index][0]:
    correct = correct + 1
  index = index + 1

print (float(correct) / len(reviews)) # print accuracy

