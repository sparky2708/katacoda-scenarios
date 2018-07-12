from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
import string

def read_review_words():
    documents = []
 
    for category in movie_reviews.categories():
        for fileid in movie_reviews.fileids(category):
            documents.append(movie_reviews.words(fileid), category, movie_reviews.raw(file_id)))

    return documents

def get_review_raw(doc):
    print doc[2]
    
def get_review_sentiment(doc):
    return doc[1]

def get_review_words(doc):
    return doc[0]

def clean_all_words(all_words):
    all_words_clean = []
    stopwords_english = stopwords.words('english')
    
    for word in all_words:
        if word not in stopwords_english and word not in string.punctuation:
            all_words_clean.append(word)
 
    return all_words_clean
