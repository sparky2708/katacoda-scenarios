
Let's create a feature function that will use the top 2,000 words found in all the reviews:

Most Common Words:

`print (len(all_words_freq))
most_common_words = all_cleaned_words_freq.most_common(2000)
print (most_common_words[:10])`{{execute}}

Least Common Words:

`print (most_common_words[1990:])`{{execute}}

Let's define a feature function that checks if the words in the movie review are present in the word features list 
Since the movie reviews have already been lowercased in the corpus we will ignore converting all the words to lowercase but if provide custom sentences to classify we have to remember to keep them in lowercase:

`def document_features(document):
    document_words = set(document)
	word_features = [item[0] for item in most_common_words]
    features = {}
    for word in word_features:
        features["contains(%s)" % word] = (word in document_words)
    return features
	`{{execute}}
    
Let's now create a feature set:

`feature_set = [(document_features(doc), category) for (doc, category, raw) in reviews]
print (feature_set[0])`{{execute}}

Let's shuffle the features to mix the positive and negative reviews
so we don't test on a disproportionate amount of positive or negative reviews. Still could happen by chance.

`from random import shuffle 
shuffle(feature_set)`{{execute}}

From the shuffled list, we will use the first 400 movie reviews as our test set and the remainder as our training set:

`test_set = feature_set[:400]
print (len(test_set))
train_set = feature_set[400:]
print (len(train_set))`{{execute}}

