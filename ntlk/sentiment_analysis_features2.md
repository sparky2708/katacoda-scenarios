

Let's create a feature function that will find all words used in positive and negative reviews:

`pos_reviews = []
for fileid in movie_reviews.fileids('pos'):
    words = movie_reviews.words(fileid)
    pos_reviews.append(words)
neg_reviews = []
for fileid in movie_reviews.fileids('neg'):
    words = movie_reviews.words(fileid)
    neg_reviews.append(words)`{{execute}}

Let's define a feature function that checks if the words in the movie review are present in
the word features list:

`def pos_neg_feature(words):
    words_clean = []
    for word in words:
        word = word.lower()
        if word not in stopwords_english and word not in string.punctuation:
            words_clean.append(word)   
    words_dictionary = dict([word, True] for word in words_clean)
    return words_dictionary`{{execute}}
    
Let's now create a feature set:

`pos_reviews_set = []
for words in pos_reviews:
    pos_reviews_set.append((bag_of_words(words), 'pos'))
neg_reviews_set = []
for words in neg_reviews:
    neg_reviews_set.append((bag_of_words(words), 'neg'))`{{execute}}

Let's use the first 200 pos & 200 neg reviews as our test set and the rest as our training set

`train_set = pos_reviews_set[200:] + neg_reviews_set[200:]
print (len(train_set))
test_set = pos_reviews_set[:200] + neg_reviews_set[:200]
print (len(test_set))`{{execute}}
