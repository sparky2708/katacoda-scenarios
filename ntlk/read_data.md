To start working with Python use the following command:

`python`{{execute}}

Let's read the movie reviews that are supplied as a sample corpus within NLTK.

`import data_reader
movie_reviews = data_reader.read_reviews()`{{execute}}

Let's look at a few moview reviews to get a feel of the text

`movie_review_idx = 23
sample_movie_review = movie_reviews[movie_review_idx]
sample_movie_review`{{execute}}
