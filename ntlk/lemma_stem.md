
NLTK implements a number stemmers. The popular "Porter Stemmer" which we will examine below as well as other stemmers including the "Lancaster Stemmer" and the "Snowball Stemmer". Let's take a look at the Porter Stemmer:

`from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()`{{execute}}

Let's see how the porter stemmer would stem:

`porter_stemmer.stem("know")
porter_stemmer.stem("knowingly")
porter_stemmer.stem("geese")
porter_stemmer.stem("goose")`{{execute}}

NLTK also implements a Lemmatizer based on the WordNet searchable database:

`from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()`{{execute}}

Let's see how the lemmatizer deals with the same cases we tried with the stemmer:

`wordnet_lemmatizer.lemmatize("know")
wordnet_lemmatizer.lemmatize("knowingly")
wordnet_lemmatizer.lemmatize("geese")
wordnet_lemmatizer.lemmatize("goose")`{{execute}}
