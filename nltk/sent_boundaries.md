Let's take a look at the sample review again.
Notice that there are a lot of punctuation mistakes.

`print(sample_movie_review)`{{execute}}

In NLTK, the default sentence tokenizer is called the Punkt tokenizer.
Let's load the Punkt tokenizer:

`import nltk.data 
sentence_tokenizer = nltk.data.load('tokenizers/punkt/PY3/english.pickle')`{{execute}}

Let's create a sentences array and observe how well the punkt tokenizer
was able to split the movie review into sentences:

`sentences = sentence_tokenizer.tokenize(sample_movie_review)
print('\n------\n'.join(sentences))`{{execute}}
