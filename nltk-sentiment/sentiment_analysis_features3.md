Let's try to create a unigram and bi-gram classifier to see if we improve classification:

Again we'll be using positive and negative reviews:

Positive Reviews:

`from nltk.corpus import movie_reviews 
pos_reviews = []
for fileid in movie_reviews.fileids('pos'):
    words = movie_reviews.words(fileid)
    pos_reviews.append(words)`{{execute}}

Negative Reviews:

`from nltk.corpus import movie_reviews 
neg_reviews = []
for fileid in movie_reviews.fileids('neg'):
    words = movie_reviews.words(fileid)
    neg_reviews.append(words)`{{execute}}

First we create a feature extractor for 1-grams
`from nltk.corpus import stopwords
def unigram_feature_extractor(words):  
	stopwords_to_use = stopwords.words('english')
    cleaned_words = data_reader.clean_all_words(words, stopwords_to_use)
    words_dictionary = dict([word, True] for word in words)    
    return words_dictionary
	`{{execute}}

Then we create a feature extractor for bi-grams
`import data_reader
from nltk import ngrams
from nltk.corpus import stopwords
def ngram_feature_extractor(words, n=2):
    acceptable_stop_words = ['above', 'below', 'off', 'over', 'under', 'more', 'most', 'such', 'no', 'nor', 'not', 'only', 'so', 'than', 'too', 'very', 'just', 'but']
    stopwords_to_use = set(stopwords.words('english')) - set(acceptable_stop_words)
    cleaned_words = data_reader.clean_all_words(words, stopwords_to_use)    
    words_ng = []
    for item in iter(ngrams(words, n)):
        words_ng.append(item)
    words_dictionary = dict([word, True] for word in words_ng)    
    return words_dictionary
	`{{execute}}

Let's put the 2 feature extractors that we created for 1-grams and 2-grams above into a single feature extractor that we will use to classify a review

`from nltk import ngrams
def document_features(words, n=2):
    unigram_features = unigram_feature_extractor(words)
    bigram_features = ngram_feature_extractor(words)
    all_features = unigram_features.copy()
    all_features.update(bigram_features)
    return all_features
	`{{execute}}
	
Now, as with other classification ideas, let's create a feature set for positive and for negative reviews:

`pos_reviews_set = []
for words in pos_reviews:
    pos_reviews_set.append((document_features(words), 'pos'))
	`{{execute}}
	
`neg_reviews_set = []
for words in neg_reviews:
    neg_reviews_set.append((document_features(words), 'neg'))
	`{{execute}}
	
Let's use the first 200 positive & 200 negative reviews as our test set and the rest as our training set

`test_set = pos_reviews_set[:200] + neg_reviews_set[:200]
print (len(test_set))
train_set = pos_reviews_set[200:] + neg_reviews_set[200:]
print (len(train_set))
`{{execute}}

