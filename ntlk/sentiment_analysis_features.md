
Let's create a feature function that will use the top 2,000 words found in all the reviews:

Most Common Words:

`print (len(all_words_freq))
most_common_words = all_cleaned_words_freq.most_common(2000)
print (most_common_words[:10])`{{execute}}

Least Common Words:

`print (most_common_words[1990:])`{{execute}}

Let's define a feature function that checks if the words in the movie review are present in
the word features list:

`def document_features(document):
    document_words = set(document)
    features = {}
    for word in all_cleaned_words:
        features["contains(%s)" % word[0]] = (word[0] in document_words)
    return features`{{execute}}
    
Let's now create a feature set:

`feature_set = [(document_features(doc), category) for (doc, category, raw) in reviews]
print (feature_set[0])`{{execute}}

Let's use the first 400 as our training set and the remainder as our training set

`train_set = feature_set[:400]
print (len(train_set))
test_set = feature_set[400:]
print (len(test_set))`{{execute}}

Train the classifier:

`from nltk import NaiveBayesClassifier
classifier = NaiveBayesClassifier.train(train_set)`{{execute}}



