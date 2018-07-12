
Let's read the movie reviews that are supplied as a sample corpus within NLTK.
Each movie review is marked with a 'pos' or 'neg' rating:

from nltk.corpus import movie_reviews 
 
`print (len(movie_reviews.fileids())) 
print (movie_reviews.categories())
print (len(movie_reviews.fileids('pos')))
print (len(movie_reviews.fileids('neg')))`{{execute}}



`import data_reader
movie_reviews = data_reader.read_reviews()`{{execute}}

Let's look at a few movie reviews to get a feel of the text

`movie_review_idx = 123
sample_movie_review = movie_reviews[movie_review_idx]
sample_movie_review`{{execute}}
