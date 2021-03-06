Let's train the classifier:

`from nltk import classify 
from nltk import NaiveBayesClassifier
classifier = NaiveBayesClassifier.train(train_set)
accuracy = classify.accuracy(classifier, test_set)
print (accuracy)`{{execute}}

Testing the classifier to see how well it works with some reviews:

**NEGATIVE REVIEW**: `my_review = "I hated the film. It was a disaster. Poor direction, bad acting."`{{execute}}
**POSITIVE REVIEW**: `my_review = "It was a wonderful and amazing movie. I loved it. Best direction, good acting."`{{execute}}

Let's see what happens when we ask the classifier if the sample review is positive or negative:

`from nltk.tokenize import word_tokenize
my_review_tokens = word_tokenize(my_review)
my_review_set = document_features(my_review_tokens)
print (classifier.classify(my_review_set))`{{execute}}

Let's look at the probabilities the classifier got when it decided on a classification:

`prob_result = classifier.prob_classify(my_review_set)
print (prob_result) 
print (prob_result.max()) 
print (prob_result.prob("neg")) 
print (prob_result.prob("pos"))`{{execute}}

Let's look at the most informative features that the classifier considers when distinguishing 
between a positive and negative review:

`classifier.show_most_informative_features(20)`{{execute}}
