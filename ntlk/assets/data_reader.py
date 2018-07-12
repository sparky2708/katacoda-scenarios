from nltk.corpus import movie_reviews

def read_reviews():
    documents = []
 
    for category in movie_reviews.categories():
        for fileid in movie_reviews.fileids(category):
            documents.append((movie_reviews.words(fileid), category))

    return documents
