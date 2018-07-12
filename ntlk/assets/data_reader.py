from nltk.corpus import movie_reviews

def read_reviews():
    documents = []
 
    for category in movie_reviews.categories():
        for fileid in movie_reviews.fileids(category):
            documents.append((movie_reviews.words(fileid), category, movie_reviews.raw(fileid)))

    return documents

def get_review_raw(doc):
    return doc[2]
    
def get_review_sentiment(doc):
    return doc[1]

def get_review_words(doc):
    return doc[0]

def get_all_words(reviews):
    all_words = []
    all_words = [word.lower() for word in movie_reviews.words()]
    return all_words
