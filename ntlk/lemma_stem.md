
NLTK implements a porter stemmer:

`from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()`{{execute}}

Let's see how the porter stemmer would stem:

`porter_stemmer.stem("geese")
porter_stemmer.stem("goose")`{{execute}}
