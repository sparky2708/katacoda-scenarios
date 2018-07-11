To start working with Python use the following command:

`python`{{execute}}

Let's read the movie reviews that are supplied as a sample corpus within NLTK.

`import data_reader
documents = data_reader.read_reviews()`{{execute}}

Let's look at a few moview reviews to get a feel of the text

`example_idx = 52
document = documents[example_idx]
document`{{execute}}
