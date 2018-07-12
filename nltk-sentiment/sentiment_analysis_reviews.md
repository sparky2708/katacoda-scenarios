
Let's read the movie reviews that are supplied as a sample corpus within NLTK.
Each movie review is marked with a 'pos' or 'neg' rating:

`from nltk.corpus import movie_reviews 
print (len(movie_reviews.fileids())) 
print (movie_reviews.categories())
print (len(movie_reviews.fileids('pos')))
print (len(movie_reviews.fileids('neg')))`{{execute}}

Import all the reviews into an array of tuples of <words, category, raw_review>:

`import data_reader
reviews = data_reader.read_reviews()`{{execute}}

Let's look at a few movie reviews to get a feel of the text

`import data_reader
movie_review_idx = 123
print(data_reader.get_review_sentiment(reviews[movie_review_idx]))
print(data_reader.get_review_raw(reviews[movie_review_idx]))`{{execute}}


